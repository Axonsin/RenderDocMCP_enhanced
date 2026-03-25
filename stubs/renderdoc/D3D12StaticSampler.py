# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .SamplerDescriptor import SamplerDescriptor
from .ShaderStageMask import ShaderStageMask

class D3D12StaticSampler(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the details of a single static sampler in a root signature. """
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
    def descriptor(self) -> SamplerDescriptor:
        """
The details of the sampler descriptor itself.

:type: SamplerDescriptor

"""
        pass

    @descriptor.setter
    def descriptor(self, value: SamplerDescriptor):
        pass

    @property
    def reg(self) -> int:
        """
The register number of this sampler.

:type: int

"""
        pass

    @reg.setter
    def reg(self, value: int):
        pass

    @property
    def space(self) -> int:
        """
The register space of this sampler.

:type: int

"""
        pass

    @space.setter
    def space(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def visibility(self) -> ShaderStageMask:
        """
The shader stage that can access this sampler.

:type: ShaderStageMask

"""
        pass

    @visibility.setter
    def visibility(self, value: ShaderStageMask):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551F1E60>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12StaticSampler' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12StaticSampler' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12StaticSampler' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12StaticSampler' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12StaticSampler' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12StaticSampler' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12StaticSampler' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12StaticSampler' objects>, 'reg': <attribute 'reg' of 'renderdoc.D3D12StaticSampler' objects>, 'descriptor': <attribute 'descriptor' of 'renderdoc.D3D12StaticSampler' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12StaticSampler' objects>, 'visibility': <attribute 'visibility' of 'renderdoc.D3D12StaticSampler' objects>, 'space': <attribute 'space' of 'renderdoc.D3D12StaticSampler' objects>, '__doc__': 'Contains the details of a single static sampler in a root signature.'})"


