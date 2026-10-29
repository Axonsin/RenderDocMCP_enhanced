"""Check release versions, extension grammar and published MCP tool references."""
import ast
import asyncio
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


async def check():
    from mcp_server.server import mcp

    version = re.search(r'^version = "([^"]+)"',
                        (ROOT / "pyproject.toml").read_text(encoding="utf-8"), re.M).group(1)
    manifest = json.loads((ROOT / "renderdoc_extension/extension.json").read_text(encoding="utf-8"))
    assert version == manifest["version"] == "3.1.0"
    assert manifest["minimum_renderdoc"] == "1.46"
    extension_files = list((ROOT / "renderdoc_extension").rglob("*.py"))
    for path in extension_files:
        ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path), feature_version=(3, 6))
    tools = await mcp.list_tools()
    assert len({t.name for t in tools}) == len(tools)
    schemas = {t.name: t.parameters for t in tools}
    schema_path = ROOT / "docs/tool_schemas.json"
    if "--write-schema" in sys.argv:
        schema_path.write_text(json.dumps(schemas, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    assert json.loads(schema_path.read_text(encoding="utf-8")) == schemas, "published schema drift"
    assert schemas["get_texture_data"]["properties"]["output_mode"]["default"] == "auto"
    assert schemas["dump_draws"]["properties"]["export_constants"]["default"] is True
    assert schemas["export_shader_bundle"]["properties"]["include_event_context"]["default"] is True
    assert schemas["get_replay_diagnostics"]["properties"]["include_device_logs"]["default"] is False
    for document in ("docs/tools.md", "docs/tools_zh.md", "AGENTS.md"):
        text = (ROOT / document).read_text(encoding="utf-8")
        for field in ("output_mode", "export_constants", "include_event_context", "include_device_logs", "aspect", "region"):
            assert field in text, (document, field)
    assert "API_CONTRACT_VERSION = 3" in (ROOT/"renderdoc_extension/services/session_state.py").read_text()
    assert "IPC_VERSION = 2" in (ROOT/"renderdoc_extension/socket_server.py").read_text()
    for document in ("AGENTS.md", "docs/tools.md", "docs/tools_zh.md"):
        text = (ROOT / document).read_text(encoding="utf-8")
        missing = [tool.name for tool in tools if "`" + tool.name + "`" not in text]
        assert not missing, (document, missing)
    for name in ("open_capture", "dump_draws", "export_shader_bundle", "compare_texture_events",
                 "get_pixel_history", "run_script"):
        schema = next(t.parameters for t in tools if t.name == name)
        assert "job_id" in schema["properties"]
    subprocess.run([sys.executable, str(ROOT / "skill-support/sync_references.py"), "--check"],
                   cwd=ROOT, check=True)
    print(json.dumps({"version": version, "minimum_renderdoc": "1.46", "mcp_tools": len(tools),
                      "python36_files": len(extension_files), "references": "in_sync"}))


if __name__ == "__main__":
    asyncio.run(check())
