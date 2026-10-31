# Replay-thread CPU processing and remote disconnects

`get_texture_data(aspect="depth")` previously converted every depth pixel inside
`at_event` / `BlockInvoke`. On the tested 2048×2048 D16 image this took 6.36 s,
exceeding the remote server's 5 s receive timeout while no native requests were
sent. Native readback itself took 22–29 ms. A diagnostic control kept the same
conversion but sent periodic native queries; it completed without disconnecting.

## Implementation

- Replay callbacks acquire owned `bytes` and detached Python format/mesh metadata,
  then restore the selected event before conversion starts. Workers never access
  a replay controller, CaptureContext, or replay-owned format object.
- Synchronous texture and mesh tools use a CPU worker while a nested Qt event loop
  services UI timers. Moving conversion to the UI thread alone would still starve
  the timer which schedules RenderDoc's remote pings. The IPC server's existing
  busy flag prevents reentrant request handling while waiting.
- Texture ROI/aspect conversion, zero checks, hashing and file transport run on
  that worker. Mesh index decoding, vertex decoding, bounds/quality computation,
  deduplication and CSV/index writing likewise run off replay.
- Async texture comparisons separate native readback from per-pixel decoding and
  comparison worker steps. Batch mesh writing and texture hashing/deduplication,
  shader evidence writing/hashing and pixel-history manifest writing use workers.
- Native calls such as SaveTexture, DisassembleShader, PixelHistory, shader and
  constant reflection access stay on replay. Constant binary/JSON writes were
  already worker steps. Caller-supplied run_script code still runs on replay;
  this change cannot automatically split arbitrary user scripts into workers.

No API/schema, format conversion, remote timeout configuration or capture data
was changed. A file/driver/native operation failure can still disconnect replay;
this fix addresses the identified CPU-processing starvation.

## Validation (2026-10-31)

- `python -m pytest tests -q`: 281 passed, 92 subtests passed.
- All extension Python files parse with Python 3.6 grammar; `git diff --check` passes.
- Installed and reloaded in RenderDoc 1.46 with extension 3.1.0, API contract 3,
  IPC 2; current Android Vulkan replay.
- Previously failing full request: resource 102709, action 539, mip/slice/sample 0,
  aspect depth, no ROI. Ordinary MCP call now returns all 4,194,304 pixels as
  16,777,216 bytes of normalized float32. First build: 6.56 s. Final build: 7.52 s.
  Replay remains healthy; selected event restored to 1125, no shader replacements.
- Depth SHA-256 matches independently verified output:
  `0f3e93058b4209688fe1080b885a1d487ba41cc818db605641b20c8ae310421d`.
- EID 557 VSOut CSV: 15,601 vertices / 59,220 indices; both CSV and index bytes
  match the earlier verified export exactly. Mesh summary also succeeds.
- 512×512 depth event comparison, fragment shader bundle with constants, and a
  batch export of meshes/constants complete without replay loss.

Raw local evidence is outside Git under
`D:/Unity_Projects/GamesRenderReplica_evidence/diagnostics/replay_cpu_fix/`.
The original controlled diagnosis remains in `diagnostics/depth_decode_root_cause/`.
