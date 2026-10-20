from ._CaptureContext import CaptureContext
from typing import Any, Dict


# Synthetic function
def ExtensionCallback(context: CaptureContext, data: Dict[str, Any]):
    """
    Not a member function - the signature for any ``ExtensionCallback`` callbacks.
    
    Callback for extensions to register entry points with, used in many situations depending on how it
    was registered.
    
    :param CaptureContext context: The current capture context.
    :param Dict[str, Any] data: Additional data for the call, as a dictionary with string keys.
      Context-dependent based on what generated the callback
    """
    pass

