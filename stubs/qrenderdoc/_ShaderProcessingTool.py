from ._ShaderToolOutput import ShaderToolOutput
from renderdoc import KnownShaderTool, ShaderEncoding, ShaderReflection, ShaderStage

# Dummy types
from . import QWidget

from typing import overload

class ShaderProcessingTool():
    # Original docstring
    """
    Describes an external program that can be used to process shaders, typically either
    compiling from a high-level language to a binary format, or decompiling from the binary format to
    a high-level language or textual representation.
    
    Commonly used with SPIR-V.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderProcessingTool.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderProcessingTool'):
        """
        Construct a new ShaderProcessingTool with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def DefaultArguments(self) -> str:
        """
        Return the default arguments used when invoking this tool
        
        :return: The arguments specified for this tool.
        :rtype: str
        """
        pass
    
    
    def DisassembleShader(self, window: QWidget, shader: ShaderReflection, args: str) -> ShaderToolOutput:
        """
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
    
    
    def CompileShader(self, window: QWidget, source: str, entryPoint: str, stage: ShaderStage, spirvVer: str, args: str) -> ShaderToolOutput:
        """
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
    
    @property
    def tool(self) -> KnownShaderTool:
        """
        The :class:`~renderdoc.KnownShaderTool` identifying which known tool this program is.
        
        :type: renderdoc.KnownShaderTool
        """
        pass
    
    @tool.setter
    def tool(self, value: KnownShaderTool):
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
    def input(self) -> ShaderEncoding:
        """
        The input that this program expects.
        
        :type: renderdoc.ShaderEncoding
        """
        pass
    
    @input.setter
    def input(self, value: ShaderEncoding):
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
    def output(self) -> ShaderEncoding:
        """
        The output that this program provides.
        
        :type: renderdoc.ShaderEncoding
        """
        pass
    
    @output.setter
    def output(self, value: ShaderEncoding):
        pass
    
    @property
    def args(self) -> str:
        """
        The command line arguments to pass to the program.
        
        :type: str
        """
        pass
    
    @args.setter
    def args(self, value: str):
        pass
    
