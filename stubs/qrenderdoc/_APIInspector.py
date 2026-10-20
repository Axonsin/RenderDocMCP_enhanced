from renderdoc import SDObject

# Dummy types
from . import QWidget

class APIInspector():
    # Original docstring
    """
    The API inspector window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetAPIInspector`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`APIInspector` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def Refresh(self):
        """
        Refresh the current API view - useful if callstacks are now available.
        """
        pass
    
    
    def RevealParameter(self, param: SDObject):
        """
        Expand the API view to reveal a given parameter and select it.
        
        :param renderdoc.SDObject param: The parameter to reveal and select.
        """
        pass
    
