"""
Capture management service for RenderDoc.
"""

import renderdoc as rd


class CaptureManager:
    """Capture management service"""

    def __init__(self, ctx, invoke_fn, runtime_info=None):
        self.ctx = ctx
        self._invoke = invoke_fn
        self._runtime_info = runtime_info or {}

    def _version_fields(self):
        return {
            "extension_version": self._runtime_info.get("extension_version"),
            "renderdoc_version": self._runtime_info.get("renderdoc_version"),
            "ipc_version": self._runtime_info.get("ipc_version"),
        }

    def get_capture_status(self):
        """Check if a capture is loaded and get API info plus replay health"""
        result = {
            "loaded": False,
            "api": None,
            "filename": None,
            "remote_replay": None,
            "replay_healthy": None,
            "replay_error": None,
        }
        result.update(self._version_fields())

        if not self.ctx.IsCaptureLoaded():
            return result

        result["loaded"] = True

        try:
            result["filename"] = self.ctx.GetCaptureFilename()
        except Exception:
            pass

        # Replay health probe: GetAPIProperties + GetFatalErrorStatus round-trip
        # proves the replay controller responds; GetFatalErrorStatus surfaces
        # driver/device removal that would otherwise only show up as empty data.
        def callback(controller):
            try:
                props = controller.GetAPIProperties()
                result["api"] = str(props.pipelineType)
                result["remote_replay"] = bool(props.remoteReplay)
                result["replay_healthy"] = True
                fatal = controller.GetFatalErrorStatus()
                if not fatal.OK():
                    result["replay_healthy"] = False
                    result["replay_error"] = str(fatal.Message())
            except Exception as exc:
                result["replay_healthy"] = False
                result["replay_error"] = str(exc)

        try:
            self._invoke(callback)
        except Exception as exc:
            result["replay_healthy"] = False
            result["replay_error"] = str(exc)
        return result

    def list_captures(self, directory):
        """
        List all .rdc files in the specified directory.

        Args:
            directory: Directory path to search

        Returns:
            dict with 'captures' list containing file info
        """
        import os
        import datetime

        # Validate directory exists
        if not os.path.isdir(directory):
            raise ValueError("Directory not found: %s" % directory)

        captures = []

        try:
            for filename in os.listdir(directory):
                if filename.lower().endswith(".rdc"):
                    filepath = os.path.join(directory, filename)
                    if os.path.isfile(filepath):
                        stat = os.stat(filepath)
                        # Format timestamp as ISO 8601
                        mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
                        captures.append({
                            "filename": filename,
                            "path": filepath,
                            "size_bytes": stat.st_size,
                            "modified_time": mtime.isoformat(),
                        })
        except Exception as e:
            raise ValueError("Failed to list directory: %s" % str(e))

        # Sort by modified time (newest first)
        captures.sort(key=lambda x: x["modified_time"], reverse=True)

        return {
            "directory": directory,
            "count": len(captures),
            "captures": captures,
        }

    def open_capture(self, capture_path):
        """
        Open a capture file in RenderDoc.

        Args:
            capture_path: Full path to the .rdc file

        Returns:
            dict with success status and capture info
        """
        import os

        # Validate file exists
        if not os.path.isfile(capture_path):
            raise ValueError("Capture file not found: %s" % capture_path)

        # Validate extension
        if not capture_path.lower().endswith(".rdc"):
            raise ValueError("Invalid file type. Expected .rdc file: %s" % capture_path)

        # Create ReplayOptions with defaults
        opts = rd.ReplayOptions()

        # Open the capture
        # LoadCapture will automatically close any existing capture
        try:
            self.ctx.LoadCapture(
                capture_path,   # captureFile
                opts,           # ReplayOptions
                capture_path,   # origFilename (same as capture path)
                False,          # temporary (False = permanent load)
                True,           # local (True = local file)
            )
        except Exception as e:
            raise ValueError("Failed to open capture: %s" % str(e))

        # Verify the capture was loaded
        if not self.ctx.IsCaptureLoaded():
            raise ValueError("Failed to load capture (unknown error)")

        # Get capture info
        result = {
            "success": True,
            "capture_path": capture_path,
            "filename": os.path.basename(capture_path),
        }
        result.update(self._version_fields())

        # Get API type if possible (may require replay thread)
        try:
            api_result = {"api": None}

            def callback(controller):
                try:
                    props = controller.GetAPIProperties()
                    api_result["api"] = str(props.pipelineType)
                except Exception:
                    pass

            self._invoke(callback)
            if api_result["api"]:
                result["api"] = api_result["api"]
        except Exception:
            pass

        return result
