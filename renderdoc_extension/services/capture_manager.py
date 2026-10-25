"""
Capture management service for RenderDoc.
"""

import renderdoc as rd
import os
import hashlib
import tempfile
import re


class CaptureManager:
    """Capture management service"""

    def __init__(self, ctx, invoke_fn, runtime_info=None, session=None, jobs=None):
        self.ctx = ctx
        self._invoke = invoke_fn
        self._runtime_info = runtime_info or {}
        self.session, self.jobs = session, jobs
        self._discovered = None

    def _version_fields(self):
        return {
            "extension_version": self._runtime_info.get("extension_version"),
            "renderdoc_version": self._runtime_info.get("renderdoc_version"),
            "ipc_version": self._runtime_info.get("ipc_version"),
        }

    @staticmethod
    def _capture_file_facts(path):
        capture = rd.OpenCaptureFile()
        try:
            outcome = capture.OpenFile(path, "", None)
            if not outcome.OK():
                raise ValueError("CAPTURE_PRECHECK_FAILED: %s" % outcome.Message())
            api = capture.DriverName()
        finally:
            capture.Shutdown()
        digest = hashlib.sha256()
        with open(path, "rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
        return {"capture_sha256": digest.hexdigest(), "capture_api": api,
                "capture_size_bytes": os.path.getsize(path)}

    def _remote_file_facts(self, path, download):
        # Android's ListFolder is application/activity browsing, not a file
        # existence API. Verify real capture bytes via the official transfer
        # interface, never by creating the requested remote path locally.
        with tempfile.TemporaryDirectory(prefix="renderdoc_mcp_preflight_") as folder:
            temporary = os.path.join(folder, "capture.rdc")
            download(path, temporary)
            if not os.path.isfile(temporary) or os.path.getsize(temporary) == 0:
                raise ValueError("REMOTE_FILE_UNAVAILABLE: capture download returned no data")
            return self._capture_file_facts(temporary)

    def _android_query(self, serial, arguments):
        """Read-only ADB queries using RenderDoc's documented tool precedence."""
        import shutil
        import subprocess
        executable = "adb.exe" if os.name == "nt" else "adb"
        configured = getattr(self.ctx.Config(), "Android_SDKPath", "")
        if hasattr(rd, "GetConfigSetting"):
            setting = rd.GetConfigSetting("Android.SDKDirPath")
            if setting is not None:
                configured = setting.AsString()
        candidates = [os.path.join(configured, "platform-tools", executable)] if configured else []
        candidates.append(shutil.which(executable))
        for name in ("ANDROID_HOME", "ANDROID_SDK_ROOT", "ANDROID_SDK", "ANDROID_SDK_HOME"):
            sdk = os.environ.get(name)
            if sdk and os.path.isdir(sdk):
                candidates.append(os.path.join(sdk, "platform-tools", executable))
                break
        if not any(path and os.path.isfile(path) for path in candidates):
            from PySide2.QtCore import QCoreApplication
            candidates.append(os.path.join(QCoreApplication.applicationDirPath(), "plugins", "android", executable))
        adb = next((p for p in candidates if p and os.path.isfile(p)), None)
        if adb is None:
            raise RuntimeError("REMOTE_START_REQUIRES_MANUAL: cannot locate the configured ADB for read-only package checks")
        command = [adb, "-s", serial, "shell"] + list(arguments)
        options = {"stdout": subprocess.PIPE, "stderr": subprocess.PIPE,
                   "universal_newlines": True, "encoding": "utf-8", "errors": "replace", "timeout": 10}
        if os.name == "nt":
            options["creationflags"] = 0x08000000  # CREATE_NO_WINDOW
        outcome = subprocess.run(command, **options)
        if outcome.returncode:
            raise RuntimeError("REMOTE_START_REQUIRES_MANUAL: ADB package query failed: %s" % outcome.stderr[:200])
        return outcome.stdout.strip()

    def _guard_android_start(self, hostname):
        """Prove official StartRemoteServer will take its no-install branch.

        v1.46 android.cpp:1123 checks ABI/package count and exact version code +
        build hash before deciding whether to uninstall/install server APKs.
        This guard is intentionally stricter: every installed server must match.
        """
        if not hostname.startswith("adb://"):
            return
        if rd.GetVersionString() != "1.46":
            raise RuntimeError("REMOTE_START_REQUIRES_MANUAL: no-install startup preflight is audited for RenderDoc 1.46 only")
        serial = hostname[6:]
        if not re.match(r"^[A-Za-z0-9_.:-]+$", serial):
            raise ValueError("REMOTE_START_REQUIRES_MANUAL: unsupported Android device URL")
        query = lambda args: self._android_query(serial, args)
        # Match GetSupportedABIs(), which uses the primary ABI and includes
        # arm32 for every arm64 device, even an Android 12+ 64-bit-only device.
        primary = query(["getprop", "ro.product.cpu.abi"])
        expected = {"arm64-v8a": ["org.renderdoc.renderdoccmd.arm32", "org.renderdoc.renderdoccmd.arm64"],
                    "armeabi-v7a": ["org.renderdoc.renderdoccmd.arm32"]}.get(primary)
        if not expected:
            raise RuntimeError("REMOTE_START_REQUIRES_MANUAL: unverified Android ABI configuration")
        user = query(["am", "get-current-user"])
        if not user.isdigit():
            raise RuntimeError("REMOTE_START_REQUIRES_MANUAL: cannot identify the active Android user")
        packages = {line.partition(":")[2].strip() for line in query(
            ["pm", "list", "packages", "--user", user, "org.renderdoc.renderdoccmd"]).splitlines() if line.startswith("package:")}
        sdk = int(query(["getprop", "ro.build.version.sdk"]))
        normal = packages == set(expected)
        arm64_only = (sdk >= 31 and "org.renderdoc.renderdoccmd.arm64" in expected and
                      packages == {"org.renderdoc.renderdoccmd.arm64"})
        if not (normal or arm64_only):
            raise RuntimeError("REMOTE_INSTALL_REQUIRED: start refused; install matching RenderDoc server packages manually")
        if arm64_only and not normal:
            absent = query(["pm", "dump", "org.renderdoc.renderdoccmd.arm32"])
            if re.search(r"\bversion(?:Code|Name)=\S+", absent):
                raise RuntimeError("REMOTE_START_REQUIRES_MANUAL: unlisted arm32 package is still visible to the native version check")
        version = rd.GetVersionString().split(".")
        version_code = version[0] + version[1]
        commit = rd.GetCommitHash()
        for package in sorted(packages):
            dump = query(["pm", "dump", package])
            code = re.search(r"\bversionCode=(\S+)", dump)
            name = re.search(r"\bversionName=(\S+)", dump)
            if not code or not name or code.group(1) != version_code or name.group(1) != commit:
                raise RuntimeError("REMOTE_VERSION_MISMATCH: installed APK differs from host build; automatic upgrade is disabled")

    def _select_replay_context(self, host, hostname):
        """Use CaptureContext so the UI's context and ReplayManager agree.

        The public context API schedules its connection asynchronously. Keep
        the native stage pending until the selected host is actually connected;
        status/cancelability remain available from the persisted job snapshot.
        """
        config = self.ctx.Config()
        if not any(h.Hostname() == host.Hostname() for h in config.GetRemoteHosts()):
            config.AddRemoteHost(host)
        self.ctx.ConnectToRemoteServer(host)

        def ready():
            current = self.ctx.Replay().CurrentRemote()
            return (current.Hostname() == hostname and
                    (not hostname or current.IsConnected()))

        if ready():
            return
        from PySide2.QtCore import QEventLoop, QTimer
        loop, timer = QEventLoop(), QTimer()
        timer.timeout.connect(lambda: loop.quit() if ready() else None)
        timer.start(100)
        try:
            loop.exec_()
        finally:
            timer.stop()

    def get_capture_status(self, probe_replay=True):
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
        if self.session:
            result.update(self.session.describe())
        result["replay_probe"] = "not_loaded"
        result["active_job"] = self.jobs.active if self.jobs else None
        result["capabilities"] = {"async_jobs": True, "event_scoped_buffers": True,
                                  "shader_bundles": True, "texture_comparison": True}

        if not self.ctx.IsCaptureLoaded():
            return result

        result["loaded"] = True

        try:
            result["filename"] = self.ctx.GetCaptureFilename()
        except Exception:
            pass
        result["event_id"] = self.ctx.CurEvent()
        result["replay_context"] = self.get_replay_context()
        if not probe_replay or (self.jobs and self.jobs.busy()):
            result["replay_probe"] = "unavailable_busy" if self.jobs and self.jobs.busy() else "not_requested"
            return result
        current = result["replay_context"]["current"]
        if current and not current["connected"]:
            result.update(replay_healthy=False, replay_error="REMOTE_CONNECTION_LOST: remote context is disconnected",
                          replay_probe="not_executed_disconnected")
            return result
        if self.session:
            self.session.observe_replacements()
            result.update(self.session.describe())

        # Replay health probe: GetAPIProperties + GetFatalErrorStatus round-trip
        # proves the replay controller responds; GetFatalErrorStatus surfaces
        # driver/device removal that would otherwise only show up as empty data.
        def callback(controller):
            try:
                fatal = controller.GetFatalErrorStatus()
                if not fatal.OK():
                    result.update(replay_healthy=False, replay_error=str(fatal.Message()))
                    return
                props = controller.GetAPIProperties()
                result["api"] = str(props.pipelineType)
                result["remote_replay"] = bool(props.remoteReplay)
                result["capabilities"]["pixel_history"] = bool(getattr(props, "pixelHistory", False))
                result["replay_healthy"] = True
                fatal = controller.GetFatalErrorStatus()
                if not fatal.OK():
                    result.update(api=None, replay_healthy=False, replay_error=str(fatal.Message()))
            except Exception as exc:
                result["replay_healthy"] = False
                result["replay_error"] = str(exc)

        try:
            self._invoke(callback)
            result["replay_probe"] = "performed"
        except Exception as exc:
            result["replay_healthy"] = False
            result["replay_error"] = str(exc)
        return result

    def get_replay_context(self):
        def describe(host):
            return {"hostname": host.Hostname(), "connected": host.IsConnected(),
                    "server_running": host.IsServerRunning(), "busy": host.IsBusy(),
                    "version_mismatch": host.IsVersionMismatch()}
        replay = self.ctx.Replay()
        current = replay.CurrentRemote()
        hosts = list(self.ctx.Config().GetRemoteHosts())
        if current.Hostname() and not any(h.Hostname() == current.Hostname() for h in hosts):
            hosts.append(current)
        # Protocol enumeration can initialise/restart an ADB daemon. Do not
        # disturb a loaded replay just to refresh a host inventory.
        may_discover = not self.ctx.IsCaptureLoaded() and not (self.jobs and self.jobs.busy())
        if self._discovered is None and may_discover:
            discovered = []
            for protocol in rd.GetSupportedDeviceProtocols() if hasattr(rd, "GetSupportedDeviceProtocols") else []:
                try:
                    device_api = rd.GetDeviceProtocolController(protocol)
                    for device in device_api.GetDevices():
                        discovered.append({"hostname": "%s://%s" % (protocol, device),
                                           "protocol": protocol, "source": "official_device_protocol"})
                except Exception as exc:
                    discovered.append({"protocol": protocol, "discovery_error": str(exc)})
            self._discovered = discovered
        return {"current": describe(current) if current.Hostname() else None,
                "hosts": [describe(h) for h in hosts],
                "discovered_hosts": self._discovered or [],
                "discovery_cached": self._discovered is not None,
                "discovery_deferred": self._discovered is None and not may_discover,
                "active_job": self.jobs.active if self.jobs else None,
                "source": "qrenderdoc.ReplayManager.CurrentRemote"}

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

    def open_capture(self, capture_path, file_location="local", replay_target="current",
                     remote_host=None, job_id=None):
        if file_location not in ("local", "remote") or replay_target not in ("current", "local", "remote"):
            raise ValueError("INVALID_REQUEST: invalid file_location/replay_target")
        if not isinstance(capture_path, str) or not capture_path.lower().endswith(".rdc"):
            raise ValueError("INVALID_REQUEST: an .rdc capture_path is required")
        if remote_host is not None and replay_target != "remote":
            raise ValueError("INVALID_REQUEST: remote_host requires replay_target=remote")
        if file_location == "remote" and replay_target == "local":
            raise ValueError("INVALID_REQUEST: remote file requires remote replay")
        if file_location == "local" and not os.path.isfile(capture_path):
            raise ValueError("CAPTURE_FILE_NOT_FOUND: %s" % capture_path)
        params = dict(capture_path=capture_path, file_location=file_location,
                      replay_target=replay_target, remote_host=remote_host)

        def steps(key):
            def load(_):
                import qrenderdoc as qrd
                replay = self.ctx.Replay()
                facts = self._capture_file_facts(capture_path) if file_location == "local" else None
                current = replay.CurrentRemote()
                hostname = (remote_host or current.Hostname()) if replay_target == "remote" else (
                    current.Hostname() if replay_target == "current" else "")
                if (replay_target == "remote" or file_location == "remote") and not hostname:
                    raise ValueError("REMOTE_HOST_REQUIRED: specify the remote replay host")
                host = None
                if hostname:
                    host = next((h for h in self.ctx.Config().GetRemoteHosts()
                                 if h.Hostname() == hostname), None) or qrd.RemoteHost(hostname)
                    self.jobs.update(key, phase="checking_remote")
                    if current.Hostname() != hostname or not current.IsConnected():
                        host.CheckStatus()
                        if host.IsVersionMismatch():
                            raise RuntimeError("REMOTE_VERSION_MISMATCH: %s" % host.VersionMismatchError())
                        if not host.IsServerRunning():
                            self.jobs.update(key, phase="starting_remote")
                            self._guard_android_start(hostname)
                            outcome = host.Launch()
                            if not outcome.OK():
                                raise RuntimeError("REMOTE_START_FAILED: %s" % outcome.Message())
                            # Launch does not make RemoteHost's cached status a
                            # proof of readiness. Refresh it before handing the
                            # host to ReplayManager or transferring capture data.
                            self.jobs.update(key, phase="confirming_remote_started")
                            host.CheckStatus()
                            if host.IsVersionMismatch():
                                raise RuntimeError("REMOTE_VERSION_MISMATCH: %s" % host.VersionMismatchError())
                            if not host.IsServerRunning():
                                raise RuntimeError("REMOTE_START_FAILED: official launch returned but server is not ready")
                        # Validate the connection/path without replacing the current replay.
                        # RemoteHost.Connect has an out-pointer in the real SWIG
                        # binding. The public rd function returns the supported tuple.
                        outcome, connection = rd.CreateRemoteServerConnection(hostname)
                        if not outcome.OK():
                            raise RuntimeError("REMOTE_CONNECT_FAILED: %s" % outcome.Message())
                        try:
                            if file_location == "remote":
                                self.jobs.update(key, phase="preflight_remote_file")
                                facts = self._remote_file_facts(capture_path,
                                    lambda source, dest: connection.CopyCaptureFromRemote(source, dest, None))
                        finally:
                            connection.ShutdownConnection()
                    elif file_location == "remote":
                        self.jobs.update(key, phase="preflight_remote_file")
                        facts = self._remote_file_facts(capture_path,
                            lambda source, dest: replay.CopyCaptureFromRemote(source, dest, self.ctx.GetMainWindow().Widget()))
                if self.ctx.IsCaptureLoaded():
                    self.ctx.CloseCapture()
                current = replay.CurrentRemote()
                if current.Hostname() != hostname or (hostname and not current.IsConnected()):
                    replay.DisconnectFromRemoteServer()
                    if host:
                        self.jobs.update(key, phase="connecting_remote")
                        self._select_replay_context(host, hostname)
                    else:
                        self._select_replay_context(qrd.RemoteHost("localhost"), "")
                actual_path = capture_path
                local = file_location == "local"
                if hostname and local:
                    self.jobs.update(key, phase="uploading_capture")
                    actual_path = replay.CopyCaptureToRemote(capture_path, self.ctx.GetMainWindow().Widget())
                    if not actual_path:
                        raise RuntimeError("REMOTE_UPLOAD_FAILED: no remote path returned")
                    self.jobs.update(key, phase="verifying_upload", uploaded_path=actual_path)
                    uploaded = self._remote_file_facts(actual_path,
                        lambda source, dest: replay.CopyCaptureFromRemote(source, dest, self.ctx.GetMainWindow().Widget()))
                    if uploaded != facts:
                        raise RuntimeError("REMOTE_UPLOAD_FAILED: capture identity differs after transfer")
                    local = False
                if hostname and (replay.CurrentRemote().Hostname() != hostname or
                                 not replay.CurrentRemote().IsConnected() or not replay.GetRemoteSupport()):
                    raise RuntimeError("REMOTE_CONNECTION_LOST: refusing to load remote path in local replay")
                self.jobs.update(key, phase="loading_capture", native_operation="LoadCapture")
                self.ctx.LoadCapture(actual_path, rd.ReplayOptions(), capture_path, False, local)
                if not self.ctx.IsCaptureLoaded():
                    raise RuntimeError("CAPTURE_LOAD_FAILED: capture did not load")
                health = {}
                def probe(controller):
                    props = controller.GetAPIProperties()
                    fatal = controller.GetFatalErrorStatus()
                    health.update(api=str(props.pipelineType), remote_replay=bool(props.remoteReplay),
                                  replay_healthy=bool(fatal.OK()), replay_error=None if fatal.OK() else str(fatal.Message()))
                self._invoke(probe)
                if not health["replay_healthy"] or health["remote_replay"] != bool(hostname):
                    raise RuntimeError("CAPTURE_VALIDATION_FAILED: %s" % health)
                if facts and health["api"].split(".")[-1] != facts["capture_api"]:
                    raise RuntimeError("CAPTURE_VALIDATION_FAILED: replay API differs from capture metadata")
                actual_host = replay.CurrentRemote().Hostname()
                if actual_host != hostname:
                    raise RuntimeError("CAPTURE_VALIDATION_FAILED: wrong replay host")
                result = dict(health, capture_path=capture_path, loaded_path=actual_path,
                              file_location=file_location, remote_host=actual_host)
                if self.ctx.GetCaptureFilename() != capture_path:
                    raise RuntimeError("CAPTURE_VALIDATION_FAILED: wrong capture identity")
                result.update(facts or {})
                result.update(self.session.describe())
                return {"result": result}
            yield ("ui_native", "preflight_capture", load)
        return self.jobs.submit("open_capture", params, steps, job_id, capture_bound=False)
