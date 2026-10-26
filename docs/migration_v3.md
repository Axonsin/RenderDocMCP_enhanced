# Migrating to RenderDoc MCP 3.0

Server/extension version **3.0.0**, API contract **3**, file IPC **2**. Minimum
RenderDoc remains **1.46**; extension code remains Python 3.6 standard-library only.
This release intentionally changes defaults and response transport. Keep the
[2.0 migration](migration_v2.md) and [2.0 validation](validation_v2.md) as history.

## Upgrade together

1. Finish/export any needed current-session work. Save shader edits before reload;
   capture reload invalidates binding IDs, jobs and replacement sessions.
2. Update the Python package and run `python scripts/install_extension.py`. The
   installer retains a rollback copy. Reload the extension or restart RenderDoc,
   then restart the client's MCP connection so the tool schemas refresh.
3. Check `get_capture_status`: both versions must be 3.0.0, contract 3, IPC 2, and
   the extension build hash must match the deployed source. A mismatch is an
   explicit API_VERSION_MISMATCH error, not a partial compatibility mode.
4. Reopen the capture with its original replay target, verify health, and issue a
   known query. Do not re-use old binding IDs or resume jobs from another session.

## Caller changes

- `dump_draws(..., export_constants=True)` is now the default. Full constant bytes,
  layout and decoded trees are file artifacts; job items contain summaries/paths.
- `export_shader_bundle(..., include_event_context=True, export_constants=True)`
  now includes the event's stage bindings and constants. Set flags false explicitly
  for a shader-only export. Missing requested exports affect completion status.
- `get_texture_data` defaults to `output_mode="auto"`: raw results at most 256 KiB
  contain content_base64; larger results contain path/metadata_path/sha256 instead.
  Callers must branch on output_mode. Explicit inline above the threshold fails.
  `output_mode="file"` always creates a binary file and JSON sidecar.
- Optional aspect=all/depth/stencil and top-left region={x,y,width,height} select
  numeric data. Verified D16/D24S8 depth is float32 LE, stencil is uint8. Raw all
  preserves original packed bytes. Unknown layouts remain opaque, not decoded.
- `compare_texture_events(..., aspect="all")` accepts depth/stencil selection and
  an explicit MSAA sample. Color storage/linear domains retain their meaning.
- `capture_session` is shared across capture, pipeline and shader services.
  Shader editor generation is separately named `edit_session`.

## Failure and diagnostics

Disconnected/fatal/API-inconsistent replay never returns an apparently valid empty
pipeline. Existing event restore guarantees remain; a restore failure invalidates
the result. No native operation is automatically resubmitted on timeout.

`get_replay_diagnostics()` reads persisted state without contacting the UI/replay
thread. It returns paths, hashes and warnings. Device evidence requires explicit
`include_device_logs=True`; collection uses configured ADB read-only operations,
with bounded time/size and partial-result reporting. It never installs, resets,
restarts services or uploads evidence. See the [tool contract](tools.md) for limits.

Transient response-file access errors retry the same file within the original
deadline. Cleanup failures retain validated results. RESULT_PENDING means the
operation was submitted and its outcome is unknown; inspect state/diagnostics.

## Validation commands

```powershell
python -m pytest tests -q
python scripts/check_contracts.py
python skill-support/sync_references.py --check
git diff --check
```

Published schemas: [tool_schemas.json](tool_schemas.json).
Device results and limitations: [validation_v3.md](validation_v3.md).
