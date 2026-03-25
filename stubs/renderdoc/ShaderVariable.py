# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderBindIndex import ShaderBindIndex
from .ShaderDirectAccess import ShaderDirectAccess
from .PointerVal import PointerVal
from .ResourceId import ResourceId
from .ShaderVariableFlags import ShaderVariableFlags
from .VarType import VarType
from .ShaderValue import ShaderValue

class ShaderVariable(): # skipped bases: <class 'SwigPyObject'>
    """
    Holds a single named shader variable. It contains either a primitive type (up to a 4x4
    matrix of a :class:`basic type <VarType>`) or a list of members, which can either be struct or array
    members of this parent variable.
    
    Matrices are always stored row-major. If necessary they are transposed when retrieving from the raw
    data bytes when they are specified to be column-major in the API/shader metadata.
    """
    def ColMajor(self) -> bool: # real signature unknown; restored from __doc__
        """
        ColMajor()
        
        Helper function for checking if :data:`flags` *does not* have
        :data:`ShaderVariableFlags.RowMajorMatrix` set. This is entirely equivalent to checking that flag
        manually, but since it is common this helper is provided.
        
        .. note::
          Vectors and scalars will be marked as row-major by convention for convenience.
        
        :return: If the storage is column-major order in memory
        :rtype: bool
        """
        pass

    def GetBindIndex(self) -> ShaderBindIndex: # real signature unknown; restored from __doc__
        """
        GetBindIndex()
        
        Utility function for getting a shader binding referenced by this variable.
        
        .. note::
        
          The return value is undefined if this variable is not a binding reference.
        
        :return: A :class:`ShaderBindIndex` with the binding referenced.
        :rtype: ShaderBindIndex
        """
        pass

    def GetDirectAccess(self) -> ShaderDirectAccess: # real signature unknown; restored from __doc__
        """
        GetDirectAccess()
        
        Utility function for getting the resource which is accessed directly from a shader without using bindings.
        
        .. note::
        
          The return value is undefined if this variable is not a resource referenced directly by a shader.
        
        :return: A :class:`ShaderDirectAccess` containing the resource reference.
        :rtype: ShaderDirectAccess
        """
        pass

    def GetPointer(self) -> PointerVal: # real signature unknown; restored from __doc__
        """
        GetPointer()
        
        Utility function for getting a pointer value, with optional type information.
        
        .. note::
        
          The return value is undefined if this variable is not a pointer.
        
        :return: A :class:`PointerVal` with the pointer value.
        :rtype: PointerVal
        """
        pass

    def IsDirectAccess(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsDirectAccess()
        
        Utility function to check if this variable stores a resource reference directly accessed by a shader.
        
        :return: If the variable represents a :class:`ShaderDirectAccess`.
        :rtype: bool
        """
        pass

    def RowMajor(self) -> bool: # real signature unknown; restored from __doc__
        """
        RowMajor()
        
        Helper function for checking if :data:`flags` has
        :data:`ShaderVariableFlags.RowMajorMatrix` set. This is entirely equivalent to checking that flag
        manually, but since it is common this helper is provided.
        
        .. note::
          Vectors and scalars will be marked as row-major by convention for convenience.
        
        :return: If the storage is row-major order in memory
        :rtype: bool
        """
        pass

    def SetBindIndex(self, idx: ShaderBindIndex): # real signature unknown; restored from __doc__
        """
        SetBindIndex(idx)
        
        Utility function for setting a reference to a shader binding.
        
        The :class:`ShaderBindIndex` uniquely refers to a given shader binding in one of the shader interfaces
        (constant blocks, samplers, read-only and read-write resources) and if necessary the element within
        an arrayed binding.
        
        :param ShaderBindIndex idx: The index of the bind being referred to.
        """
        pass

    def SetDirectAccess(self, access: ShaderDirectAccess): # real signature unknown; restored from __doc__
        """
        SetDirectAccess(access)
        
        Utility function for setting a resource which is accessed directly from a shader without using bindings.
        
        The :class:`ShaderDirectAccess` uniquely refers to a resource descriptor.
        
        :param ShaderDirectAccess access: The resource descriptor being referenced.
        """
        pass

    def SetTypedPointer(self, pointer: int, shader: ResourceId, pointerTypeID: int): # real signature unknown; restored from __doc__
        """
        SetTypedPointer(pointer, shader, pointerTypeID)
        
        Utility function for setting a pointer value with type information.
        
        :param int pointer: The actual pointer value.
        :param ResourceId shader: The shader containing the type information.
        :param int pointerTypeID: The type's index in the shader's :data:`ShaderReflection.pointerTypes`
          list.
        """
        pass

    def SetTypelessPointer(self, pointer: int): # real signature unknown; restored from __doc__
        """
        SetTypelessPointer(pointer)
        
        Utility function for setting a pointer value with no type information.
        
        :param int pointer: The actual pointer value.
        """
        pass

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
    def columns(self) -> int:
        """
The number of columns in this matrix.

:type: int

"""
        pass

    @columns.setter
    def columns(self, value: int):
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
    def members(self) -> 'List[ShaderVariable]':
        """
The members of this variable.

:type: List[ShaderVariable]

"""
        pass

    @members.setter
    def members(self, value: 'List[ShaderVariable]'):
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
    def rows(self) -> int:
        """
The number of rows in this matrix.

:type: int

"""
        pass

    @rows.setter
    def rows(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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
    def value(self) -> ShaderValue:
        """
The contents of this variable if it has no members.

:type: ShaderValue

"""
        pass

    @value.setter
    def value(self, value: ShaderValue):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5522A050>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderVariable' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderVariable' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderVariable' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderVariable' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderVariable' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderVariable' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderVariable' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderVariable' objects>, 'RowMajor': <method 'RowMajor' of 'renderdoc.ShaderVariable' objects>, 'ColMajor': <method 'ColMajor' of 'renderdoc.ShaderVariable' objects>, 'SetTypelessPointer': <method 'SetTypelessPointer' of 'renderdoc.ShaderVariable' objects>, 'SetTypedPointer': <method 'SetTypedPointer' of 'renderdoc.ShaderVariable' objects>, 'GetPointer': <method 'GetPointer' of 'renderdoc.ShaderVariable' objects>, 'SetBindIndex': <method 'SetBindIndex' of 'renderdoc.ShaderVariable' objects>, 'GetBindIndex': <method 'GetBindIndex' of 'renderdoc.ShaderVariable' objects>, 'SetDirectAccess': <method 'SetDirectAccess' of 'renderdoc.ShaderVariable' objects>, 'GetDirectAccess': <method 'GetDirectAccess' of 'renderdoc.ShaderVariable' objects>, 'IsDirectAccess': <method 'IsDirectAccess' of 'renderdoc.ShaderVariable' objects>, 'value': <attribute 'value' of 'renderdoc.ShaderVariable' objects>, 'name': <attribute 'name' of 'renderdoc.ShaderVariable' objects>, 'members': <attribute 'members' of 'renderdoc.ShaderVariable' objects>, 'rows': <attribute 'rows' of 'renderdoc.ShaderVariable' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderVariable' objects>, 'type': <attribute 'type' of 'renderdoc.ShaderVariable' objects>, 'flags': <attribute 'flags' of 'renderdoc.ShaderVariable' objects>, 'columns': <attribute 'columns' of 'renderdoc.ShaderVariable' objects>, '__doc__': '\\nHolds a single named shader variable. It contains either a primitive type (up to a 4x4\\nmatrix of a :class:`basic type <VarType>`) or a list of members, which can either be struct or array\\nmembers of this parent variable.\\n\\nMatrices are always stored row-major. If necessary they are transposed when retrieving from the raw\\ndata bytes when they are specified to be column-major in the API/shader metadata.\\n\\n'})"


