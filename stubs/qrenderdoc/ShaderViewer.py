# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderViewer(): # skipped bases: <class 'SwigPyObject'>
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
    def AddWatch(self, expression: str): # real signature unknown; restored from __doc__
        """
        AddWatch(expression)
        
        Add an expression to the watch panel.
        
        :param str expression: The name of the expression to watch.
        """
        pass

    def CurrentStep(self) -> int: # real signature unknown; restored from __doc__
        """
        CurrentStep()
        
        Retrieves the current step in the debugging.
        
        :return: The current step.
        :rtype: int
        """
        pass

    def GetCurrentFileContents(self) -> List[Tuple[str,str]]: # real signature unknown; restored from __doc__
        """
        GetCurrentFileContents()
        
        Return the current text of source files within the viewer. Primarily useful for
        returning any edits applied when editing a shader.
        
        :return: The current file contents as a list of (filename, contents) pairs.
        :rtype: List[Tuple[str,str]]
        """
        pass

    def RunForward(self): # real signature unknown; restored from __doc__
        """
        RunForward()
        
        Runs execution forward to the next breakpoint, or the end of the trace.
        """
        pass

    def SetCurrentStep(self, step: int): # real signature unknown; restored from __doc__
        """
        SetCurrentStep(step)
        
        Sets the current step in the debugging.
        
        :param int step: The current step to jump to.
        """
        pass

    def ShowErrors(self, errors: str): # real signature unknown; restored from __doc__
        """
        ShowErrors(errors)
        
        Show a list of shader compilation errors or warnings.
        
        :param str errors: The string of errors or warnings to display.
        """
        pass

    def ToggleBreakpointOnDisassemblyLine(self, disassemblyLine: int): # real signature unknown; restored from __doc__
        """
        ToggleBreakpointOnDisassemblyLine(disassemblyLine)
        
        Toggles a breakpoint at a given disassembly line (starting from 1).
        
        :param int disassemblyLine: The line of the disassembly to toggle a breakpoint on.
        """
        pass

    def ToggleBreakpointOnInstruction(self, instruction: int=-1): # real signature unknown; restored from __doc__
        """
        ToggleBreakpointOnInstruction(instruction=-1)
        ToggleBreakpointOnInstruction()
        
        Toggles a breakpoint at a given instruction.
        
        :param int instruction: The instruction to toggle breakpoint at. If this is ``-1`` the nearest
          instruction after the current caret position is used.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`ShaderViewer` if PySide2 is available, or otherwise
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5013F970>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.ShaderViewer' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.ShaderViewer' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.ShaderViewer' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.ShaderViewer' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.ShaderViewer' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.ShaderViewer' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.ShaderViewer' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.ShaderViewer' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.ShaderViewer' objects>, 'CurrentStep': <method 'CurrentStep' of 'qrenderdoc.ShaderViewer' objects>, 'SetCurrentStep': <method 'SetCurrentStep' of 'qrenderdoc.ShaderViewer' objects>, 'ToggleBreakpointOnInstruction': <method 'ToggleBreakpointOnInstruction' of 'qrenderdoc.ShaderViewer' objects>, 'ToggleBreakpointOnDisassemblyLine': <method 'ToggleBreakpointOnDisassemblyLine' of 'qrenderdoc.ShaderViewer' objects>, 'RunForward': <method 'RunForward' of 'qrenderdoc.ShaderViewer' objects>, 'ShowErrors': <method 'ShowErrors' of 'qrenderdoc.ShaderViewer' objects>, 'AddWatch': <method 'AddWatch' of 'qrenderdoc.ShaderViewer' objects>, 'GetCurrentFileContents': <method 'GetCurrentFileContents' of 'qrenderdoc.ShaderViewer' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.ShaderViewer' objects>, '__doc__': '\\nA shader window used for viewing, editing, or debugging.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.ViewShader`,\\n:meth:`CaptureContext.EditShader`, or :meth:`CaptureContext.DebugShader`.\\n\\n.. function:: SaveCallback(context, viewer, encoding, flags, entry, compiled)\\n\\n  Not a member function - the signature for any ``SaveCallback`` callbacks.\\n\\n  Called whenever a shader viewer that was open for editing triggers a save/update.\\n\\n  :param CaptureContext context: The current capture context.\\n  :param ShaderViewer viewer: The open shader viewer.\\n  :param renderdoc.ResourceId id: The id of the shader being replaced.\\n  :param renderdoc.ShaderStage stage: The shader stage of the shader being replaced.\\n  :param renderdoc.ShaderEncoding encoding: The encoding of the files being passed.\\n  :param renderdoc.ShaderCompileFlags flags: The flags to use during compilation.\\n  :param str entryFunc: The name of the entry point.\\n  :param bytes source: The byte buffer containing the source - may just be text depending on the\\n    encoding.\\n\\n.. function:: RevertCallback(context)\\n\\n  Not a member function - the signature for any ``RevertCallback`` callbacks.\\n\\n  Called whenever a shader viewer that was open for editing is closed.\\n\\n  :param CaptureContext context: The current capture context.\\n  :param ShaderViewer viewer: The open shader viewer.\\n  :param renderdoc.ResourceId id: The id of the shader being replaced.\\n\\n'})"


