# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ConstantBlock import ConstantBlock
from .ShaderDebugInfo import ShaderDebugInfo
from .ShaderEncoding import ShaderEncoding
from .SigParameter import SigParameter
from .Topology import Topology
from .ShaderConstantType import ShaderConstantType
from .ShaderResource import ShaderResource
from .ResourceId import ResourceId
from .ShaderSampler import ShaderSampler
from .ShaderStage import ShaderStage

class ShaderReflection(): # skipped bases: <class 'SwigPyObject'>
    """
    The reflection and metadata fully describing a shader.
    
    The information in this structure is API agnostic.
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
    def constantBlocks(self) -> List[ConstantBlock]:
        """
The constant block bindings.

:type: List[ConstantBlock]

"""
        pass

    @constantBlocks.setter
    def constantBlocks(self, value: List[ConstantBlock]):
        pass

    @property
    def debugInfo(self) -> ShaderDebugInfo:
        """
The embedded debugging information.

:type: ShaderDebugInfo

"""
        pass

    @debugInfo.setter
    def debugInfo(self, value: ShaderDebugInfo):
        pass

    @property
    def dispatchThreadsDimension(self) -> Tuple[int,int,int]:
        """
The 3D dimensions of a compute workgroup, for compute shaders.

:type: Tuple[int,int,int]

"""
        pass

    @dispatchThreadsDimension.setter
    def dispatchThreadsDimension(self, value: Tuple[int,int,int]):
        pass

    @property
    def encoding(self) -> ShaderEncoding:
        """
The :class:`ShaderEncoding` of this shader. See :data:`rawBytes`.

:type: ShaderEncoding

"""
        pass

    @encoding.setter
    def encoding(self, value: ShaderEncoding):
        pass

    @property
    def entryPoint(self) -> str:
        """
The entry point in the shader for this reflection, if multiple entry points exist.

:type: str

"""
        pass

    @entryPoint.setter
    def entryPoint(self, value: str):
        pass

    @property
    def inputSignature(self) -> List[SigParameter]:
        """
The input signature.

:type: List[SigParameter]

"""
        pass

    @inputSignature.setter
    def inputSignature(self, value: List[SigParameter]):
        pass

    @property
    def interfaces(self) -> List[str]:
        """
The list of strings with the shader's interfaces. Largely an unused API feature.

:type: List[str]

"""
        pass

    @interfaces.setter
    def interfaces(self, value: List[str]):
        pass

    @property
    def outputSignature(self) -> List[SigParameter]:
        """
The output signature.

:type: List[SigParameter]

"""
        pass

    @outputSignature.setter
    def outputSignature(self, value: List[SigParameter]):
        pass

    @property
    def outputTopology(self) -> Topology:
        """
The output topology for geometry, tessellation and mesh shaders.

:type: Topology

"""
        pass

    @outputTopology.setter
    def outputTopology(self, value: Topology):
        pass

    @property
    def pointerTypes(self) -> List[ShaderConstantType]:
        """
The list of pointer types referred to in this shader.

:type: List[ShaderConstantType]

"""
        pass

    @pointerTypes.setter
    def pointerTypes(self, value: List[ShaderConstantType]):
        pass

    @property
    def rawBytes(self) -> bytes:
        """
A raw ``bytes`` dump of the original shader, encoded in the form denoted by
:data:`encoding`.

:type: bytes

"""
        pass

    @rawBytes.setter
    def rawBytes(self, value: bytes):
        pass

    @property
    def rayAttributes(self) -> ConstantBlock:
        """
The block layout of the ray attributes structure.

Only relevant for intersection shaders and closest/any hit shaders, this gives
the attributes structure produced by a custom intersection shader which is available by hit shaders,
or else the built-in structure if no intersection shader was used and a triangle intersection is
reported.

:type: ConstantBlock

"""
        pass

    @rayAttributes.setter
    def rayAttributes(self, value: ConstantBlock):
        pass

    @property
    def rayPayload(self) -> ConstantBlock:
        """
The block layout of the ray payload.

Only relevant for raytracing shaders, this gives the payload accessible for read and write by ray
evaluation during the processing of the ray

:type: ConstantBlock

"""
        pass

    @rayPayload.setter
    def rayPayload(self, value: ConstantBlock):
        pass

    @property
    def readOnlyResources(self) -> List[ShaderResource]:
        """
The read-only resource bindings.

:type: List[ShaderResource]

"""
        pass

    @readOnlyResources.setter
    def readOnlyResources(self, value: List[ShaderResource]):
        pass

    @property
    def readWriteResources(self) -> List[ShaderResource]:
        """
The read-write resource bindings.

:type: List[ShaderResource]

"""
        pass

    @readWriteResources.setter
    def readWriteResources(self, value: List[ShaderResource]):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of this shader.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    @property
    def samplers(self) -> List[ShaderSampler]:
        """
The sampler bindings.

:type: List[ShaderSampler]

"""
        pass

    @samplers.setter
    def samplers(self, value: List[ShaderSampler]):
        pass

    @property
    def stage(self) -> ShaderStage:
        """
The :class:`ShaderStage` that this shader corresponds to, if multiple entry points exist.

:type: ShaderStage

"""
        pass

    @stage.setter
    def stage(self, value: ShaderStage):
        pass

    @property
    def taskPayload(self) -> ConstantBlock:
        """
The block layout of the task-mesh communication payload.

Only relevant for task or mesh shaders, this gives the output payload (for task shaders) or the
input payload (for mesh shaders)

:type: ConstantBlock

"""
        pass

    @taskPayload.setter
    def taskPayload(self, value: ConstantBlock):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552242F0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderReflection' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderReflection' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderReflection' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderReflection' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderReflection' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderReflection' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderReflection' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderReflection' objects>, 'rawBytes': <attribute 'rawBytes' of 'renderdoc.ShaderReflection' objects>, 'dispatchThreadsDimension': <attribute 'dispatchThreadsDimension' of 'renderdoc.ShaderReflection' objects>, 'constantBlocks': <attribute 'constantBlocks' of 'renderdoc.ShaderReflection' objects>, 'rayAttributes': <attribute 'rayAttributes' of 'renderdoc.ShaderReflection' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.ShaderReflection' objects>, 'debugInfo': <attribute 'debugInfo' of 'renderdoc.ShaderReflection' objects>, 'samplers': <attribute 'samplers' of 'renderdoc.ShaderReflection' objects>, 'stage': <attribute 'stage' of 'renderdoc.ShaderReflection' objects>, 'entryPoint': <attribute 'entryPoint' of 'renderdoc.ShaderReflection' objects>, 'encoding': <attribute 'encoding' of 'renderdoc.ShaderReflection' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderReflection' objects>, 'inputSignature': <attribute 'inputSignature' of 'renderdoc.ShaderReflection' objects>, 'outputSignature': <attribute 'outputSignature' of 'renderdoc.ShaderReflection' objects>, 'readOnlyResources': <attribute 'readOnlyResources' of 'renderdoc.ShaderReflection' objects>, 'readWriteResources': <attribute 'readWriteResources' of 'renderdoc.ShaderReflection' objects>, 'pointerTypes': <attribute 'pointerTypes' of 'renderdoc.ShaderReflection' objects>, 'taskPayload': <attribute 'taskPayload' of 'renderdoc.ShaderReflection' objects>, 'rayPayload': <attribute 'rayPayload' of 'renderdoc.ShaderReflection' objects>, 'outputTopology': <attribute 'outputTopology' of 'renderdoc.ShaderReflection' objects>, 'interfaces': <attribute 'interfaces' of 'renderdoc.ShaderReflection' objects>, '__doc__': '\\nThe reflection and metadata fully describing a shader.\\n\\nThe information in this structure is API agnostic.\\n\\n'})"


