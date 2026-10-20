from ._ShaderComputeMessageLocation import ShaderComputeMessageLocation
from ._ShaderGeometryMessageLocation import ShaderGeometryMessageLocation
from ._ShaderMeshMessageLocation import ShaderMeshMessageLocation
from ._ShaderPixelMessageLocation import ShaderPixelMessageLocation
from ._ShaderVertexMessageLocation import ShaderVertexMessageLocation

from typing import overload

class ShaderMessageLocation():
    # Original docstring
    """
    A shader message's location.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderMessageLocation.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderMessageLocation'):
        """
        Construct a new ShaderMessageLocation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
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
    def vertex(self) -> ShaderVertexMessageLocation:
        """
        The location if the shader is a vertex shader.
        
        :type: ShaderVertexMessageLocation
        """
        pass
    
    @vertex.setter
    def vertex(self, value: ShaderVertexMessageLocation):
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
    def pixel(self) -> ShaderPixelMessageLocation:
        """
        The location if the shader is a pixel shader.
        
        :type: ShaderPixelMessageLocation
        """
        pass
    
    @pixel.setter
    def pixel(self, value: ShaderPixelMessageLocation):
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
    
