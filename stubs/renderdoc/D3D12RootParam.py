# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .Descriptor import Descriptor
from .ResourceId import ResourceId
from .D3D12RootTableRange import D3D12RootTableRange
from .ShaderStageMask import ShaderStageMask

class D3D12RootParam(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the structure and content of a single root parameter. """
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
    def constants(self) -> bytes:
        """
For a root constant parameter, the words defined.

:type: bytes

"""
        pass

    @constants.setter
    def constants(self, value: bytes):
        pass

    @property
    def descriptor(self) -> Descriptor:
        """
For a root descriptor parameter, the descriptor itself.

:type: Descriptor

"""
        pass

    @descriptor.setter
    def descriptor(self, value: Descriptor):
        pass

    @property
    def heap(self) -> ResourceId:
        """
For a root table parameter, the descriptor heap bound to this parameter. See
:data:`heapByteOffset` and :data:`tableRanges`.

:type: ResourceId

"""
        pass

    @heap.setter
    def heap(self, value: ResourceId):
        pass

    @property
    def heapByteOffset(self) -> int:
        """
For a root table parameter, the byte offset into the descriptor heap bound to this
parameter. See :data:`heap` and :data:`tableRanges`.

:type: int

"""
        pass

    @heapByteOffset.setter
    def heapByteOffset(self, value: int):
        pass

    @property
    def reg(self) -> int:
        """
For a root parameter, the register of the binding.

:type: int

"""
        pass

    @reg.setter
    def reg(self, value: int):
        pass

    @property
    def space(self) -> int:
        """
For a root parameter, the register space of the binding.

:type: int

"""
        pass

    @space.setter
    def space(self, value: int):
        pass

    @property
    def tableRanges(self) -> List[D3D12RootTableRange]:
        """
For a root table parameter, the descriptor ranges that define this table. See
:data:`heap` and :data:`heapByteOffset`.

:type: List[D3D12RootTableRange]

"""
        pass

    @tableRanges.setter
    def tableRanges(self, value: List[D3D12RootTableRange]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def visibility(self) -> ShaderStageMask:
        """
The shader stage that can access this parameter.

:type: ShaderStageMask

"""
        pass

    @visibility.setter
    def visibility(self, value: ShaderStageMask):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55224690>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12RootParam' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12RootParam' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12RootParam' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12RootParam' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12RootParam' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12RootParam' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12RootParam' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12RootParam' objects>, 'reg': <attribute 'reg' of 'renderdoc.D3D12RootParam' objects>, 'heap': <attribute 'heap' of 'renderdoc.D3D12RootParam' objects>, 'descriptor': <attribute 'descriptor' of 'renderdoc.D3D12RootParam' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12RootParam' objects>, 'visibility': <attribute 'visibility' of 'renderdoc.D3D12RootParam' objects>, 'constants': <attribute 'constants' of 'renderdoc.D3D12RootParam' objects>, 'heapByteOffset': <attribute 'heapByteOffset' of 'renderdoc.D3D12RootParam' objects>, 'tableRanges': <attribute 'tableRanges' of 'renderdoc.D3D12RootParam' objects>, 'space': <attribute 'space' of 'renderdoc.D3D12RootParam' objects>, '__doc__': 'Contains the structure and content of a single root parameter.'})"


