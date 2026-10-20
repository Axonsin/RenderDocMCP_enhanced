from ._ShaderBuiltin import ShaderBuiltin
from ._VarType import VarType

from typing import overload

class SigParameter():
    # Original docstring
    """
    The information describing an input or output signature element describing the interface
    between shader stages.
    
    .. data:: NoIndex
    
      Value for an index that means it is invalid or not applicable for this parameter.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised SigParameter.
        """
        pass
    
    @overload
    def __init__(self, other: 'SigParameter'):
        """
        Construct a new SigParameter with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    NoIndex = 4294967295
    """
    Value for an index that means it is invalid or not applicable for this parameter.
    """
    
    @property
    def semanticIndex(self) -> int:
        """
        The semantic index of this variable - see :data:`semanticName`.
        
        :type: int
        """
        pass
    
    @semanticIndex.setter
    def semanticIndex(self, value: int):
        pass
    
    @property
    def needSemanticIndex(self) -> bool:
        """
        A convenience flag - ``True`` if the semantic name is unique and no index is needed.
        
        :type: bool
        """
        pass
    
    @needSemanticIndex.setter
    def needSemanticIndex(self, value: bool):
        pass
    
    @property
    def channelUsedMask(self) -> int:
        """
        A bitmask indicating which components in the shader register are actually used by the
        shader itself, for APIs that pack signatures together.
        
        :type: int
        """
        pass
    
    @channelUsedMask.setter
    def channelUsedMask(self, value: int):
        pass
    
    @property
    def compCount(self) -> int:
        """
        The number of components used to store this element. See :data:`varType`.
        
        :type: int
        """
        pass
    
    @compCount.setter
    def compCount(self, value: int):
        pass
    
    @property
    def perPrimitiveRate(self) -> bool:
        """
        A flag indicating if this parameter is output at per-primitive rate rather than per-vertex.
        
        :type: bool
        """
        pass
    
    @perPrimitiveRate.setter
    def perPrimitiveRate(self, value: bool):
        pass
    
    @property
    def semanticName(self) -> str:
        """
        The semantic name of this variable, if the API uses semantic matching for bindings.
        
        :type: str
        """
        pass
    
    @semanticName.setter
    def semanticName(self, value: str):
        pass
    
    @property
    def stream(self) -> int:
        """
        Selects a stream for APIs that provide multiple output streams for the same named output.
        
        :type: int
        """
        pass
    
    @stream.setter
    def stream(self, value: int):
        pass
    
    @property
    def regChannelMask(self) -> int:
        """
        A bitmask indicating which components in the shader register are stored, for APIs that
        pack signatures together.
        
        :type: int
        """
        pass
    
    @regChannelMask.setter
    def regChannelMask(self, value: int):
        pass
    
    @property
    def varName(self) -> str:
        """
        The name of this variable - may not be present in the metadata for all APIs.
        
        :type: str
        """
        pass
    
    @varName.setter
    def varName(self, value: str):
        pass
    
    @property
    def systemValue(self) -> ShaderBuiltin:
        """
        The :class:`ShaderBuiltin` value that this element contains.
        
        :type: ShaderBuiltin
        """
        pass
    
    @systemValue.setter
    def systemValue(self, value: ShaderBuiltin):
        pass
    
    @property
    def regIndex(self) -> int:
        """
        The index of the shader register/binding used to store this signature element.
        
        This may be :data:`NoIndex` if the element is system-generated and not consumed by another shader
        stage. See :data:`systemValue`.
        
        :type: int
        """
        pass
    
    @regIndex.setter
    def regIndex(self, value: int):
        pass
    
    @property
    def semanticIdxName(self) -> str:
        """
        The combined semantic name and index.
        
        :type: str
        """
        pass
    
    @semanticIdxName.setter
    def semanticIdxName(self, value: str):
        pass
    
    @property
    def varType(self) -> VarType:
        """
        The :class:`variable type <VarType>` of data that this element stores.
        
        :type: VarType
        """
        pass
    
    @varType.setter
    def varType(self, value: VarType):
        pass
    
