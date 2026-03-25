# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderComputeMessageLocation(): # skipped bases: <class 'SwigPyObject'>
    """ A compute shader message's location. """
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def thread(self) -> Tuple[int,int,int]:
        """
The thread index within the workgroup.

:type: Tuple[int,int,int]

"""
        pass

    @thread.setter
    def thread(self, value: Tuple[int,int,int]):
        pass

    @property
    def workgroup(self) -> Tuple[int,int,int]:
        """
The workgroup index within the dispatch.

:type: Tuple[int,int,int]

"""
        pass

    @workgroup.setter
    def workgroup(self, value: Tuple[int,int,int]):
        pass


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5522E730>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'workgroup\': <attribute \'workgroup\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'thread\': <attribute \'thread\' of \'renderdoc.ShaderComputeMessageLocation\' objects>, \'__doc__\': "A compute shader message\'s location."})'


