from ._ResourceId import ResourceId
from ._ShaderReflection import ShaderReflection
from ._ShaderStage import ShaderStage
from typing import List

from typing import overload

class D3D11Shader():
    # Original docstring
    """
    Describes a D3D11 shader stage.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11Shader.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11Shader'):
        """
        Construct a new D3D11Shader with a deep copy of the input.
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
    def classInstances(self) -> List[str]:
        """
        The bound class instance names.
        
        :type: List[str]
        """
        pass
    
    @classInstances.setter
    def classInstances(self, value: List[str]):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the shader itself.
        
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
    
