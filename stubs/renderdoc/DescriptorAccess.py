# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId
from .ShaderStage import ShaderStage
from .DescriptorType import DescriptorType

class DescriptorAccess(): # skipped bases: <class 'SwigPyObject'>
    """
    The details of a single accessed descriptor as fetched by a shader and which descriptor
    in the descriptor store was fetched.
    
    This may be a somewhat conservative access, reported as possible but not actually executed on the
    GPU itself.
    
    .. data:: NoShaderBinding
    
      No shader binding corresponds to this descriptor access, it happened directly without going
      through any kind of binding.
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
    def arrayElement(self) -> int:
        """
For an arrayed resource declared in a shader, the array element used.

:type: int

"""
        pass

    @arrayElement.setter
    def arrayElement(self, value: int):
        pass

    @property
    def byteOffset(self) -> int:
        """
The offset in bytes to the descriptor in the descriptor store.

:type: int

"""
        pass

    @byteOffset.setter
    def byteOffset(self, value: int):
        pass

    @property
    def byteSize(self) -> int:
        """
The size in bytes of the descriptor.

:type: int

"""
        pass

    @byteSize.setter
    def byteSize(self, value: int):
        pass

    @property
    def descriptorStore(self) -> ResourceId:
        """
The backing storage of the descriptor.

:type: ResourceId

"""
        pass

    @descriptorStore.setter
    def descriptorStore(self, value: ResourceId):
        pass

    @property
    def index(self) -> int:
        """
The index within the shader's reflection list corresponding to :data:`type` of the
accessing resource.

If this value is set to :data:`NoShaderBinding` then the shader synthesised a direct access into
descriptor storage without passing through a declared binding.

:type: int

"""
        pass

    @index.setter
    def index(self, value: int):
        pass

    @property
    def stage(self) -> ShaderStage:
        """
The shader stage that this descriptor access came from.

:type: ShaderStage

"""
        pass

    @stage.setter
    def stage(self, value: ShaderStage):
        pass

    @property
    def staticallyUnused(self) -> bool:
        """
For informational purposes, some descriptors that are declared in the shader
interface but are provably unused may still be reported as descriptor accesses. This flag will be
set to ``True`` to indicate that the descriptor was definitely not used.

This flag only states that a descriptor is definitely unused on all paths. If set to ``False`` this
does not necessarily guarantee that the descriptor was accessed on the GPU during execution.

:type: bool

"""
        pass

    @staticallyUnused.setter
    def staticallyUnused(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> DescriptorType:
        """
The type of the descriptor being accessed.

:type: DescriptorType

"""
        pass

    @type.setter
    def type(self, value: DescriptorType):
        pass


    NoShaderBinding = 65535
    __dict__ = None # (!) real value is "mappingproxy({'NoShaderBinding': 65535, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551ECF90>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DescriptorAccess' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DescriptorAccess' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DescriptorAccess' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DescriptorAccess' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DescriptorAccess' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DescriptorAccess' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DescriptorAccess' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DescriptorAccess' objects>, 'stage': <attribute 'stage' of 'renderdoc.DescriptorAccess' objects>, 'descriptorStore': <attribute 'descriptorStore' of 'renderdoc.DescriptorAccess' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DescriptorAccess' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.DescriptorAccess' objects>, 'type': <attribute 'type' of 'renderdoc.DescriptorAccess' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.DescriptorAccess' objects>, 'index': <attribute 'index' of 'renderdoc.DescriptorAccess' objects>, 'staticallyUnused': <attribute 'staticallyUnused' of 'renderdoc.DescriptorAccess' objects>, 'arrayElement': <attribute 'arrayElement' of 'renderdoc.DescriptorAccess' objects>, '__doc__': '\\nThe details of a single accessed descriptor as fetched by a shader and which descriptor\\nin the descriptor store was fetched.\\n\\nThis may be a somewhat conservative access, reported as possible but not actually executed on the\\nGPU itself.\\n\\n.. data:: NoShaderBinding\\n\\n  No shader binding corresponds to this descriptor access, it happened directly without going\\n  through any kind of binding.\\n\\n'})"


