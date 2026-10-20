from renderdoc import ResourceId, SDObject

# Dummy types
from . import QWidget

class ResourceInspector():
    # Original docstring
    """
    The Resource inspector window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetResourceInspector`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`ResourceInspector` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def Inspect(self, id: ResourceId):
        """
        Change the current resource being inspected.
        
        :param renderdoc.ResourceId id: The ID of the resource to inspect.
        """
        pass
    
    
    def CurrentResource(self) -> ResourceId:
        """
        Return which resource is currently being inspected.
        
        :return: The ID of the resource being inspected.
        :rtype: renderdoc.ResourceId
        """
        pass
    
    
    def RevealParameter(self, param: SDObject):
        """
        Expand the resource initialisation chunks to reveal and select a given parameter.
        
        :param renderdoc.SDObject param: The parameter to reveal and select.
        """
        pass
    
