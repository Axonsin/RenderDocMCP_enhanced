
from typing import overload

class ShaderConstant():
    # Original docstring
    """
    Contains the detail of a constant within a struct, such as a :class:`ConstantBlock`,
    with its type and relative location in memory.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderConstant.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderConstant'):
        """
        Construct a new ShaderConstant with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def defaultValue(self) -> int:
        """
        If this constant is no larger than a 64-bit constant, gives a default value for it.
        
        :type: int
        """
        pass
    
    @defaultValue.setter
    def defaultValue(self, value: int):
        pass
    
    @property
    def name(self) -> str:
        """
        The name of this constant
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def byteOffset(self) -> int:
        """
        The byte offset of this constant relative to the parent structure
        
        :type: int
        """
        pass
    
    @byteOffset.setter
    def byteOffset(self, value: int):
        pass
    
    @property
    def type(self) -> 'ShaderConstantType':
        """
        The type information for this constant.
        
        :type: ShaderConstantType
        """
        pass
    
    @type.setter
    def type(self, value: 'ShaderConstantType'):
        pass
    
    @property
    def bitFieldOffset(self) -> int:
        """
        If the variable is bitfield packed, the bit offset from :data:`byteOffset` above where
        this variable starts.
        
        If the variable is not a bitfield, this value will be 0. Only integer scalars will have bitfield
        packing.
        
        .. note::
           Although the offset specified in :data:`byteOffset` is in bytes, this bitfield offset may be
           larger than 0 depending on the surrounding values and their types and packing. However it is
           guaranteed that the offset and the size (from :data:`bitFieldSize`) will be contained within the
           normal bit size for the variable type. For example if the variable type is a 32-bit integer, the
           offsets may range from 0 to 31 and the sum of offset and size will be no more than 32. If the
           variable is an 8-bit integer, similarly the offset will be 0 to 7 and the sum will be no more
           than 8.
        
        :type: int
        """
        pass
    
    @bitFieldOffset.setter
    def bitFieldOffset(self, value: int):
        pass
    
    @property
    def bitFieldSize(self) -> int:
        """
        If the variable is bitfield packed, the number of bits this variable spans starting
        from :data:`bitFieldOffset` into memory.
        
        If the variable is not a bitfield, this value will be 0. Only integer scalars will have bitfield
        packing.
        
        :type: int
        """
        pass
    
    @bitFieldSize.setter
    def bitFieldSize(self, value: int):
        pass
    
from ._ShaderVariableFlags import ShaderVariableFlags
from ._VarType import VarType
from typing import List

from typing import overload

class ShaderConstantType():
    # Original docstring
    """
    Describes the type and members of a :class:`ShaderConstant`.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderConstantType.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderConstantType'):
        """
        Construct a new ShaderConstantType with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def RowMajor(self) -> bool:
        """
        Helper function for checking if :data:`flags` has
        :data:`ShaderVariableFlags.RowMajorMatrix` set. This is entirely equivalent to checking that flag
        manually, but since it is common this helper is provided.
        
        .. note::
          Vectors and scalars will be marked as row-major by convention for convenience.
        
        :return: If the storage is row-major order in memory
        :rtype: bool
        """
        pass
    
    
    def ColMajor(self) -> bool:
        """
        Helper function for checking if :data:`flags` *does not* have
        :data:`ShaderVariableFlags.RowMajorMatrix` set. This is entirely equivalent to checking that flag
        manually, but since it is common this helper is provided.
        
        .. note::
          Vectors and scalars will be marked as row-major by convention for convenience.
        
        :return: If the storage is column-major order in memory
        :rtype: bool
        """
        pass
    
    @property
    def baseType(self) -> VarType:
        """
        The base :class:`VarType` of this constant.
        
        :type: VarType
        """
        pass
    
    @baseType.setter
    def baseType(self, value: VarType):
        pass
    
    @property
    def name(self) -> str:
        """
        The name of the type of this constant, e.g. a ``struct`` name.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def members(self) -> List['ShaderConstant']:
        """
        Any members that this constant may contain.
        
        :type: List[ShaderConstant]
        """
        pass
    
    @members.setter
    def members(self, value: List['ShaderConstant']):
        pass
    
    @property
    def rows(self) -> int:
        """
        The number of rows in this matrix.
        
        :type: int
        """
        pass
    
    @rows.setter
    def rows(self, value: int):
        pass
    
    @property
    def elements(self) -> int:
        """
        The number of elements in the array, or 1 if it's not an array.
        
        :type: int
        """
        pass
    
    @elements.setter
    def elements(self, value: int):
        pass
    
    @property
    def arrayByteStride(self) -> int:
        """
        The number of bytes between the start of one element in the array and the next.
        
        :type: int
        """
        pass
    
    @arrayByteStride.setter
    def arrayByteStride(self, value: int):
        pass
    
    @property
    def matrixByteStride(self) -> int:
        """
        The number of bytes between the start of one column/row in a matrix and the next.
        
        :type: int
        """
        pass
    
    @matrixByteStride.setter
    def matrixByteStride(self, value: int):
        pass
    
    @property
    def flags(self) -> ShaderVariableFlags:
        """
        The flags controlling how this constant is interpreted and displayed.
        
        :type: ShaderVariableFlags
        """
        pass
    
    @flags.setter
    def flags(self, value: ShaderVariableFlags):
        pass
    
    @property
    def pointerTypeID(self) -> int:
        """
        The index in :data:`ShaderReflection.pointerTypes` of the pointee type.
        
        :type: int
        """
        pass
    
    @pointerTypeID.setter
    def pointerTypeID(self, value: int):
        pass
    
    @property
    def columns(self) -> int:
        """
        The number of columns in this matrix.
        
        :type: int
        """
        pass
    
    @columns.setter
    def columns(self, value: int):
        pass
    
