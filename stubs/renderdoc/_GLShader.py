from ._ResourceId import ResourceId
from ._ShaderReflection import ShaderReflection
from ._ShaderStage import ShaderStage
from typing import List

from typing import overload

class GLShader():
    # Original docstring
    """
    Describes an OpenGL shader stage.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLShader.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLShader'):
        """
        Construct a new GLShader with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def subroutines(self) -> List[int]:
        """
        A list of integers with the subroutine values.
        
        :type: List[int]
        """
        pass
    
    @subroutines.setter
    def subroutines(self, value: List[int]):
        pass
    
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
    def shaderResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the shader object itself.
        
        :type: ResourceId
        """
        pass
    
    @shaderResourceId.setter
    def shaderResourceId(self, value: ResourceId):
        pass
    
    @property
    def programResourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the program bound to this stage.
        
        :type: ResourceId
        """
        pass
    
    @programResourceId.setter
    def programResourceId(self, value: ResourceId):
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
    
