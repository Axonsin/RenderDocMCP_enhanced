"""Sync shared references into each skill's references/ directory.

Single editing source: skill-support/shared-references/*.md is copied into every
skill under .agents/skills/*/references/. If a target already exists and differs
from the source, it is reported as a conflict and skipped unless --force.

Usage:
    python sync_references.py            # sync + write manifest.json
    python sync_references.py --force    # overwrite modified targets
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


def skill_dirs():
    if not SKILLS_DIR.is_dir():
        sys.exit("skill directory not found: %s" % SKILLS_DIR)
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true",
                        help="overwrite locally modified targets")
    parser.add_argument("--check", action="store_true",
                        help="report drift without writing; exit 1 on drift")
    args = parser.parse_args()

    sources = sorted(SOURCE_DIR.glob("*.md"))
    if not sources:
        sys.exit("no shared references found in %s" % SOURCE_DIR)

    manifest = {}
    conflicts, copied, drift = [], 0, False

    for skill in skill_dirs():
        target_dir = skill / "references"
        for source in sources:
            target = target_dir / source.name
            record = {
                "source": str(source.relative_to(REPO_ROOT)).replace("\\", "/"),
                "targets": [],
            }
            source_hash = sha256(source)
            if target.exists() and sha256(target) != source_hash:
                if args.check:
                    print("DRIFT  %s" % target)
                    drift = True
                    continue
                if not args.force:
                    conflicts.append(str(target))
                    continue
            if not args.check:
                target_dir.mkdir(parents=True, exist_ok=True)
                # Byte-for-byte copy: text mode would rewrite line endings and
                # break hash comparison on Windows.
                target.write_bytes(source.read_bytes())
                copied += 1
            record["targets"].append({
                "path": str(target.relative_to(REPO_ROOT)).replace("\\", "/"),
                "sha256": source_hash,
            })
            manifest[source.name] = record

    if args.check:
        print("check complete: %s" % ("DRIFT DETECTED" if drift else "in sync"))
        return 1 if drift else 0

    if conflicts:
        print("CONFLICTS (targets modified locally, use --force to overwrite):")
        for item in conflicts:
            print("  " + item)
        return 1

    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print("synced %d file(s) into %d skill(s); manifest: %s"
          % (copied, len(skill_dirs()), MANIFEST.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
