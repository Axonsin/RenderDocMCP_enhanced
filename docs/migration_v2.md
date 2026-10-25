# RenderDoc MCP 2.0 migration / 迁移说明

Requires RenderDoc 1.46 or newer. Upgrade the MCP server and UI extension together;
API contract version 2 is checked on every request/reply. File IPC remains version 2.

Implementation reference: official RenderDoc v1.46, commit
[`e4bd23b671d3d5a747ff5221dbe08a63eb6ca200`](https://github.com/baldurk/renderdoc/tree/e4bd23b671d3d5a747ff5221dbe08a63eb6ca200).
The relevant contracts are [Mesh Viewer](https://github.com/baldurk/renderdoc/blob/e4bd23b671d3d5a747ff5221dbe08a63eb6ca200/qrenderdoc/Windows/BufferViewer.cpp),
[replay/event and pixel-history handling](https://github.com/baldurk/renderdoc/blob/e4bd23b671d3d5a747ff5221dbe08a63eb6ca200/renderdoc/replay/replay_controller.cpp),
[shader layouts/values](https://github.com/baldurk/renderdoc/blob/e4bd23b671d3d5a747ff5221dbe08a63eb6ca200/renderdoc/api/replay/shader_types.h),
and [remote capture lifecycle](https://github.com/baldurk/renderdoc/blob/e4bd23b671d3d5a747ff5221dbe08a63eb6ca200/qrenderdoc/Code/ReplayManager.cpp).

## Async operations / 异步操作

`open_capture`, `dump_draws`, `export_shader_bundle`, `compare_texture_events` and
`get_pixel_history` return a persisted job descriptor immediately. Poll
`get_job_status(job_id, offset=0, limit=100)`; the full manifest stays on disk.
The client creates the ID before submission and includes it in timeout errors.
Batch `items` are compact draw summaries with `details_path` for the complete
binding/layout record and `artifact_paths` for files. Texture summary counts refer
to binding references; the final manifest's textures_saved counts distinct contents.
Completed detail objects are released from memory; historical pages are loaded on demand.
Reuse the same ID and identical arguments for idempotent submission. Conflicting
arguments are rejected. Job completion is not user-goal or reconstruction acceptance.

States: `queued`, `running`, `paused`, `cancelling`, `completed`,
`completed_with_errors`, `failed`, `cancelled`, `interrupted`.
`stalled` reports no progress for 30 seconds, not proof that a native call failed.
`cancel_job` is cooperative between steps; native loading is not cancellable.
`resume_job(job_id, texture_budget=48)` continues paused/cancelled batches only
within the same capture session and replay revision. Restarted/stale work must be
submitted as a new job. Other replay queries receive `REPLAY_BUSY` during a job;
status/context/cancel calls do not access the replay controller. MCP `get_job_status`
reads atomic disk snapshots even while the UI is blocked; `status_source` identifies
this read. Cancelling non-cancellable native stages fails immediately.
Cancellation requests are atomic control files, consumed at a cooperative boundary;
a request can be accepted while an ongoing operation is still finishing. Large manifest
writes and ROI arithmetic run on a Python worker, keeping the UI/remote keepalive responsive.

```python
job = open_capture(capture_path="E:/captures/frame.rdc", file_location="local",
                   replay_target="remote", remote_host="adb://DEVICE_SERIAL")
get_job_status(job_id=job["job_id"])
job = dump_draws(output_dir="D:/exports", action_event_ids=[155, 169], max_textures=48)
get_job_status(job_id=job["job_id"])
resume_job(job_id=job["job_id"], texture_budget=48)  # when paused at the texture limit
```

## Remote loading / 远端加载

`file_location=local|remote` describes the file, independently of
`replay_target=current|local|remote` (default `local` file / `current` replay context).
`remote_host` is accepted only with `replay_target=remote`; omit it to reuse a
connected remote host. Local files are uploaded through RenderDoc; remote paths
are checked remotely and loaded with `local=False`. No local dummy file is needed.
Only the explicitly selected host can be launched, using the official configured
launch mechanism. No automatic installation/upgrades/device restart occur.
Android automatic startup is audited for 1.46 only: a read-only check of the active
user, primary ABI and installed package versionCode/build hash must prove that
RenderDoc's native launcher will skip its install branch. Missing/mismatched packages
are rejected; other RenderDoc versions require manually starting the server first.
Connection selection uses CaptureContext so UI and ReplayManager contexts agree.
`get_replay_context()` returns configured/current hosts and cached discovery.
Protocol discovery is deferred while a capture is loaded to avoid disturbing ADB replay.
Android folder browsing enumerates applications, so file preflight uses a temporary
download of real capture bytes and native metadata/hash checks. Uploaded captures
are read back and verified before loading; no local placeholder for a remote path is used.

Preflight precedes capture replacement. Native LoadCapture failures can still open
RenderDoc's own modal dialog: the extension cannot force-close it or safely abort
an in-progress native call. A running/stalled job is not safe to blindly retry.

## Mesh and constants / 网格与常量

- `get_buffer_contents` gains `action_event_id`; explicit reads are after the action,
  restore replay and retain the 256 KiB inline limit. Omission uses the current event.
- Mesh tools gain `view_index=0` (VSIn requires 0). Post-VS uses RenderDoc's returned
  remapped index buffer, not an assumed sequential stream. `get_mesh_data.indices`
  is populated for all stages; pagination/total_count count draw references.
- CSV stores a unique vertex table and `.idx` stores topology references; `-1`
  indicates primitive restart. Keep `topology`, do not assume every stream is triangles.
- Invalid offsets, short indices or missing required attributes are errors, never
  fabricated zero vertices. Repeated/degenerate/nonfinite data is diagnosed, not
  automatically labelled a driver failure. Quality sampling limits are reported.
- Constant `SInt` values use `s32v`. Decoded matrix values are always row-major;
  `layout.storage_order` describes original memory separately. Vulkan dynamic offsets
  are already included in GetConstantBlock ranges and must not be added again.
- `dump_draws.object_matrix` is removed: 720-byte blocks do not identify object
  transforms. Use reflected constant paths/layouts and shader evidence. No automatic
  UV/albedo/normal/object-transform semantics are assigned.

## Batch outputs / 批量导出

Replace `mesh_dir`, `texture_dir`, `summary_path` with required absolute `output_dir`.
Files live in `output_dir/<job_id>/` with a provenance manifest. Choose exactly one
of `action_event_ids` (1..256 actual draws), `marker_filter`, `action_event_id_range`.
Range/marker selection resolves actual draws; explicit non-draw IDs are rejected.
`mesh_stage=VSIn|VSOut|GSOut`, `instances=[0]`, `view_index=0` select geometry.
`max_textures=48` is a per-run allowance; exhaustion pauses, resume adds allowance.
`max_texture_edge=None`, `skip_depth=False` expose optional filtering explicitly.

Bindings retain descriptor subresources, samplers, raw vertex layouts, shader IDs
and constant locations. Texture exports record the exact event/mip/slice/sample,
source format and conversion path. Same filenames do not authorize reuse. Reuse is
scoped to capture/revision/event/subresource/conversion; cross-event content is
retrieved again, then deduplicated by the exported content SHA256.

## Investigation tools / 调查工具

- `export_shader_bundle(action_event_id, stage, output_dir)`: raw binary/text with
  encoding, disassembly targets, reflected signatures/layouts/resources/samplers,
  embedded sources only when present, file hashes and manifest.
- `compare_texture_events(resource_id, action_event_id_a, action_event_id_b, region,
  output_dir, mip=0, slice_index=0, sample=0, depth_slice=0, value_domain=storage)`:
  region is `{x,y,width,height}`, top-left. `linear` applies sRGB EOTF to RGB only.
  Supports Vulkan/D3D11/D3D12 regular 8/16/32-bit integer/normalized and 16/32/64-bit
  float, R10G10B10A2 and R11G11B10. Unsupported layouts return `UNSUPPORTED_FORMAT`,
  never PNG fallback. Limits: 64 MiB/subresource, 262144 ROI pixels. Signed B-minus-A
  differences are little-endian float64, pixel-interleaved on disk. Metrics explicitly
  count nonfinite samples; metrics are null when no finite deltas exist. Component
  inequality treats NaN as unequal and is explicitly identified in the result.
  This is observed difference, not isolated draw contribution.
- `get_pixel_history(resource_id, x, y, action_event_id, output_dir, ...)`: native
  history up to the action. Check `available`; device support and native validity
  restrictions apply. Fragments are paginated through get_job_status.

## Verification / 验证

Unit/IPC tests use real API-shaped fixtures. Live Vulkan checks additionally compare
native viewport/scissor/blend, index/xyzw, UBO bytes and HDR probes, exercise >30s
jobs, pause/cancel/resume, verify capture/revision invalidation and restored replay.
D3D has regression coverage here, not a claimed live GPU certification. Test media,
RDCs and local evidence remain excluded from Git.
