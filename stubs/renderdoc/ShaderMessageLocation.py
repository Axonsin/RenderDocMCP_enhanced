# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderComputeMessageLocation import ShaderComputeMessageLocation
from .ShaderGeometryMessageLocation import ShaderGeometryMessageLocation
from .ShaderMeshMessageLocation import ShaderMeshMessageLocation
from .ShaderPixelMessageLocation import ShaderPixelMessageLocation
from .ShaderVertexMessageLocation import ShaderVertexMessageLocation

class ShaderMessageLocation(): # skipped bases: <class 'SwigPyObject'>
    """ A shader message's location. """
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
    def compute(self) -> ShaderComputeMessageLocation:
        """
The location if the shader is a compute shader.

:type: ShaderComputeMessageLocation

"""
        pass

    @compute.setter
    def compute(self, value: ShaderComputeMessageLocation):
        pass

    @property
    def geometry(self) -> ShaderGeometryMessageLocation:
        """
The location if the shader is a geometry shader.

:type: ShaderGeometryMessageLocation

"""
        pass

    @geometry.setter
    def geometry(self, value: ShaderGeometryMessageLocation):
        pass

    @property
    def mesh(self) -> ShaderMeshMessageLocation:
        """
The location if the shader is a task or mesh shader.

:type: ShaderMeshMessageLocation

"""
        pass

    @mesh.setter
    def mesh(self, value: ShaderMeshMessageLocation):
        pass

    @property
    def pixel(self) -> ShaderPixelMessageLocation:
        """
The location if the shader is a pixel shader.

:type: ShaderPixelMessageLocation

"""
        pass

    @pixel.setter
    def pixel(self, value: ShaderPixelMessageLocation):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vertex(self) -> ShaderVertexMessageLocation:
        """
The location if the shader is a vertex shader.

:type: ShaderVertexMessageLocation

"""
        pass

    @vertex.setter
    def vertex(self, value: ShaderVertexMessageLocation):
        pass


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55220630>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'mesh\': <attribute \'mesh\' of \'renderdoc.ShaderMessageLocation\' objects>, \'vertex\': <attribute \'vertex\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.ShaderMessageLocation\' objects>, \'compute\': <attribute \'compute\' of \'renderdoc.ShaderMessageLocation\' objects>, \'pixel\': <attribute \'pixel\' of \'renderdoc.ShaderMessageLocation\' objects>, \'geometry\': <attribute \'geometry\' of \'renderdoc.ShaderMessageLocation\' objects>, \'__doc__\': "A shader message\'s location."})'


