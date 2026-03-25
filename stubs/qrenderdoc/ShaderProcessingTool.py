# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderToolOutput import ShaderToolOutput

from renderdoc.ShaderReflection import ShaderReflection

from renderdoc.ShaderStage import ShaderStage

class ShaderProcessingTool(): # skipped bases: <class 'SwigPyObject'>
    """
    Describes an external program that can be used to process shaders, typically either
    compiling from a high-level language to a binary format, or decompiling from the binary format to
    a high-level language or textual representation.
    
    Commonly used with SPIR-V.
    """
    def CompileShader(self, window: QWidget, source: str, entryPoint: str, stage: ShaderStage, spirvVer: str, args: str) -> ShaderToolOutput: # real signature unknown; restored from __doc__
        """
        CompileShader(window, source, entryPoint, stage, spirvVer, args)
        
        Runs this program to disassemble a given shader source.
        
        :param QWidget window: A handle to the window to use when showing a progress bar or error messages.
        :param str source: The source code, preprocessed into a single file.
        :param str entryPoint: The name of the entry point in the shader to compile.
        :param renderdoc.ShaderStage stage: The pipeline stage that this shader represents.
        :param str spirvVer: The version of SPIR-V in use for this shader, or an empty string for defaults.
          The current version can be obtained from reflection data via the ``@spirver`` compile flag.
        :param str args: arguments to pass to the tool. The default arguments can be obtained using
          :meth:`DefaultArguments` which can then be customised as desired. Passing an empty string uses the
          default arguments.
        :return: The result of running the tool.
        :rtype: ShaderToolOutput
        """
        pass

    def DefaultArguments(self) -> str: # real signature unknown; restored from __doc__
        """
        DefaultArguments()
        
        Return the default arguments used when invoking this tool
        
        :return: The arguments specified for this tool.
        :rtype: str
        """
        pass

    def DisassembleShader(self, window: QWidget, shader: ShaderReflection, args: str) -> ShaderToolOutput: # real signature unknown; restored from __doc__
        """
        DisassembleShader(window, shader, args)
        
        Runs this program to disassemble a given shader reflection.
        
        :param QWidget window: A handle to the window to use when showing a progress bar or error messages.
        :param renderdoc.ShaderReflection shader: The shader to disassemble.
        :param str args: arguments to pass to the tool. The default arguments can be obtained using
          :meth:`DefaultArguments` which can then be customised as desired. Passing an empty string uses the
          default arguments.
        :return: The result of running the tool.
        :rtype: ShaderToolOutput
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

    @property
    def args(self) -> str:
        """
The command line argmuents to pass to the program.

:type: str

"""
        pass

    @args.setter
    def args(self, value: str):
        pass

    @property
    def executable(self) -> str:
        """
The path to the executable to run for this program.

:type: str

"""
        pass

    @executable.setter
    def executable(self, value: str):
        pass

    @property
    def input(self) -> ShaderEncoding:
        """
The input that this program expects.

:type: ShaderEncoding

"""
        pass

    @input.setter
    def input(self, value: ShaderEncoding):
        pass

    @property
    def name(self) -> str:
        """
The human-readable name of the program.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    @property
    def output(self) -> ShaderEncoding:
        """
The output that this program provides.

:type: ShaderEncoding

"""
        pass

    @output.setter
    def output(self, value: ShaderEncoding):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def tool(self) -> KnownShaderTool:
        """
The :class:`KnownShaderTool` identifying which known tool this program is.

:type: KnownShaderTool

"""
        pass

    @tool.setter
    def tool(self, value: KnownShaderTool):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50144500>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.ShaderProcessingTool' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.ShaderProcessingTool' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.ShaderProcessingTool' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.ShaderProcessingTool' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.ShaderProcessingTool' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.ShaderProcessingTool' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.ShaderProcessingTool' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.ShaderProcessingTool' objects>, 'DefaultArguments': <method 'DefaultArguments' of 'qrenderdoc.ShaderProcessingTool' objects>, 'DisassembleShader': <method 'DisassembleShader' of 'qrenderdoc.ShaderProcessingTool' objects>, 'CompileShader': <method 'CompileShader' of 'qrenderdoc.ShaderProcessingTool' objects>, 'tool': <attribute 'tool' of 'qrenderdoc.ShaderProcessingTool' objects>, 'name': <attribute 'name' of 'qrenderdoc.ShaderProcessingTool' objects>, 'input': <attribute 'input' of 'qrenderdoc.ShaderProcessingTool' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.ShaderProcessingTool' objects>, 'executable': <attribute 'executable' of 'qrenderdoc.ShaderProcessingTool' objects>, 'output': <attribute 'output' of 'qrenderdoc.ShaderProcessingTool' objects>, 'args': <attribute 'args' of 'qrenderdoc.ShaderProcessingTool' objects>, '__doc__': '\\nDescribes an external program that can be used to process shaders, typically either\\ncompiling from a high-level language to a binary format, or decompiling from the binary format to\\na high-level language or textual representation.\\n\\nCommonly used with SPIR-V.\\n\\n'})"


