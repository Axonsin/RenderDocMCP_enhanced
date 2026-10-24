"""Sync shared references into each skill's references/ directory.

Single editing source: skill-support/shared-references/*.md is copied into every
skill under .agents/skills/*/references/.

Source updates vs local edits are told apart via the previous manifest: a target
whose content still matches its last-synced hash is "unchanged since sync" and
is safely refreshed when the source changes; a target that matches neither the
source nor its last-synced hash was modified locally and conflicts unless
--force. Targets whose source disappeared are removed (clean, hash-verified).

Usage:
    python sync_references.py            # sync + write manifest
    python sync_references.py --force    # overwrite locally modified targets
    python sync_references.py --check    # report drift only, exit 1 on drift
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = SUPPORT_DIR / "shared-references"
REPO_ROOT = SUPPORT_DIR.parent
SKILLS_DIR = REPO_ROOT / ".agents" / "skills"
MANIFEST = SUPPORT_DIR / "references-manifest.json"


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(path, repo_root):
    return str(path.relative_to(repo_root)).replace("\\", "/")


def load_previous(manifest_path):
    if not manifest_path.exists():
        return {}
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except ValueError:
        return {}


def previous_target_hash(previous, target_rel):
    for entry in previous.values():
        for item in entry.get("targets", []):
            if item.get("path") == target_rel:
                return item.get("sha256")
    return None


def sync(source_dir, skills_dir, manifest_path, repo_root, force=False, check=False):
    """Sync shared references into skill trees. Returns a process exit code."""
    sources = sorted(source_dir.glob("*.md"))
    if not sources:
        print("no shared references found in %s" % source_dir)
        return 1
    if not skills_dir.is_dir():
        print("skill directory not found: %s" % skills_dir)
        return 1
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not skill_dirs:
        print("no skill directories found in %s" % skills_dir)
        return 1

    previous = load_previous(manifest_path)
    # Paths the previous manifest synced; anything left over after processing
    # the current sources is stale (its source was deleted).
    managed = {}
    for entry in previous.values():
        for item in entry.get("targets", []):
            managed[item["path"]] = item.get("sha256")

    manifest = {}
    conflicts, drift = [], False
    copied = removed = 0

    for source in sources:
        source_hash = sha256(source)
        record = {"source": rel(source, repo_root), "targets": []}
        for skill in skill_dirs:
            target = skill / "references" / source.name
            target_rel = rel(target, repo_root)
            managed.pop(target_rel, None)
            # Accumulate every skill's target; never let the last skill win.
            record["targets"].append({"path": target_rel, "sha256": source_hash})

            if check:
                # A missing target is drift, not a silent success.
                if not target.exists():
                    print("DRIFT  %s (missing)" % target_rel)
                    drift = True
                elif sha256(target) != source_hash:
                    print("DRIFT  %s" % target_rel)
                    drift = True
                continue

            if not target.exists():
                (skill / "references").mkdir(parents=True, exist_ok=True)
                target.write_bytes(source.read_bytes())
                copied += 1
                continue

            target_hash = sha256(target)
            if target_hash == source_hash:
                continue  # already in sync
            last = previous_target_hash(previous, target_rel)
            if force or last == target_hash:
                # Source updated (or override requested); target untouched
                # since the last sync, so refreshing it is safe.
                target.write_bytes(source.read_bytes())
                copied += 1
            else:
                conflicts.append(target_rel)
        manifest[source.name] = record

    for target_rel in sorted(managed):
        stale = repo_root / target_rel
        if not stale.exists():
            continue  # already clean
        if check:
            print("DRIFT  %s (stale, source removed)" % target_rel)
            drift = True
            continue
        if force or sha256(stale) == managed[target_rel]:
            stale.unlink()
            removed += 1
        else:
            conflicts.append(target_rel)

    if check:
        print("check complete: %s" % ("DRIFT DETECTED" if drift else "in sync"))
        return 1 if drift else 0

    if conflicts:
        print("CONFLICTS (targets modified locally, use --force to overwrite):")
        for item in conflicts:
            print("  " + item)
        return 1

    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print("synced %d file(s) into %d skill(s), removed %d stale; manifest: %s"
          % (copied, len(skill_dirs), removed, manifest_path.name))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true",
                        help="overwrite locally modified targets")
    parser.add_argument("--check", action="store_true",
                        help="report drift without writing; exit 1 on drift")
    args = parser.parse_args()
    return sync(SOURCE_DIR, SKILLS_DIR, MANIFEST, REPO_ROOT,
                force=args.force, check=args.check)


if __name__ == "__main__":
    sys.exit(main())
