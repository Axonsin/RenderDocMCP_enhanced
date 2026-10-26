"""
RenderDoc Extension Installer
Copies the extension to RenderDoc's extension directory.
"""

import os
import shutil
import sys
import uuid
import hashlib
from pathlib import Path


def fingerprint(root):
    digest = hashlib.sha256()
    for directory, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__")
        for name in sorted(files):
            if name.endswith((".py", ".json")):
                path = Path(directory) / name
                digest.update(path.relative_to(root).as_posix().encode("utf-8"))
                digest.update(path.read_bytes())
    return digest.hexdigest()


def get_extension_dir():
    """Get RenderDoc extension directory"""
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        if appdata:
            return Path(appdata) / "qrenderdoc" / "extensions"
    else:
        home = Path.home()
        return home / ".local" / "share" / "qrenderdoc" / "extensions"

    raise RuntimeError("Cannot determine RenderDoc extension directory")


def install():
    """Install the extension"""
    # Source directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    extension_src = project_root / "renderdoc_extension"

    if not extension_src.exists():
        print("Error: Extension source not found at %s" % extension_src)
        sys.exit(1)

    # Destination directory
    ext_dir = get_extension_dir()
    ext_dir.mkdir(parents=True, exist_ok=True)

    dest = ext_dir / "renderdoc_mcp_bridge"

    # Stage a complete package before touching the installed version. Keep the
    # previous package outside the extension discovery directory for rollback.
    staging_parent = ext_dir.parent / "mcp_bridge_staging"
    staging_parent.mkdir(parents=True, exist_ok=True)
    staging = staging_parent / uuid.uuid4().hex
    backups = ext_dir.parent / "mcp_bridge_backups"
    backup = backups / uuid.uuid4().hex
    root = ext_dir.parent.resolve()
    for target in (dest, staging, backup):
        if os.path.commonpath([str(root), str(target.resolve())]) != str(root):
            raise RuntimeError("Installation target escapes qrenderdoc directory")
    shutil.copytree(extension_src, staging,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo"))
    import json
    manifest = json.loads((staging / "extension.json").read_text(encoding="utf-8"))
    if manifest["version"] != "3.0.0":
        raise RuntimeError("Unexpected staged extension version")
    build_hash = fingerprint(extension_src)
    if fingerprint(staging) != build_hash:
        raise RuntimeError("Staged extension differs from source")
    if dest.exists():
        backups.mkdir(parents=True, exist_ok=True)
        os.replace(str(dest), str(backup))
    try:
        os.replace(str(staging), str(dest))
    except Exception:
        if backup.exists() and not dest.exists():
            os.replace(str(backup), str(dest))
        raise
    if backup.exists():
        print("Rollback package: %s" % backup)
    print("Extension installed to %s" % dest)
    print("Build SHA256: %s" % build_hash)
    print("  (__pycache__ directories excluded)")
    print("")
    print("Please restart RenderDoc and enable the extension in:")
    print("  Tools > Manage Extensions > RenderDoc MCP Bridge")


def uninstall():
    """Uninstall the extension"""
    ext_dir = get_extension_dir()
    dest = ext_dir / "renderdoc_mcp_bridge"

    if dest.resolve().parent != ext_dir.resolve() or dest.is_symlink():
        raise RuntimeError("Uninstall target escapes extension directory")

    if dest.exists():
        shutil.rmtree(dest)
        print("Extension uninstalled from %s" % dest)
    else:
        print("Extension not found at %s" % dest)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "uninstall":
        uninstall()
    else:
        install()
