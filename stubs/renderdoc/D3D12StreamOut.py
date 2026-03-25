# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .D3D12StreamOutBind import D3D12StreamOutBind

class D3D12StreamOut(): # skipped bases: <class 'SwigPyObject'>
    """
    Describes the stream-out state in the PSO.
    
    .. data:: NoRasterization
    
      Value for :data:`rasterizedStream` that indicates no stream is being rasterized.
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
    def outputs(self) -> List[D3D12StreamOutBind]:
        """
The bound stream-out buffer bindings.

:type: List[D3D12StreamOutBind]

"""
        pass

    @outputs.setter
    def outputs(self, value: List[D3D12StreamOutBind]):
        pass

    @property
    def rasterizedStream(self) -> int:
        """
Which stream-out stream is being used for rasterization.

If the value is :data:`NoRasterization` then no stream has been selected for rasterization.

:type: int

"""
        pass

    @rasterizedStream.setter
    def rasterizedStream(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    NoRasterization = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'NoRasterization': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55202400>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12StreamOut' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12StreamOut' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12StreamOut' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12StreamOut' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12StreamOut' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12StreamOut' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12StreamOut' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12StreamOut' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12StreamOut' objects>, 'rasterizedStream': <attribute 'rasterizedStream' of 'renderdoc.D3D12StreamOut' objects>, 'outputs': <attribute 'outputs' of 'renderdoc.D3D12StreamOut' objects>, '__doc__': '\\nDescribes the stream-out state in the PSO.\\n\\n.. data:: NoRasterization\\n\\n  Value for :data:`rasterizedStream` that indicates no stream is being rasterized.\\n\\n'})"


