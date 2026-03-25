# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .D3D12RootParam import D3D12RootParam
from .ResourceId import ResourceId
from .D3D12StaticSampler import D3D12StaticSampler

class D3D12RootSignature(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the root signature structure and root parameters. """
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
    def parameters(self) -> List[D3D12RootParam]:
        """
The parameters in this root signature.

:type: List[D3D12RootParam]

"""
        pass

    @parameters.setter
    def parameters(self, value: List[D3D12RootParam]):
        pass

    @property
    def resourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the root signature object.

:type: ResourceId

"""
        pass

    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass

    @property
    def staticSamplers(self) -> List[D3D12StaticSampler]:
        """
The static samplers defined in this root signature.

:type: List[D3D12StaticSampler]

"""
        pass

    @staticSamplers.setter
    def staticSamplers(self, value: List[D3D12StaticSampler]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551CA550>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12RootSignature' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12RootSignature' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12RootSignature' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12RootSignature' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12RootSignature' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12RootSignature' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12RootSignature' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12RootSignature' objects>, 'parameters': <attribute 'parameters' of 'renderdoc.D3D12RootSignature' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.D3D12RootSignature' objects>, 'staticSamplers': <attribute 'staticSamplers' of 'renderdoc.D3D12RootSignature' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12RootSignature' objects>, '__doc__': 'Contains the root signature structure and root parameters.'})"


