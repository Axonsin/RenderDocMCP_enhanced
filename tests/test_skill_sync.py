"""Regression tests for skill-support/sync_references.py."""

import importlib.util
import json
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_sync():
    spec = importlib.util.spec_from_file_location(
        "sync_references_under_test", ROOT / "skill-support" / "sync_references.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SYNC = load_sync()


class SyncFixture:
    """Temporary repo layout: shared-references source + N skill directories."""

    def __init__(self):
        self._tmp = tempfile.TemporaryDirectory()
        base = Path(self._tmp.name)
        self.repo = base
        self.source = base / "shared-references"
        self.source.mkdir()
        self.skills = base / "skills"
        self.manifest = base / "manifest.json"

    def write_source(self, name, text):
        (self.source / name).write_text(text, encoding="utf-8")

    def add_skill(self, name):
        directory = self.skills / name
        directory.mkdir(parents=True, exist_ok=True)
        return directory

    def target(self, skill, name):
        return self.skills / skill / "references" / name

    def close(self):
        self._tmp.cleanup()


class SyncReferenceTests(unittest.TestCase):
    def setUp(self):
        self.fx = SyncFixture()
        self.fx.write_source("tool-usage.md", "v1\n")
        self.fx.add_skill("skill-a")
        self.fx.add_skill("skill-b")

    def tearDown(self):
        self.fx.close()

    def sync(self, **kwargs):
        return SYNC.sync(self.fx.source, self.fx.skills, self.fx.manifest,
                         self.fx.repo, **kwargs)

    def test_check_fails_when_target_missing(self):
        # Review regression: a fully missing target must fail --check, not pass.
        self.assertEqual(self.sync(check=True), 1)  # nothing synced yet
        self.assertEqual(self.sync(), 0)
        self.assertEqual(self.sync(check=True), 0)
        self.fx.target("skill-a", "tool-usage.md").unlink()
        self.assertEqual(self.sync(check=True), 1)

    def test_manifest_accumulates_all_skill_targets(self):
        # Review regression: every skill's target is recorded, not just the last.
        self.assertEqual(self.sync(), 0)
        manifest = json.loads(self.fx.manifest.read_text(encoding="utf-8"))
        entry = manifest["tool-usage.md"]
        paths = [item["path"] for item in entry["targets"]]
        self.assertEqual(len(paths), 2)
        self.assertIn("skills/skill-a/references/tool-usage.md", paths)
        self.assertIn("skills/skill-b/references/tool-usage.md", paths)

    def test_source_only_update_does_not_require_force(self):
        # Review regression: updating only the shared source is a normal sync,
        # not a "locally modified target" conflict.
        self.assertEqual(self.sync(), 0)
        self.fx.write_source("tool-usage.md", "v2\n")
        self.assertEqual(self.sync(), 0)
        self.assertIn("v2", self.fx.target("skill-a", "tool-usage.md").read_text())
        self.assertIn("v2", self.fx.target("skill-b", "tool-usage.md").read_text())

    def test_locally_modified_target_conflicts_then_force_overwrites(self):
        self.assertEqual(self.sync(), 0)
        self.fx.target("skill-a", "tool-usage.md").write_text("local edit\n")
        self.assertEqual(self.sync(), 1)  # conflict reported, no silent overwrite
        self.assertIn("local edit",
                      self.fx.target("skill-a", "tool-usage.md").read_text())
        self.assertEqual(self.sync(force=True), 0)
        self.assertIn("v1", self.fx.target("skill-a", "tool-usage.md").read_text())

    def test_source_update_after_local_edit_still_conflicts(self):
        self.assertEqual(self.sync(), 0)
        self.fx.target("skill-a", "tool-usage.md").write_text("local edit\n")
        self.fx.write_source("tool-usage.md", "v2\n")
        # Target differs from both the new source and its last-synced hash.
        self.assertEqual(self.sync(), 1)

    def test_stale_target_removed_when_source_deleted(self):
        self.fx.write_source("old-contract.md", "old\n")
        self.assertEqual(self.sync(), 0)
        (self.fx.source / "old-contract.md").unlink()
        self.assertEqual(self.sync(check=True), 1)  # stale target is drift
        self.assertEqual(self.sync(), 0)
        self.assertFalse(self.fx.target("skill-a", "old-contract.md").exists())
        self.assertTrue(self.fx.target("skill-a", "tool-usage.md").exists())


if __name__ == "__main__":
    unittest.main()
