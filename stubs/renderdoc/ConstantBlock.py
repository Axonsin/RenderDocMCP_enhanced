# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderConstant import ShaderConstant

class ConstantBlock(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the information for a block of constant values. The values are not present,
    only the metadata about how the variables are stored in memory itself and their type/name
    information.
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
    def bindArraySize(self) -> int:
        """
If this binding is natively arrayed, how large is the array size. If not arrayed, this
will be set to 1.

This value may be set to a very large number if the array is unbounded in the shader.

:type: int

"""
        pass

    @bindArraySize.setter
    def bindArraySize(self, value: int):
        pass

    @property
    def bufferBacked(self) -> bool:
        """
``True`` if the contents are stored in a buffer of memory. If not then they are set by
some other API-specific method, such as direct function calls or they may be compile-time
specialisation constants.

:type: bool

"""
        pass

    @bufferBacked.setter
    def bufferBacked(self, value: bool):
        pass

    @property
    def byteSize(self) -> int:
        """
The total number of bytes consumed by all of the constants contained in this block.

:type: int

"""
        pass

    @byteSize.setter
    def byteSize(self, value: int):
        pass

    @property
    def compileConstants(self) -> bool:
        """
``True`` if this is a virtual buffer listing compile-time specialisation constants.

:type: bool

"""
        pass

    @compileConstants.setter
    def compileConstants(self, value: bool):
        pass

    @property
    def fixedBindNumber(self) -> int:
        """
The fixed binding number for this binding. The interpretation of this is API-specific
and it is provided purely for informational purposes and has no bearing on how data is accessed or
described. Similarly some bindings don't have a fixed bind number and the value here should not be
relied on.

For OpenGL only, this value is not used as bindings are dynamic and cannot be determined by the
shader reflection. Bindings must be determined only by the descriptor mapped to.

Generally speaking sorting by this number will give a reasonable ordering by binding if it exists.

.. note::
  Because this number is API-specific, there is no guarantee that it will be unique across all
  resources, though generally it will be unique within all binds of the same type. It should be used
  only within contexts that can interpret it API-specifically, or else for purely
  informational/non-semantic purposes like sorting.

:type: int

"""
        pass

    @fixedBindNumber.setter
    def fixedBindNumber(self, value: int):
        pass

    @property
    def fixedBindSetOrSpace(self) -> int:
        """
The fixed binding set or space for this binding. This is API-specific, on Vulkan this
gives the set and on D3D12 this gives the register space.
It is provided purely for informational purposes and has no bearing on how data is accessed or
described.

Generally speaking sorting by this number before :data:`fixedBindNumber` will give a reasonable
ordering by binding if it exists.

:type: int

"""
        pass

    @fixedBindSetOrSpace.setter
    def fixedBindSetOrSpace(self, value: int):
        pass

    @property
    def inlineDataBytes(self) -> bool:
        """
``True`` if this is backed by in-line data bytes rather than a specific buffer.

:type: bool

"""
        pass

    @inlineDataBytes.setter
    def inlineDataBytes(self, value: bool):
        pass

    @property
    def name(self) -> str:
        """
The name of this constant block, may be empty on some APIs.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def variables(self) -> List[ShaderConstant]:
        """
The constants contained within this block.

:type: List[ShaderConstant]

"""
        pass

    @variables.setter
    def variables(self, value: List[ShaderConstant]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551CDFF0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ConstantBlock' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ConstantBlock' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ConstantBlock' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ConstantBlock' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ConstantBlock' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ConstantBlock' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ConstantBlock' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ConstantBlock' objects>, 'bindArraySize': <attribute 'bindArraySize' of 'renderdoc.ConstantBlock' objects>, 'bufferBacked': <attribute 'bufferBacked' of 'renderdoc.ConstantBlock' objects>, 'name': <attribute 'name' of 'renderdoc.ConstantBlock' objects>, 'inlineDataBytes': <attribute 'inlineDataBytes' of 'renderdoc.ConstantBlock' objects>, 'variables': <attribute 'variables' of 'renderdoc.ConstantBlock' objects>, 'fixedBindNumber': <attribute 'fixedBindNumber' of 'renderdoc.ConstantBlock' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ConstantBlock' objects>, 'compileConstants': <attribute 'compileConstants' of 'renderdoc.ConstantBlock' objects>, 'fixedBindSetOrSpace': <attribute 'fixedBindSetOrSpace' of 'renderdoc.ConstantBlock' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.ConstantBlock' objects>, '__doc__': '\\nContains the information for a block of constant values. The values are not present,\\nonly the metadata about how the variables are stored in memory itself and their type/name\\ninformation.\\n\\n'})"


