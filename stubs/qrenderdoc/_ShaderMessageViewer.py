from renderdoc import ShaderMessage
from typing import List

# Dummy types
from . import QWidget

class ShaderMessageViewer():
    # Original docstring
    """
    A shader message list window.
    
    This window is retrieved by calling :meth:`CaptureContext.ViewShaderMessages`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`ShaderMessageViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def GetEvent(self) -> int:
        """
        Return the EID that this viewer is displaying messages from.
        
        :return: The EID.
        :rtype: int
        """
        pass
    
    
    def GetShaderMessages(self) -> List[ShaderMessage]:
        """
        Return the shader messages displayed in this viewer.
        
        :return: The shader messages.
        :rtype: List[renderdoc.ShaderMessage]
        """
        pass
    
    
    def IsOutOfDate(self) -> bool:
        """
        Returns whether or not this viewer is out of date - if the shaders have been edited
        since the messages were fetched.
        
        :return: ``True`` if the viewer is out of date.
        :rtype: bool
        """
        pass
    
