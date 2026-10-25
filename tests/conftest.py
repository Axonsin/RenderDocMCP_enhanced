"""Pytest configuration for the MCP test-suite.

`tests/blender_tests/` contains job artifacts and Blender-side scripts that run
inside Blender's Python (they import `bpy`). They are not unit tests.
"""

collect_ignore_glob = ["blender_tests/*", "blender_tests/**/*"]
