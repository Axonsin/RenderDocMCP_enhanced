# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VarType import VarType
from .ShaderVariableFlags import ShaderVariableFlags
from .ShaderConstant import ShaderConstant

class ShaderConstantType(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the type and members of a :class:`ShaderConstant`. """
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
    def members(self) -> List[ShaderConstant]:
        """
Any members that this constant may contain.

:type: List[ShaderConstant]

"""
        pass

    @members.setter
    def members(self, value: List[ShaderConstant]):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5520B870>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderConstantType' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderConstantType' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderConstantType' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderConstantType' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderConstantType' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderConstantType' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderConstantType' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderConstantType' objects>, 'RowMajor': <method 'RowMajor' of 'renderdoc.ShaderConstantType' objects>, 'ColMajor': <method 'ColMajor' of 'renderdoc.ShaderConstantType' objects>, 'baseType': <attribute 'baseType' of 'renderdoc.ShaderConstantType' objects>, 'name': <attribute 'name' of 'renderdoc.ShaderConstantType' objects>, 'members': <attribute 'members' of 'renderdoc.ShaderConstantType' objects>, 'rows': <attribute 'rows' of 'renderdoc.ShaderConstantType' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderConstantType' objects>, 'elements': <attribute 'elements' of 'renderdoc.ShaderConstantType' objects>, 'arrayByteStride': <attribute 'arrayByteStride' of 'renderdoc.ShaderConstantType' objects>, 'matrixByteStride': <attribute 'matrixByteStride' of 'renderdoc.ShaderConstantType' objects>, 'flags': <attribute 'flags' of 'renderdoc.ShaderConstantType' objects>, 'pointerTypeID': <attribute 'pointerTypeID' of 'renderdoc.ShaderConstantType' objects>, 'columns': <attribute 'columns' of 'renderdoc.ShaderConstantType' objects>, '__doc__': 'Describes the type and members of a :class:`ShaderConstant`.'})"


