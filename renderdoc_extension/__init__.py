"""
RenderDoc MCP Bridge Extension
Provides a file IPC server for external MCP server communication.
"""

import importlib
import json
import os

from . import socket_server
from . import request_handler
from . import renderdoc_facade

# Global state
_context = None
_server = None
_facade = None
_version = ""

_RELOAD_MODULES = [
    ".utils.parsers",
    ".utils.serializers",
    ".utils.helpers",
    ".utils",
    ".services.replay_guard",
    ".services.resource_catalog",
    ".services.texture_values",
    ".services.structured_data",
    ".services.replay_query",
    ".services.native_serialization",
    ".services.session_state",
    ".services.job_service",
    ".services.texture_export",
    ".services.capture_manager",
    ".services.action_service",
    ".services.search_service",
    ".services.resource_service",
    ".services.pipeline_snapshot",
    ".services.shader_variables",
    ".services.pipeline_queries",
    ".services.pipeline_service",
    ".services.mesh_service",
    ".services.shader_edit_service",
    ".services.analysis_service",
    ".services.constant_export",
    ".services.batch_service",
    ".services.investigation_service",
    ".services.script_service",
    ".services",
    ".renderdoc_facade",
    ".request_handler",
    ".socket_server",
]

# Try to import qrenderdoc for UI integration (only available in RenderDoc)
try:
    import qrenderdoc as qrd

    _has_qrenderdoc = True
except ImportError:
    _has_qrenderdoc = False


def register(version, ctx):
    """
    Called when extension is loaded.

    Args:
        version: RenderDoc version string (e.g., "1.20")
        ctx: CaptureContext handle
    """
    global _context, _server, _version, _facade
    import re
    numbers = re.match(r"(\d+)\.(\d+)", version)
    if not numbers or tuple(int(n) for n in numbers.groups()) < (1, 46):
        raise RuntimeError("RenderDoc MCP 2.0 requires RenderDoc 1.46 or newer")
    _version = version
    _context = ctx
    _reload_child_modules()

    # Create facade and handler
    facade = renderdoc_facade.RenderDocFacade(ctx, _runtime_info(version))
    _facade = facade
    handler = request_handler.RequestHandler(facade)

    # Start file IPC server
    _server = socket_server.MCPBridgeServer(handler=handler)
    _server.start()

    # Register menu item if UI is available
    if _has_qrenderdoc:
        try:
            ctx.Extensions().RegisterWindowMenu(
                qrd.WindowMenu.Tools, ["MCP Bridge", "Status"], _show_status
            )
        except Exception as e:
            print("[MCP Bridge] Could not register menu: %s" % str(e))

    print("[MCP Bridge] Extension loaded (RenderDoc %s)" % version)
    print("[MCP Bridge] File IPC server ready")


def _extension_version():
    """Read the extension version from the manifest next to this package."""
    try:
        manifest_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "extension.json"
        )
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
        return manifest.get("version")
    except Exception:
        return None


def _runtime_info(renderdoc_version):
    """Version/protocol info reported by get_capture_status and ping."""
    from .services.session_state import build_fingerprint
    return {
        "extension_version": _extension_version(),
        "api_contract_version": 3,
        "extension_build_hash": build_fingerprint(),
        "renderdoc_version": renderdoc_version,
        "ipc_version": socket_server.IPC_VERSION,
    }


def unregister():
    """Called when extension is unloaded"""
    global _server, _facade, _context
    if _server:
        _server.stop()
        _server = None
    if _facade:
        _facade.dispose()
        _facade = None
    _context = None
    print("[MCP Bridge] Extension unloaded")


def _show_status(ctx, data):
    """Show status dialog"""
    if _server and _server.is_running():
        ctx.Extensions().MessageDialog(
            "MCP Bridge file IPC is running", "MCP Bridge Status"
        )
    else:
        ctx.Extensions().ErrorDialog("MCP Bridge is not running", "MCP Bridge Status")


def _reload_child_modules():
    """Refresh package submodules when RenderDoc's Extension Manager reloads us."""
    global socket_server, request_handler, renderdoc_facade
    package = __name__
    for module_name in _RELOAD_MODULES:
        try:
            module = importlib.import_module(module_name, package)
            importlib.reload(module)
        except Exception as exc:
            print("[MCP Bridge] Could not reload %s: %s" % (module_name, str(exc)))

    from . import socket_server as reloaded_socket_server
    from . import request_handler as reloaded_request_handler
    from . import renderdoc_facade as reloaded_renderdoc_facade

    socket_server = reloaded_socket_server
    request_handler = reloaded_request_handler
    renderdoc_facade = reloaded_renderdoc_facade
