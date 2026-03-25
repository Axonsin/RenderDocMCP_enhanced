# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .D3D12IndexBuffer import D3D12IndexBuffer
from .D3D12Layout import D3D12Layout
from .Topology import Topology
from .D3D12VertexBuffer import D3D12VertexBuffer

class D3D12InputAssembly(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the input assembler state in the PSO. """
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
    def indexBuffer(self) -> D3D12IndexBuffer:
        """
The bound index buffer.

:type: D3D12IndexBuffer

"""
        pass

    @indexBuffer.setter
    def indexBuffer(self, value: D3D12IndexBuffer):
        pass

    @property
    def indexStripCutValue(self) -> int:
        """
The index value to use for cutting strips. Either ``0``, ``0xffff`` or ``0xffffffff``.
If the value is 0, strip cutting is disabled.

:type: int

"""
        pass

    @indexStripCutValue.setter
    def indexStripCutValue(self, value: int):
        pass

    @property
    def layouts(self) -> List[D3D12Layout]:
        """
The input layout elements in this layout.

:type: List[D3D12Layout]

"""
        pass

    @layouts.setter
    def layouts(self, value: List[D3D12Layout]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def topology(self) -> Topology:
        """
The current primitive topology.

:type: Topology

"""
        pass

    @topology.setter
    def topology(self, value: Topology):
        pass

    @property
    def vertexBuffers(self) -> List[D3D12VertexBuffer]:
        """
The bound vertex buffers

:type: List[D3D12VertexBuffer]

"""
        pass

    @vertexBuffers.setter
    def vertexBuffers(self, value: List[D3D12VertexBuffer]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D15E0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12InputAssembly' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12InputAssembly' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12InputAssembly' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12InputAssembly' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12InputAssembly' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12InputAssembly' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12InputAssembly' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12InputAssembly' objects>, 'layouts': <attribute 'layouts' of 'renderdoc.D3D12InputAssembly' objects>, 'indexBuffer': <attribute 'indexBuffer' of 'renderdoc.D3D12InputAssembly' objects>, 'indexStripCutValue': <attribute 'indexStripCutValue' of 'renderdoc.D3D12InputAssembly' objects>, 'vertexBuffers': <attribute 'vertexBuffers' of 'renderdoc.D3D12InputAssembly' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12InputAssembly' objects>, 'topology': <attribute 'topology' of 'renderdoc.D3D12InputAssembly' objects>, '__doc__': 'Describes the input assembler state in the PSO.'})"


