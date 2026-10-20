from ._ConstantBlock import ConstantBlock
from ._ResourceId import ResourceId
from ._ShaderConstantType import ShaderConstantType
from ._ShaderDebugInfo import ShaderDebugInfo
from ._ShaderEncoding import ShaderEncoding
from ._ShaderResource import ShaderResource
from ._ShaderSampler import ShaderSampler
from ._ShaderStage import ShaderStage
from ._SigParameter import SigParameter
from ._Topology import Topology
from typing import List, Tuple

class ShaderReflection():
    # Original docstring
    """
    The reflection and metadata fully describing a shader.
    
    The information in this structure is API agnostic.
    """
    
    
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
    def dispatchThreadsDimension(self) -> Tuple[int, int, int]:
        """
        The 3D dimensions of a compute workgroup, for compute shaders.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @dispatchThreadsDimension.setter
    def dispatchThreadsDimension(self, value: Tuple[int, int, int]):
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
    def interfaces(self) -> List[str]:
        """
        The list of strings with the shader's interfaces. Largely an unused API feature.
        
        :type: List[str]
        """
        pass
    
    @interfaces.setter
    def interfaces(self, value: List[str]):
        pass
    
