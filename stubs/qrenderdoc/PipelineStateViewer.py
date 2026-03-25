# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .PipelineStage import PipelineStage

from renderdoc.ShaderReflection import ShaderReflection

class PipelineStateViewer(): # skipped bases: <class 'SwigPyObject'>
    """
    The pipeline state viewer window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetPipelineViewer`.
    """
    def SaveShaderFile(self, shader: ShaderReflection) -> bool: # real signature unknown; restored from __doc__
        """
        SaveShaderFile(shader)
        
        Prompt the user to save the binary form of the given shader to disk.
        
        :param renderdoc.ShaderReflection shader: The shader reflection data to save.
        :return: ``True`` if the shader was saved successfully, ``False`` if an error occurred.
        :rtype: bool
        """
        pass

    def SelectPipelineStage(self, stage: PipelineStage): # real signature unknown; restored from __doc__
        """
        SelectPipelineStage(stage)
        
        Select a given pipeline stage in the viewer.
        
        :param PipelineStage stage: The stage to select.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`PipelineStateViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50137670>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.PipelineStateViewer' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.PipelineStateViewer' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.PipelineStateViewer' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.PipelineStateViewer' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.PipelineStateViewer' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.PipelineStateViewer' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.PipelineStateViewer' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.PipelineStateViewer' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.PipelineStateViewer' objects>, 'SaveShaderFile': <method 'SaveShaderFile' of 'qrenderdoc.PipelineStateViewer' objects>, 'SelectPipelineStage': <method 'SelectPipelineStage' of 'qrenderdoc.PipelineStateViewer' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.PipelineStateViewer' objects>, '__doc__': '\\nThe pipeline state viewer window.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetPipelineViewer`.\\n\\n'})"


