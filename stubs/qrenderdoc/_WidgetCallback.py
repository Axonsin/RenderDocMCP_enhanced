from ._CaptureContext import CaptureContext

# Dummy types
from . import QWidget


# Synthetic function
def WidgetCallback(context: CaptureContext, widget: QWidget, text: str):
    """
    Not a member function - the signature for any ``WidgetCallback`` callbacks.
    
    Callback for widgets can be registered at creation time, the text field is optional and may be
    blank depending on the event, but the context and widget are always valid.
    
    :param CaptureContext context: The current capture context.
    :param QWidget widget: The widget sending the callback.
    :param str text: Additional data for the call, such as the current or selected text.
    """
    pass

