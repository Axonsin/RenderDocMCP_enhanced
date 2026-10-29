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


def sync_in_place(staging, dest, expected_hash):
    """Replace the installed tree's files in place, one by one.

    Used when the directory-level swap fails because a running RenderDoc
    keeps handles inside the installed directory. Files removed here only
    disappear from disk; the running instance keeps its imported modules
    until it restarts.
    """
    failed = []
    for directory, dirs, files in os.walk(dest):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        rel = Path(directory).relative_to(dest)
        for name in files:
            if not (staging / rel / name).exists():
                try:
                    (Path(directory) / name).unlink()
                except OSError as exc:
                    failed.append("%s: %s" % (rel / name, exc))
    for directory, dirs, files in os.walk(staging):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        rel = Path(directory).relative_to(staging)
        (dest / rel).mkdir(parents=True, exist_ok=True)
        for name in files:
            try:
                shutil.copyfile(str(Path(directory) / name), str(dest / rel / name))
            except OSError as exc:
                failed.append("%s: %s" % (rel / name, exc))
    if failed:
        raise RuntimeError("In-place sync failed for %d file(s):\n  %s"
                           % (len(failed), "\n  ".join(failed)))
    if fingerprint(dest) != expected_hash:
        raise RuntimeError("In-place sync left the installed directory different from source")
    shutil.rmtree(str(staging), ignore_errors=True)


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
    if manifest["version"] != "3.1.0":
        raise RuntimeError("Unexpected staged extension version")
    build_hash = fingerprint(extension_src)
    if fingerprint(staging) != build_hash:
        raise RuntimeError("Staged extension differs from source")
    if dest.exists():
        backups.mkdir(parents=True, exist_ok=True)
        try:
            os.replace(str(dest), str(backup))
            os.replace(str(staging), str(dest))
        except OSError:
            # A running RenderDoc holds the installed directory open, so the
            # swap fails with access denied. The staged package was already
            # verified against the source, so sync it into place file by file.
            if backup.exists() and not dest.exists():
                os.replace(str(backup), str(dest))
            sync_in_place(staging, dest, build_hash)
            print("Directory swap was blocked (is RenderDoc running?); synced files in place.")
    else:
        os.replace(str(staging), str(dest))
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
