# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderVertexMessageLocation(): # skipped bases: <class 'SwigPyObject'>
    """ A vertex shader message's location. """
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
    def instance(self) -> int:
        """
The instance for this vertex.

:type: int

"""
        pass

    @instance.setter
    def instance(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vertexIndex(self) -> int:
        """
The vertex or index for this vertex.

:type: int

"""
        pass

    @vertexIndex.setter
    def vertexIndex(self, value: int):
        pass

    @property
    def view(self) -> int:
        """
The multiview view for this vertex, or ``0`` if multiview is disabled.

:type: int

"""
        pass

    @view.setter
    def view(self, value: int):
        pass


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551EF7E0>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'view\': <attribute \'view\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'vertexIndex\': <attribute \'vertexIndex\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'instance\': <attribute \'instance\' of \'renderdoc.ShaderVertexMessageLocation\' objects>, \'__doc__\': "A vertex shader message\'s location."})'


