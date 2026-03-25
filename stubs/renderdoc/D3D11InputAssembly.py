# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderReflection import ShaderReflection
from .D3D11IndexBuffer import D3D11IndexBuffer
from .D3D11Layout import D3D11Layout
from .ResourceId import ResourceId
from .Topology import Topology
from .D3D11VertexBuffer import D3D11VertexBuffer

class D3D11InputAssembly(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the input assembler data. """
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
    def bytecode(self) -> ShaderReflection:
        """
The shader reflection for the bytecode used to create the input layout.

:type: ShaderReflection

"""
        pass

    @bytecode.setter
    def bytecode(self, value: ShaderReflection):
        pass

    @property
    def indexBuffer(self) -> D3D11IndexBuffer:
        """
The bound index buffer.

:type: D3D11IndexBuffer

"""
        pass

    @indexBuffer.setter
    def indexBuffer(self, value: D3D11IndexBuffer):
        pass

    @property
    def layouts(self) -> List[D3D11Layout]:
        """
The input layout elements in this layout.

:type: List[D3D11Layout]

"""
        pass

    @layouts.setter
    def layouts(self, value: List[D3D11Layout]):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the layout object.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
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
    def vertexBuffers(self) -> List[D3D11VertexBuffer]:
        """
The bound vertex buffers

:type: List[D3D11VertexBuffer]

"""
        pass

    @vertexBuffers.setter
    def vertexBuffers(self, value: List[D3D11VertexBuffer]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55229B10>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D11InputAssembly' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D11InputAssembly' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D11InputAssembly' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D11InputAssembly' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D11InputAssembly' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D11InputAssembly' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D11InputAssembly' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D11InputAssembly' objects>, 'bytecode': <attribute 'bytecode' of 'renderdoc.D3D11InputAssembly' objects>, 'layouts': <attribute 'layouts' of 'renderdoc.D3D11InputAssembly' objects>, 'indexBuffer': <attribute 'indexBuffer' of 'renderdoc.D3D11InputAssembly' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.D3D11InputAssembly' objects>, 'vertexBuffers': <attribute 'vertexBuffers' of 'renderdoc.D3D11InputAssembly' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D11InputAssembly' objects>, 'topology': <attribute 'topology' of 'renderdoc.D3D11InputAssembly' objects>, '__doc__': 'Describes the input assembler data.'})"


