from ._AxisMapping import AxisMapping
from ._Camera import Camera
from ._FloatVector import FloatVector
from ._MeshDataStage import MeshDataStage
from ._MeshFormat import MeshFormat
from ._Visualisation import Visualisation

from typing import overload

class MeshDisplay():
    # Original docstring
    """
    Describes how to render a mesh preview of one or more meshes. Describes the camera configuration as
    well as what options to use when rendering both the current mesh, and any other auxiliary meshes.
    
    .. data:: NoHighlight
    
      Value for :data:`highlightVert` if no vertex should be highlighted.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised MeshDisplay.
        """
        pass
    
    @overload
    def __init__(self, other: 'MeshDisplay'):
        """
        Construct a new MeshDisplay with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    NoHighlight = 4294967295
    """
    Value for :data:`highlightVert` if no vertex should be highlighted.
    """
    
    @property
    def showBBox(self) -> bool:
        """
        ``True`` if the bounding box around the mesh should be rendered.
        
        :type: bool
        """
        pass
    
    @showBBox.setter
    def showBBox(self, value: bool):
        pass
    
    @property
    def wireframeDraw(self) -> bool:
        """
        ``True`` if the wireframe of the mesh should be rendered as well as solid shading.
        
        :type: bool
        """
        pass
    
    @wireframeDraw.setter
    def wireframeDraw(self, value: bool):
        pass
    
    @property
    def showPrevInstances(self) -> bool:
        """
        ``True`` if all previous instances in the drawcall should be drawn as secondary meshes.
        
        :type: bool
        """
        pass
    
    @showPrevInstances.setter
    def showPrevInstances(self, value: bool):
        pass
    
    @property
    def showAllInstances(self) -> bool:
        """
        ``True`` if all instances in the drawcall should be drawn as secondary meshes.
        
        :type: bool
        """
        pass
    
    @showAllInstances.setter
    def showAllInstances(self, value: bool):
        pass
    
    @property
    def curView(self) -> int:
        """
        The index of the currently selected multiview view in the drawcall.
        
        :type: int
        """
        pass
    
    @curView.setter
    def curView(self, value: int):
        pass
    
    @property
    def cam(self) -> Camera:
        """
        The camera to use when rendering all of the meshes.
        
        :type: Camera
        """
        pass
    
    @cam.setter
    def cam(self, value: Camera):
        pass
    
    @property
    def aspect(self) -> float:
        """
        The aspect ratio to use when calculating a perspective projection matrix.
        
        :type: float
        """
        pass
    
    @aspect.setter
    def aspect(self, value: float):
        pass
    
    @property
    def visualisationMode(self) -> Visualisation:
        """
        The :class:`visualisation mode <Visualisation>` to use when rendering the current mesh.
        
        :type: Visualisation
        """
        pass
    
    @visualisationMode.setter
    def visualisationMode(self, value: Visualisation):
        pass
    
    @property
    def ortho(self) -> bool:
        """
        ``True`` if the projection matrix to use when unprojecting vertex positions is orthographic.
        
        :type: bool
        """
        pass
    
    @ortho.setter
    def ortho(self, value: bool):
        pass
    
    @property
    def second(self) -> MeshFormat:
        """
        The configuration for the primary mesh's secondary data, if used for solid shading.
        
        :type: MeshFormat
        """
        pass
    
    @second.setter
    def second(self, value: MeshFormat):
        pass
    
    @property
    def minBounds(self) -> FloatVector:
        """
        The minimum co-ordinates in each axis of the mesh bounding box.
        
        :type: FloatVector
        """
        pass
    
    @minBounds.setter
    def minBounds(self, value: FloatVector):
        pass
    
    @property
    def maxBounds(self) -> FloatVector:
        """
        The maximum co-ordinates in each axis of the mesh bounding box.
        
        :type: FloatVector
        """
        pass
    
    @maxBounds.setter
    def maxBounds(self, value: FloatVector):
        pass
    
    @property
    def position(self) -> MeshFormat:
        """
        The configuration for the primary mesh's position data.
        
        :type: MeshFormat
        """
        pass
    
    @position.setter
    def position(self, value: MeshFormat):
        pass
    
    @property
    def type(self) -> MeshDataStage:
        """
        The :class:`MeshDataStage` where this mesh data comes from.
        
        :type: MeshDataStage
        """
        pass
    
    @type.setter
    def type(self, value: MeshDataStage):
        pass
    
    @property
    def axisMapping(self) -> AxisMapping:
        """
        The axis mapping to apply to the mesh.
        
        :type: AxisMapping
        """
        pass
    
    @axisMapping.setter
    def axisMapping(self, value: AxisMapping):
        pass
    
    @property
    def vtxExploderSliderSNorm(self) -> float:
        """
        Displace/explode vertices to help visualise vertex reuse vs disjointedness.
        
        :type: float
        """
        pass
    
    @vtxExploderSliderSNorm.setter
    def vtxExploderSliderSNorm(self, value: float):
        pass
    
    @property
    def curInstance(self) -> int:
        """
        The index of the currently selected instance in the drawcall.
        
        :type: int
        """
        pass
    
    @curInstance.setter
    def curInstance(self, value: int):
        pass
    
    @property
    def exploderScale(self) -> float:
        """
        Scales the exploded vertex displacement.
        
        :type: float
        """
        pass
    
    @exploderScale.setter
    def exploderScale(self, value: float):
        pass
    
    @property
    def highlightVert(self) -> int:
        """
        The index of the vertex to highlight, or :data:`NoHighlight` to select no vertex.
        
        :type: int
        """
        pass
    
    @highlightVert.setter
    def highlightVert(self, value: int):
        pass
    
    @property
    def fov(self) -> float:
        """
        The field of view to use when calculating a perspective projection matrix.
        
        :type: float
        """
        pass
    
    @fov.setter
    def fov(self, value: float):
        pass
    
    @property
    def showWholePass(self) -> bool:
        """
        ``True`` if all draws in the current pass up to the current draw should be drawn as secondary meshes.
        
        :type: bool
        """
        pass
    
    @showWholePass.setter
    def showWholePass(self, value: bool):
        pass
    
