from ._PointerVal import PointerVal
from ._ResourceId import ResourceId
from ._ShaderBindIndex import ShaderBindIndex
from ._ShaderDirectAccess import ShaderDirectAccess
from ._ShaderValue import ShaderValue
from ._ShaderVariableFlags import ShaderVariableFlags
from ._VarType import VarType
from typing import List

from typing import overload

class ShaderVariable():
    # Original docstring
    """
    Holds a single named shader variable. It contains either a primitive type (up to a 4x4
    matrix of a :class:`basic type <VarType>`) or a list of members, which can either be struct or array
    members of this parent variable.
    
    Matrices are always stored row-major. If necessary they are transposed when retrieving from the raw
    data bytes when they are specified to be column-major in the API/shader metadata.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderVariable.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderVariable'):
        """
        Construct a new ShaderVariable with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, name: str, x: float, y: float, z: float, w: float):
        """
        Construct a new ShaderVariable using provided values.
        """
        pass
    
    @overload
    def __init__(self, name: str, x: int, y: int, z: int, w: int):
        """
        Construct a new ShaderVariable using provided values.
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
    
    
    def SetTypelessPointer(self, pointer: int):
        """
        Utility function for setting a pointer value with no type information.
        
        :param int pointer: The actual pointer value.
        """
        pass
    
    
    def SetTypedPointer(self, pointer: int, shader: ResourceId, pointerTypeID: int):
        """
        Utility function for setting a pointer value with type information.
        
        :param int pointer: The actual pointer value.
        :param ResourceId shader: The shader containing the type information.
        :param int pointerTypeID: The type's index in the shader's :data:`ShaderReflection.pointerTypes`
          list.
        """
        pass
    
    
    def GetPointer(self) -> PointerVal:
        """
        Utility function for getting a pointer value, with optional type information.
        
        .. note::
        
          The return value is undefined if this variable is not a pointer.
        
        :return: A :class:`PointerVal` with the pointer value.
        :rtype: PointerVal
        """
        pass
    
    
    def SetBindIndex(self, idx: ShaderBindIndex):
        """
        Utility function for setting a reference to a shader binding.
        
        The :class:`ShaderBindIndex` uniquely refers to a given shader binding in one of the shader interfaces
        (constant blocks, samplers, read-only and read-write resources) and if necessary the element within
        an arrayed binding.
        
        :param ShaderBindIndex idx: The index of the bind being referred to.
        """
        pass
    
    
    def GetBindIndex(self) -> ShaderBindIndex:
        """
        Utility function for getting a shader binding referenced by this variable.
        
        .. note::
        
          The return value is undefined if this variable is not a binding reference.
        
        :return: A :class:`ShaderBindIndex` with the binding referenced.
        :rtype: ShaderBindIndex
        """
        pass
    
    
    def SetDirectAccess(self, access: ShaderDirectAccess):
        """
        Utility function for setting a resource which is accessed directly from a shader without using bindings.
        
        The :class:`ShaderDirectAccess` uniquely refers to a resource descriptor.
        
        :param ShaderDirectAccess access: The resource descriptor being referenced.
        """
        pass
    
    
    def GetDirectAccess(self) -> ShaderDirectAccess:
        """
        Utility function for getting the resource which is accessed directly from a shader without using bindings.
        
        .. note::
        
          The return value is undefined if this variable is not a resource referenced directly by a shader.
        
        :return: A :class:`ShaderDirectAccess` containing the resource reference.
        :rtype: ShaderDirectAccess
        """
        pass
    
    
    def IsDirectAccess(self) -> bool:
        """
        Utility function to check if this variable stores a resource reference directly accessed by a shader.
        
        :return: If the variable represents a :class:`ShaderDirectAccess`.
        :rtype: bool
        """
        pass
    
    @property
    def value(self) -> ShaderValue:
        """
        The contents of this variable if it has no members.
        
        :type: ShaderValue
        """
        pass
    
    @value.setter
    def value(self, value: ShaderValue):
        pass
    
    @property
    def name(self) -> str:
        """
        The name of this variable.
        
        :type: str
        """
        pass
    
    @name.setter
    def name(self, value: str):
        pass
    
    @property
    def members(self) -> List['ShaderVariable']:
        """
        The members of this variable.
        
        :type: List[ShaderVariable]
        """
        pass
    
    @members.setter
    def members(self, value: List['ShaderVariable']):
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
    def type(self) -> VarType:
        """
        The :class:`basic type <VarType>` of this variable.
        
        :type: VarType
        """
        pass
    
    @type.setter
    def type(self, value: VarType):
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
    def columns(self) -> int:
        """
        The number of columns in this matrix.
        
        :type: int
        """
        pass
    
    @columns.setter
    def columns(self, value: int):
        pass
    
