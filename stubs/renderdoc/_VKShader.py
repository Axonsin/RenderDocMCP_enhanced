from ._ResourceId import ResourceId
from ._ShaderReflection import ShaderReflection
from ._ShaderStage import ShaderStage
from typing import List

from typing import overload

class VKShader():
    # Original docstring
    """
    Describes a Vulkan shader stage.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKShader.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKShader'):
        """
        Construct a new VKShader with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def reflection(self) -> ShaderReflection:
        """
        The reflection data for this shader.
        
        :type: ShaderReflection
        """
        pass
    
    @reflection.setter
    def reflection(self, value: ShaderReflection):
        pass
    
    @property
    def shaderObject(self) -> bool:
        """
        Whether the shader is a shader object or shader module.
        
        :type: bool
        """
        pass
    
    @shaderObject.setter
    def shaderObject(self, value: bool):
        pass
    
    @property
    def requiredSubgroupSize(self) -> int:
        """
        The required subgroup size specified for this shader at pipeline creation time.
        
        :type: int
        """
        pass
    
    @requiredSubgroupSize.setter
    def requiredSubgroupSize(self, value: int):
        pass
    
    @property
    def specializationData(self) -> bytes:
        """
        The provided specialization constant data. Shader constants store the byte offset into
        this buffer as their byteOffset. This data includes the applied specialization constants over the
        top of the default values, so it is safe to read any constant from here and get the correct current
        value.
        
        :type: bytes
        """
        pass
    
    @specializationData.setter
    def specializationData(self, value: bytes):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the shader module object.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def stage(self) -> ShaderStage:
        """
        A :class:`ShaderStage` identifying which stage this shader is bound to.
        
        :type: ShaderStage
        """
        pass
    
    @stage.setter
    def stage(self, value: ShaderStage):
        pass
    
    @property
    def entryPoint(self) -> str:
        """
        The name of the entry point in the shader module that is used.
        
        :type: str
        """
        pass
    
    @entryPoint.setter
    def entryPoint(self, value: str):
        pass
    
    @property
    def pushConstantRangeByteOffset(self) -> int:
        """
        The byte offset into the push constant data that is visible to this shader.
        
        :type: int
        """
        pass
    
    @pushConstantRangeByteOffset.setter
    def pushConstantRangeByteOffset(self, value: int):
        pass
    
    @property
    def pushConstantRangeByteSize(self) -> int:
        """
        The number of bytes in the push constant data that is visible to this shader.
        
        :type: int
        """
        pass
    
    @pushConstantRangeByteSize.setter
    def pushConstantRangeByteSize(self, value: int):
        pass
    
    @property
    def specializationIds(self) -> List[int]:
        """
        The specialization constant ID for each entry in the specialization constant block of
        reflection info. This corresponds to the ``constantID`` in ``VkSpecializationMapEntry``, while the offset
        and size into ``specializationData`` can be obtained from the reflection info.
        
        :type: List[int]
        """
        pass
    
    @specializationIds.setter
    def specializationIds(self, value: List[int]):
        pass
    
