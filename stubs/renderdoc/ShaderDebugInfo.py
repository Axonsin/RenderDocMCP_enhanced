# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderCompileFlags import ShaderCompileFlags
from .KnownShaderTool import KnownShaderTool
from .ShaderEncoding import ShaderEncoding
from .LineColumnInfo import LineColumnInfo
from .ShaderSourceFile import ShaderSourceFile

class ShaderDebugInfo(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the information about a shader contained within API-specific debugging
    information attached to the shader.
    
    Primarily this means the embedded original source files.
    """
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552181E0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderDebugInfo' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderDebugInfo' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderDebugInfo' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderDebugInfo' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderDebugInfo' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderDebugInfo' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderDebugInfo' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderDebugInfo' objects>, 'sourceDebugInformation': <attribute 'sourceDebugInformation' of 'renderdoc.ShaderDebugInfo' objects>, 'entryLocation': <attribute 'entryLocation' of 'renderdoc.ShaderDebugInfo' objects>, 'editBaseFile': <attribute 'editBaseFile' of 'renderdoc.ShaderDebugInfo' objects>, 'encoding': <attribute 'encoding' of 'renderdoc.ShaderDebugInfo' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderDebugInfo' objects>, 'entrySourceName': <attribute 'entrySourceName' of 'renderdoc.ShaderDebugInfo' objects>, 'debuggable': <attribute 'debuggable' of 'renderdoc.ShaderDebugInfo' objects>, 'compiler': <attribute 'compiler' of 'renderdoc.ShaderDebugInfo' objects>, 'debugInfoLoadingLog': <attribute 'debugInfoLoadingLog' of 'renderdoc.ShaderDebugInfo' objects>, 'debugStatus': <attribute 'debugStatus' of 'renderdoc.ShaderDebugInfo' objects>, 'compileFlags': <attribute 'compileFlags' of 'renderdoc.ShaderDebugInfo' objects>, 'files': <attribute 'files' of 'renderdoc.ShaderDebugInfo' objects>, '__doc__': '\\nContains the information about a shader contained within API-specific debugging\\ninformation attached to the shader.\\n\\nPrimarily this means the embedded original source files.\\n\\n'})"


