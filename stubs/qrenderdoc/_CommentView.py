
# Dummy types
from . import QWidget

class CommentView():
    # Original docstring
    """
    The capture comments window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetCommentView`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`CommentView` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def SetComments(self, text: str):
        """
        Sets the current comments text.
        
        :param str text: The new comments text.
        """
        pass
    
    
    def GetComments(self) -> str:
        """
        Gets the current comments text.
        
        :return: The current comments text.
        :rtype: str
        """
        pass
    
