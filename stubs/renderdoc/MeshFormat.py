# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceFormat import ResourceFormat
from .ResourceId import ResourceId
from .FloatVector import FloatVector
from .MeshletSize import MeshletSize
from .TaskGroupSize import TaskGroupSize
from .Topology import Topology

class MeshFormat(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the details of a single element of data (such as position or texture
    co-ordinates) within a mesh.
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
    def allowRestart(self) -> bool:
        """
``True`` if the primitive restart index feature should be used.

:type: bool

"""
        pass

    @allowRestart.setter
    def allowRestart(self, value: bool):
        pass

    @property
    def baseVertex(self) -> int:
        """
For indexed meshes, a value added to each index before using it to read the vertex.

:type: int

"""
        pass

    @baseVertex.setter
    def baseVertex(self, value: int):
        pass

    @property
    def dispatchSize(self) -> Tuple[int,int,int]:
        """
The size of the dispatch that launched a meshlet based draw.

Only valid for the task stage if task shaders are used.

.. note::
  This is present because the dispatch size at the time of the mesh output fetch may not match the
  :data:`ActionDescription.dispatchDimension` due to non-determinism in the capture. Being present
  here allows the replay to process the mesh output validly in itself without seeing a mismatch.

:type: Tuple[int,int,int]

"""
        pass

    @dispatchSize.setter
    def dispatchSize(self, value: Tuple[int,int,int]):
        pass

    @property
    def farPlane(self) -> float:
        """
The far plane for the projection matrix.

:type: float

"""
        pass

    @farPlane.setter
    def farPlane(self, value: float):
        pass

    @property
    def flipY(self) -> bool:
        """
``True`` if there is an implicit Y-flip to account for in the projection.

:type: bool

"""
        pass

    @flipY.setter
    def flipY(self, value: bool):
        pass

    @property
    def format(self) -> ResourceFormat:
        """
The format description of this mesh components elements.

:type: ResourceFormat

"""
        pass

    @format.setter
    def format(self, value: ResourceFormat):
        pass

    @property
    def indexByteOffset(self) -> int:
        """
The offset in bytes where the indices start in idxbuf.

:type: int

"""
        pass

    @indexByteOffset.setter
    def indexByteOffset(self, value: int):
        pass

    @property
    def indexByteSize(self) -> int:
        """
The number of bytes to use from the index buffer. Only valid on APIs that allow it.

:type: int

"""
        pass

    @indexByteSize.setter
    def indexByteSize(self, value: int):
        pass

    @property
    def indexByteStride(self) -> int:
        """
The width in bytes of each index. Valid values are 1 (depending on API), 2 or 4.

:type: int

"""
        pass

    @indexByteStride.setter
    def indexByteStride(self, value: int):
        pass

    @property
    def indexResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the index buffer that goes with this mesh element.

:type: ResourceId

"""
        pass

    @indexResourceId.setter
    def indexResourceId(self, value: ResourceId):
        pass

    @property
    def instanced(self) -> bool:
        """
``True`` if this mesh element comes from instanced data. See :data:`instStepRate`.

:type: bool

"""
        pass

    @instanced.setter
    def instanced(self, value: bool):
        pass

    @property
    def instStepRate(self) -> int:
        """
The number of instances to render with the same value. See :data:`instanced`.

:type: int

"""
        pass

    @instStepRate.setter
    def instStepRate(self, value: int):
        pass

    @property
    def meshColor(self) -> FloatVector:
        """
The color to use for rendering the wireframe of this mesh element.

:type: FloatVector

"""
        pass

    @meshColor.setter
    def meshColor(self, value: FloatVector):
        pass

    @property
    def meshletIndexOffset(self) -> int:
        """
If showing a set of meshlets that don't start from index 0, this is the number of
vertices to consider skipped before :data:`meshletSizes` - equivalent to baseVertex.

Primarily useful for keeping a consistent colouring of meshlets when filtering to a subset

See also :data:`meshletOffset`.

:type: int

"""
        pass

    @meshletIndexOffset.setter
    def meshletIndexOffset(self, value: int):
        pass

    @property
    def meshletOffset(self) -> int:
        """
If showing a set of meshlets that don't start from meshlet 0, this is the number of
meshlet to consider skipped before :data:`meshletSizes`.

Primarily useful for keeping a consistent colouring of meshlets when filtering to a subset

See also :data:`meshletIndexOffset`.

:type: int

"""
        pass

    @meshletOffset.setter
    def meshletOffset(self, value: int):
        pass

    @property
    def meshletSizes(self) -> List[MeshletSize]:
        """
The size of each meshlet, for a meshlet based draw.

Each meshlet lists its individual size, but a cumulative sum can be used for defining boundaries
between meshlets either by raw vertex order (using the number of indices) or by index value (using
the number of vertices).

:type: List[MeshletSize]

"""
        pass

    @meshletSizes.setter
    def meshletSizes(self, value: List[MeshletSize]):
        pass

    @property
    def nearPlane(self) -> float:
        """
The near plane for the projection matrix.

:type: float

"""
        pass

    @nearPlane.setter
    def nearPlane(self, value: float):
        pass

    @property
    def numIndices(self) -> int:
        """
The number of vertices in the mesh.

:type: int

"""
        pass

    @numIndices.setter
    def numIndices(self, value: int):
        pass

    @property
    def perPrimitiveOffset(self) -> int:
        """
The offset in bytes to the start of the per-primitive rate vertex data.

Only for meshlet outputs.

:type: int

"""
        pass

    @perPrimitiveOffset.setter
    def perPrimitiveOffset(self, value: int):
        pass

    @property
    def perPrimitiveStride(self) -> int:
        """
The stride in bytes of the per-primitive rate vertex data.

Only for meshlet outputs.

:type: int

"""
        pass

    @perPrimitiveStride.setter
    def perPrimitiveStride(self, value: int):
        pass

    @property
    def restartIndex(self) -> int:
        """
The primitive restart index to use, if possible. See :data:`allowRestart`.

:type: int

"""
        pass

    @restartIndex.setter
    def restartIndex(self, value: int):
        pass

    @property
    def showAlpha(self) -> bool:
        """
``True`` if the alpha component of this element should be used.

:type: bool

"""
        pass

    @showAlpha.setter
    def showAlpha(self, value: bool):
        pass

    @property
    def status(self) -> str:
        """
A string with the status of this mesh format - only used when a mesh format is
returned to the application detailing e.g. vertex output data.

An empty string indicates no errors/problems.

:type: str

"""
        pass

    @status.setter
    def status(self, value: str):
        pass

    @property
    def taskSizes(self) -> List[TaskGroupSize]:
        """
The size of each task group's dispatch, for a meshlet based draw.

Each group of a task shader within a dispatch can itself fill out a payload and dispatch a number
of mesh groups. This list contains the 3-dimensional dimension that each task group emitted.

:type: List[TaskGroupSize]

"""
        pass

    @taskSizes.setter
    def taskSizes(self, value: List[TaskGroupSize]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def topology(self) -> Topology:
        """
The :class:`Topology` that describes the primitives in this mesh.

:type: Topology

"""
        pass

    @topology.setter
    def topology(self, value: Topology):
        pass

    @property
    def unproject(self) -> bool:
        """
``True`` if this mesh element contains post-projection positional data.

:type: bool

"""
        pass

    @unproject.setter
    def unproject(self, value: bool):
        pass

    @property
    def vertexByteOffset(self) -> int:
        """
The offset in bytes to the start of the vertex data.

:type: int

"""
        pass

    @vertexByteOffset.setter
    def vertexByteOffset(self, value: int):
        pass

    @property
    def vertexByteSize(self) -> int:
        """
The number of bytes to use from the vertex buffer. Only valid on APIs that allow it.

:type: int

"""
        pass

    @vertexByteSize.setter
    def vertexByteSize(self, value: int):
        pass

    @property
    def vertexByteStride(self) -> int:
        """
The stride in bytes between the start of one vertex and the start of another.

:type: int

"""
        pass

    @vertexByteStride.setter
    def vertexByteStride(self, value: int):
        pass

    @property
    def vertexResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the vertex buffer containing this mesh element.

:type: ResourceId

"""
        pass

    @vertexResourceId.setter
    def vertexResourceId(self, value: ResourceId):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552318E0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.MeshFormat' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.MeshFormat' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.MeshFormat' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.MeshFormat' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.MeshFormat' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.MeshFormat' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.MeshFormat' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.MeshFormat' objects>, 'instanced': <attribute 'instanced' of 'renderdoc.MeshFormat' objects>, 'dispatchSize': <attribute 'dispatchSize' of 'renderdoc.MeshFormat' objects>, 'baseVertex': <attribute 'baseVertex' of 'renderdoc.MeshFormat' objects>, 'vertexResourceId': <attribute 'vertexResourceId' of 'renderdoc.MeshFormat' objects>, 'indexResourceId': <attribute 'indexResourceId' of 'renderdoc.MeshFormat' objects>, 'allowRestart': <attribute 'allowRestart' of 'renderdoc.MeshFormat' objects>, 'instStepRate': <attribute 'instStepRate' of 'renderdoc.MeshFormat' objects>, 'format': <attribute 'format' of 'renderdoc.MeshFormat' objects>, 'vertexByteStride': <attribute 'vertexByteStride' of 'renderdoc.MeshFormat' objects>, 'indexByteStride': <attribute 'indexByteStride' of 'renderdoc.MeshFormat' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.MeshFormat' objects>, 'perPrimitiveStride': <attribute 'perPrimitiveStride' of 'renderdoc.MeshFormat' objects>, 'nearPlane': <attribute 'nearPlane' of 'renderdoc.MeshFormat' objects>, 'farPlane': <attribute 'farPlane' of 'renderdoc.MeshFormat' objects>, 'unproject': <attribute 'unproject' of 'renderdoc.MeshFormat' objects>, 'vertexByteOffset': <attribute 'vertexByteOffset' of 'renderdoc.MeshFormat' objects>, 'indexByteOffset': <attribute 'indexByteOffset' of 'renderdoc.MeshFormat' objects>, 'perPrimitiveOffset': <attribute 'perPrimitiveOffset' of 'renderdoc.MeshFormat' objects>, 'numIndices': <attribute 'numIndices' of 'renderdoc.MeshFormat' objects>, 'taskSizes': <attribute 'taskSizes' of 'renderdoc.MeshFormat' objects>, 'vertexByteSize': <attribute 'vertexByteSize' of 'renderdoc.MeshFormat' objects>, 'indexByteSize': <attribute 'indexByteSize' of 'renderdoc.MeshFormat' objects>, 'meshletSizes': <attribute 'meshletSizes' of 'renderdoc.MeshFormat' objects>, 'topology': <attribute 'topology' of 'renderdoc.MeshFormat' objects>, 'meshletOffset': <attribute 'meshletOffset' of 'renderdoc.MeshFormat' objects>, 'meshletIndexOffset': <attribute 'meshletIndexOffset' of 'renderdoc.MeshFormat' objects>, 'restartIndex': <attribute 'restartIndex' of 'renderdoc.MeshFormat' objects>, 'meshColor': <attribute 'meshColor' of 'renderdoc.MeshFormat' objects>, 'status': <attribute 'status' of 'renderdoc.MeshFormat' objects>, 'showAlpha': <attribute 'showAlpha' of 'renderdoc.MeshFormat' objects>, 'flipY': <attribute 'flipY' of 'renderdoc.MeshFormat' objects>, '__doc__': '\\nContains the details of a single element of data (such as position or texture\\nco-ordinates) within a mesh.\\n\\n'})"


