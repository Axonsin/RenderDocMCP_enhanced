from typing import List, Tuple

# Dummy types
from . import QWidget

class ShaderViewer():
    # Original docstring
    """
    A shader window used for viewing, editing, or debugging.
    
    This window is retrieved by calling :meth:`CaptureContext.ViewShader`,
    :meth:`CaptureContext.EditShader`, or :meth:`CaptureContext.DebugShader`.
    
    .. function:: SaveCallback(context, viewer, encoding, flags, entry, compiled)
    
      Not a member function - the signature for any ``SaveCallback`` callbacks.
    
      Called whenever a shader viewer that was open for editing triggers a save/update.
    
      :param CaptureContext context: The current capture context.
      :param ShaderViewer viewer: The open shader viewer.
      :param renderdoc.ResourceId id: The id of the shader being replaced.
      :param renderdoc.ShaderStage stage: The shader stage of the shader being replaced.
      :param renderdoc.ShaderEncoding encoding: The encoding of the files being passed.
      :param renderdoc.ShaderCompileFlags flags: The flags to use during compilation.
      :param str entryFunc: The name of the entry point.
      :param bytes source: The byte buffer containing the source - may just be text depending on the
        encoding.
    
    .. function:: RevertCallback(context)
    
      Not a member function - the signature for any ``RevertCallback`` callbacks.
    
      Called whenever a shader viewer that was open for editing is closed.
    
      :param CaptureContext context: The current capture context.
      :param ShaderViewer viewer: The open shader viewer.
      :param renderdoc.ResourceId id: The id of the shader being replaced.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`ShaderViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def CurrentStep(self) -> int:
        """
        Retrieves the current step in the debugging.
        
        :return: The current step.
        :rtype: int
        """
        pass
    
    
    def SetCurrentStep(self, step: int):
        """
        Sets the current step in the debugging.
        
        :param int step: The current step to jump to.
        """
        pass
    
    
    def ToggleBreakpointOnInstruction(self, instruction: int = -1):
        """
        Toggles a breakpoint at a given instruction.
        
        :param int instruction=-1: **Optional parameter**. The instruction to toggle breakpoint at.
          If this is ``-1`` the nearest instruction after the current caret position is used.
        """
        pass
    
    
    def ToggleBreakpointOnDisassemblyLine(self, disassemblyLine: int):
        """
        Toggles a breakpoint at a given disassembly line (starting from 1).
        
        :param int disassemblyLine: The line of the disassembly to toggle a breakpoint on.
        """
        pass
    
    
    def RunForward(self):
        """
        Runs execution forward to the next breakpoint, or the end of the trace.
        """
        pass
    
    
    def ShowErrors(self, errors: str):
        """
        Show a list of shader compilation errors or warnings.
        
        :param str errors: The string of errors or warnings to display.
        """
        pass
    
    
    def AddWatch(self, expression: str):
        """
        Add an expression to the watch panel.
        
        :param str expression: The name of the expression to watch.
        """
        pass
    
    
    def GetCurrentFileContents(self) -> List[Tuple[str, str]]:
        """
        Return the current text of source files within the viewer. Primarily useful for
        returning any edits applied when editing a shader.
        
        :return: The current file contents as a list of (filename, contents) pairs.
        :rtype: List[Tuple[str,str]]
        """
        pass
    
