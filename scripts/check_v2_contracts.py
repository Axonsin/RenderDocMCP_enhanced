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
    assert version == manifest["version"] == "2.0.0"
    assert manifest["minimum_renderdoc"] == "1.46"
    extension_files = list((ROOT / "renderdoc_extension").rglob("*.py"))
    for path in extension_files:
        ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path), feature_version=(3, 6))
    tools = await mcp.list_tools()
    assert len(tools) == 44
    for document in ("AGENTS.md", "docs/tools.md", "docs/tools_zh.md"):
        text = (ROOT / document).read_text(encoding="utf-8")
        missing = [tool.name for tool in tools if "`" + tool.name + "`" not in text]
        assert not missing, (document, missing)
    for name in ("open_capture", "dump_draws", "export_shader_bundle", "compare_texture_events", "get_pixel_history"):
        schema = next(t.parameters for t in tools if t.name == name)
        assert "job_id" in schema["properties"]
    subprocess.run([sys.executable, str(ROOT / "skill-support/sync_references.py"), "--check"],
                   cwd=ROOT, check=True)
    print(json.dumps({"version": version, "minimum_renderdoc": "1.46", "mcp_tools": len(tools),
                      "python36_files": len(extension_files), "references": "in_sync"}))


if __name__ == "__main__":
    asyncio.run(check())
