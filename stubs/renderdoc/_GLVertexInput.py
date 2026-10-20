from ._GLVertexAttribute import GLVertexAttribute
from ._GLVertexBuffer import GLVertexBuffer
from ._ResourceId import ResourceId
from ._Topology import Topology
from typing import List

from typing import overload

class GLVertexInput():
    # Original docstring
    """
    Describes the setup for fixed-function vertex input fetch.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised GLVertexInput.
        """
        pass
    
    @overload
    def __init__(self, other: 'GLVertexInput'):
        """
        Construct a new GLVertexInput with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def attributes(self) -> List[GLVertexAttribute]:
        """
        The vertex attributes.
        
        :type: List[GLVertexAttribute]
        """
        pass
    
    @attributes.setter
    def attributes(self, value: List[GLVertexAttribute]):
        pass
    
    @property
    def indexBuffer(self) -> ResourceId:
        """
        The :class:`ResourceId` of the index buffer.
        
        :type: ResourceId
        """
        pass
    
    @indexBuffer.setter
    def indexBuffer(self, value: ResourceId):
        pass
    
    @property
    def primitiveRestart(self) -> bool:
        """
        ``True`` if primitive restart is enabled for strip primitives.
        
        :type: bool
        """
        pass
    
    @primitiveRestart.setter
    def primitiveRestart(self, value: bool):
        pass
    
    @property
    def vertexBuffers(self) -> List[GLVertexBuffer]:
        """
        The vertex buffers.
        
        :type: List[GLVertexBuffer]
        """
        pass
    
    @vertexBuffers.setter
    def vertexBuffers(self, value: List[GLVertexBuffer]):
        pass
    
    @property
    def indexByteStride(self) -> int:
        """
        The byte width of the index buffer - typically 1, 2 or 4 bytes. It can be 0 for
        non-indexed draws.
        
        .. note::
          This does not correspond to a real GL state since the index type is specified per-action in the call
          itself. This is an implicit state derived from the last (or current) action at any given event.
        
        :type: int
        """
        pass
    
    @indexByteStride.setter
    def indexByteStride(self, value: int):
        pass
    
    @property
    def topology(self) -> Topology:
        """
        The byte width of the index buffer - typically 1, 2 or 4 bytes.
        
        .. note::
          This does not correspond to a real GL state since the topology is specified per-action in the call
          itself. This is an implicit state derived from the last (or current) action at any given event.
        
        :type: Topology
        """
        pass
    
    @topology.setter
    def topology(self, value: Topology):
        pass
    
    @property
    def provokingVertexLast(self) -> bool:
        """
        ``True`` if the provoking vertex is the last one in the primitive.
        
        ``False`` if the provoking vertex is the first one.
        
        :type: bool
        """
        pass
    
    @provokingVertexLast.setter
    def provokingVertexLast(self, value: bool):
        pass
    
    @property
    def restartIndex(self) -> int:
        """
        The index value to use to indicate a strip restart.
        
        :type: int
        """
        pass
    
    @restartIndex.setter
    def restartIndex(self, value: int):
        pass
    
    @property
    def vertexArrayObject(self) -> ResourceId:
        """
        The :class:`ResourceId` of the vertex array object that's bound.
        
        :type: ResourceId
        """
        pass
    
    @vertexArrayObject.setter
    def vertexArrayObject(self, value: ResourceId):
        pass
    
