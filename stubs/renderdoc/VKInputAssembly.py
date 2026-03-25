# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKIndexBuffer import VKIndexBuffer
from .Topology import Topology

class VKInputAssembly(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the vulkan input assembly configuration. """
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
    def indexBuffer(self) -> VKIndexBuffer:
        """
The index buffer binding.

:type: VKIndexBuffer

"""
        pass

    @indexBuffer.setter
    def indexBuffer(self, value: VKIndexBuffer):
        pass

    @property
    def primitiveRestartEnable(self) -> bool:
        """
``True`` if primitive restart is enabled for strip primitives.

:type: bool

"""
        pass

    @primitiveRestartEnable.setter
    def primitiveRestartEnable(self, value: bool):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55212D00>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKInputAssembly' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKInputAssembly' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKInputAssembly' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKInputAssembly' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKInputAssembly' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKInputAssembly' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKInputAssembly' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKInputAssembly' objects>, 'indexBuffer': <attribute 'indexBuffer' of 'renderdoc.VKInputAssembly' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKInputAssembly' objects>, 'topology': <attribute 'topology' of 'renderdoc.VKInputAssembly' objects>, 'primitiveRestartEnable': <attribute 'primitiveRestartEnable' of 'renderdoc.VKInputAssembly' objects>, '__doc__': 'Describes the vulkan input assembly configuration.'})"


