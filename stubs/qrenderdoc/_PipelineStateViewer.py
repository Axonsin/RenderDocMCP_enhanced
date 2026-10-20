from ._PipelineStage import PipelineStage
from renderdoc import ShaderReflection

# Dummy types
from . import QWidget

class PipelineStateViewer():
    # Original docstring
    """
    The pipeline state viewer window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetPipelineViewer`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`PipelineStateViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def SaveShaderFile(self, shader: ShaderReflection) -> bool:
        """
        Prompt the user to save the binary form of the given shader to disk.
        
        :param renderdoc.ShaderReflection shader: The shader reflection data to save.
        :return: ``True`` if the shader was saved successfully, ``False`` if an error occurred.
        :rtype: bool
        """
        pass
    
    
    def SelectPipelineStage(self, stage: PipelineStage):
        """
        Select a given pipeline stage in the viewer.
        
        :param PipelineStage stage: The stage to select.
        """
        pass
    
