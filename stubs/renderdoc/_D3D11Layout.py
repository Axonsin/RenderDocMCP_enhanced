from ._ResourceFormat import ResourceFormat

from typing import overload

class D3D11Layout():
    # Original docstring
    """
    Describes a single D3D11 input layout element for one vertex input.
    
    .. data:: TightlyPacked
    
      Value for :data:`byteOffset` that indicates this element is tightly packed.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised D3D11Layout.
        """
        pass
    
    @overload
    def __init__(self, other: 'D3D11Layout'):
        """
        Construct a new D3D11Layout with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    TightlyPacked = 4294967295
    """
    Value for :data:`byteOffset` that indicates this element is tightly packed.
    """
    
    @property
    def semanticIndex(self) -> int:
        """
        The semantic index for this input.
        
        :type: int
        """
        pass
    
    @semanticIndex.setter
    def semanticIndex(self, value: int):
        pass
    
    @property
    def semanticName(self) -> str:
        """
        The semantic name for this input.
        
        :type: str
        """
        pass
    
    @semanticName.setter
    def semanticName(self, value: str):
        pass
    
    @property
    def instanceDataStepRate(self) -> int:
        """
        If :data:`perInstance` is ``True`` then this is how many times each instance data is
        used before advancing to the next instance.
        
        E.g. if this value is two, then two instances will be drawn with the first instance data, then two
        with the next instance data.
        
        :type: int
        """
        pass
    
    @instanceDataStepRate.setter
    def instanceDataStepRate(self, value: int):
        pass
    
    @property
    def format(self) -> ResourceFormat:
        """
        The format describing how the input data is interpreted.
        
        :type: ResourceFormat
        """
        pass
    
    @format.setter
    def format(self, value: ResourceFormat):
        pass
    
    @property
    def inputSlot(self) -> int:
        """
        The vertex buffer input slot where the data is sourced from.
        
        :type: int
        """
        pass
    
    @inputSlot.setter
    def inputSlot(self, value: int):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset from the start of the vertex data in the vertex buffer from
        :data:`inputSlot`.
        
        If the value is :data:`TightlyPacked` then the element is packed tightly after the previous element, or 0
        if this is the first element.
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def perInstance(self) -> bool:
        """
        ``True`` if the vertex data is instance-rate.
        
        :type: bool
        """
        pass
    
    @perInstance.setter
    def perInstance(self, value: bool):
        pass
    
