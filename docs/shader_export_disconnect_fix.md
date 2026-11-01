# Shader bundle export remote timeout (2026-11-02)

## Diagnosis

The failing request was `export_shader_bundle(action_event_id=681,
stage="fragment")` on the GFL2 frame21389 Vulkan capture, replayed on Android
through RenderDoc 1.46. Both event context and constants were enabled.

An instrumentation-only build reproduced the disconnect. Its flushed
`timings.jsonl` shows that SPIR-V disassembly took 0.016 seconds, followed by
12 local AMDIL/GCN/RDNA compiler targets taking approximately 0.42-0.48 seconds
each. The complete disassembly loop lasted approximately 5.4 seconds without
remote replay requests. Android logged `Timeout of 5.000000 seconds exceeded
in recv`, closed the connection, and remained ready to accept a new connection.
The next constant-buffer request discovered the closed connection. The final
error was consequently `REPLAY_RESTORE_FAILED: REPLAY_UNHEALTHY: Connection lost
to remote server`. Constant reading took only approximately 0.031 seconds;
reflection serialization was also short. This was cumulative local compiler
work starving remote communication, rather than a constant-buffer size problem.

## Changes

- Export detached shader bytes, reflection, event bindings and constants first.
- Execute each disassembly target in its own replay job step. Each step
  reacquires its pipeline/reflection on replay, restores the selected event and
  checks replay health before yielding to the UI/job scheduler. No replay-owned
  SWIG object is retained across callbacks or sent to a worker.
- Keep all disassembly targets and per-target unavailable results. Cancellation
  remains cooperative between targets, and replay failure fails the job.
- Flush stage start/end/failure records to a per-export `timings.jsonl`.
  The result/manifest exposes `timings_path`; failed jobs retain boundary logs
  in `<output_dir>/<job_id>/timings.jsonl` even without a completed manifest.
- Correct decompiler argument substitution to use canonical `fragment`,
  `tess_control`, and `tess_eval` names, with task/mesh mappings when supported.
  The old pixel/hull/domain dictionary raised `KeyError` before launching the
  configured external tool, including for the SPIR-V assembly path.

## Validation

- Unit tests cover all six standard stages through the real QProcess argument
  construction, and ensure every disassembly target has a separate event
  restore boundary, including when a local compiler is unavailable.
- Full suite: 284 passed, 98 subtests passed.
- Live EID 681 export: completed, all 14 targets retained, three constant blocks
  exported. Largest disassembly step approximately 0.61 seconds, compared with
  the old uninterrupted loop of approximately 5.4 seconds. Total job duration
  approximately 9.2 seconds includes scheduling and event restoration.
- Live EID 739 export: completed with 14 targets and all three constant blocks.
- Live EID 681 `spirv_asm`: spirv-dis/spirv-as, 247864 source characters.
- Live EID 681 `glsl`: SPIRV-Cross, 53600 source characters.
- Remote replay remains healthy and the selected event remains 951. No shader
  replacement was applied during validation.

Source and installed extension fingerprints are checked during deployment;
RenderDoc's **Reload changed extensions** activates the installed code.
Evidence, including the instrumentation-only failing run and successful
exports, is outside Git at
`D:/Unity_Projects/GamesRenderReplica_evidence/diagnostics/shader_export_fix/`.

Splitting the loop fixes the observed cumulative timeout. It cannot forcibly
interrupt an individual native driver/compiler call if that call itself hangs.
