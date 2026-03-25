# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderConstantType import ShaderConstantType

class ShaderConstant(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the detail of a constant within a struct, such as a :class:`ConstantBlock`,
    with its type and relative location in memory.
    """
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> ShaderConstantType:
        """
The type information for this constant.

:type: ShaderConstantType

"""
        pass

    @type.setter
    def type(self, value: ShaderConstantType):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B6770>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderConstant' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderConstant' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderConstant' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderConstant' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderConstant' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderConstant' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderConstant' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderConstant' objects>, 'defaultValue': <attribute 'defaultValue' of 'renderdoc.ShaderConstant' objects>, 'name': <attribute 'name' of 'renderdoc.ShaderConstant' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderConstant' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.ShaderConstant' objects>, 'type': <attribute 'type' of 'renderdoc.ShaderConstant' objects>, 'bitFieldOffset': <attribute 'bitFieldOffset' of 'renderdoc.ShaderConstant' objects>, 'bitFieldSize': <attribute 'bitFieldSize' of 'renderdoc.ShaderConstant' objects>, '__doc__': '\\nContains the detail of a constant within a struct, such as a :class:`ConstantBlock`,\\nwith its type and relative location in memory.\\n\\n'})"


