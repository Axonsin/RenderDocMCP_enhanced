# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceFormat import ResourceFormat

class D3D11Layout(): # skipped bases: <class 'SwigPyObject'>
    """
    Describes a single D3D11 input layout element for one vertex input.
    
    .. data:: TightlyPacked
    
      Value for :data:`byteOffset` that indicates this element is tightly packed.
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
    def perInstance(self) -> bool:
        """
``True`` if the vertex data is instance-rate.

:type: bool

"""
        pass

    @perInstance.setter
    def perInstance(self, value: bool):
        pass

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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    TightlyPacked = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'TightlyPacked': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551DE4C0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D11Layout' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D11Layout' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D11Layout' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D11Layout' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D11Layout' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D11Layout' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D11Layout' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D11Layout' objects>, 'semanticIndex': <attribute 'semanticIndex' of 'renderdoc.D3D11Layout' objects>, 'semanticName': <attribute 'semanticName' of 'renderdoc.D3D11Layout' objects>, 'instanceDataStepRate': <attribute 'instanceDataStepRate' of 'renderdoc.D3D11Layout' objects>, 'format': <attribute 'format' of 'renderdoc.D3D11Layout' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D11Layout' objects>, 'inputSlot': <attribute 'inputSlot' of 'renderdoc.D3D11Layout' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.D3D11Layout' objects>, 'perInstance': <attribute 'perInstance' of 'renderdoc.D3D11Layout' objects>, '__doc__': '\\nDescribes a single D3D11 input layout element for one vertex input.\\n\\n.. data:: TightlyPacked\\n\\n  Value for :data:`byteOffset` that indicates this element is tightly packed.\\n\\n'})"


