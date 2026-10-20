from ._KnownShaderTool import KnownShaderTool
from ._LineColumnInfo import LineColumnInfo
from ._ShaderCompileFlags import ShaderCompileFlags
from ._ShaderEncoding import ShaderEncoding
from ._ShaderSourceFile import ShaderSourceFile
from typing import List

from typing import overload

class ShaderDebugInfo():
    # Original docstring
    """
    Contains the information about a shader contained within API-specific debugging
    information attached to the shader.
    
    Primarily this means the embedded original source files.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderDebugInfo.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderDebugInfo'):
        """
        Construct a new ShaderDebugInfo with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def sourceDebugInformation(self) -> bool:
        """
        Indicates whether this shader has debug information to allow source-level debugging.
        
        :type: bool
        """
        pass
    
    @sourceDebugInformation.setter
    def sourceDebugInformation(self, value: bool):
        pass
    
    @property
    def entryLocation(self) -> LineColumnInfo:
        """
        The source location of the first executable line or the entry point.
        
        .. note::
        
          The information is not guaranteed to be available depending on the underlying shader format, so
          all of the elements are optional.
        
        :type: LineColumnInfo
        """
        pass
    
    @entryLocation.setter
    def entryLocation(self, value: LineColumnInfo):
        pass
    
    @property
    def editBaseFile(self) -> int:
        """
        The index of the file which should be used for re-editing this shader's entry point.
        
        This is an optional value, and if set to ``-1`` you should fall back to using the file specified
        in :data:`entryLocation`, and if no file is specified there then use the first file listed.
        
        :type: int
        """
        pass
    
    @editBaseFile.setter
    def editBaseFile(self, value: int):
        pass
    
    @property
    def encoding(self) -> ShaderEncoding:
        """
        The :class:`ShaderEncoding` of the source. See :data:`files`.
        
        :type: ShaderEncoding
        """
        pass
    
    @encoding.setter
    def encoding(self, value: ShaderEncoding):
        pass
    
    @property
    def entrySourceName(self) -> str:
        """
        The name of the entry point in the source code, not necessarily the same as the
        entry point name exported to the API.
        
        :type: str
        """
        pass
    
    @entrySourceName.setter
    def entrySourceName(self, value: str):
        pass
    
    @property
    def debuggable(self) -> bool:
        """
        Indicates whether this particular shader can be debugged. In some cases even if the
        API can debug shaders in general, specific shaders cannot be debugged because they use unsupported
        functionality
        
        :type: bool
        """
        pass
    
    @debuggable.setter
    def debuggable(self, value: bool):
        pass
    
    @property
    def compiler(self) -> KnownShaderTool:
        """
        The :class:`KnownShaderTool` of the compiling tool.
        
        :type: KnownShaderTool
        """
        pass
    
    @compiler.setter
    def compiler(self, value: KnownShaderTool):
        pass
    
    @property
    def debugInfoLoadingLog(self) -> str:
        """
        Contains a log of the debug shader loading process i.e. searching for shader PDB.
        
        :type: str
        """
        pass
    
    @debugInfoLoadingLog.setter
    def debugInfoLoadingLog(self, value: str):
        pass
    
    @property
    def debugStatus(self) -> str:
        """
        If :data:`debuggable` is false then this contains a simple explanation of why the
        shader is not supported for debugging
        
        :type: str
        """
        pass
    
    @debugStatus.setter
    def debugStatus(self, value: str):
        pass
    
    @property
    def compileFlags(self) -> ShaderCompileFlags:
        """
        The flags used to compile this shader.
        
        :type: ShaderCompileFlags
        """
        pass
    
    @compileFlags.setter
    def compileFlags(self, value: ShaderCompileFlags):
        pass
    
    @property
    def files(self) -> List[ShaderSourceFile]:
        """
        The shader files encoded in the form denoted by :data:`encoding`.
        
        The first entry in the list is always the file where the entry point is.
        
        :type: List[ShaderSourceFile]
        """
        pass
    
    @files.setter
    def files(self, value: List[ShaderSourceFile]):
        pass
    
