from ._ResourceId import ResourceId
from ._ShaderReflection import ShaderReflection
from ._ShaderStage import ShaderStage

from typing import overload

class D3D12Shader():
    # Original docstring
    """
    Describes a D3D12 shader stage.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D12Shader.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D12Shader'):
        """
        Construct a new D3D12Shader with a deep copy of the input.
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
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the shader object itself.
        
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
    
