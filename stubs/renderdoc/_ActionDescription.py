from ._APIEvent import APIEvent
from ._ActionFlags import ActionFlags
from ._FloatVector import FloatVector
from ._ResourceId import ResourceId
from ._SDFile import SDFile
from ._Subresource import Subresource
from typing import List, Tuple

from typing import overload

class ActionDescription():
    # Original docstring
    """
    Describes the properties of an action.
    
    An action is a call such as a draw, a compute dispatch, clears, copies, resolves, etc. Any GPU event
    which may have deliberate visible side-effects to application-visible memory, typically resources
    such as textures and buffers. It also includes markers, which provide a user-generated annotation of
    events and actions.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ActionDescription.
        """
        pass
    
    @overload
    def __init__(self, other: 'ActionDescription'):
        """
        Construct a new ActionDescription with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def IsFakeMarker(self) -> bool:
        """
        Returns whether or not this action corresponds to a fake marker added by
        :meth:`ReplayController.AddFakeMarkers`.
        
        Such actions may break expectations of event IDs and action IDs, so it is recommended to avoid
        processing them wherever possible.
        
        :return: Returns whether or not this action is a fake marker.
        :rtype: bool
        """
        pass
    
    
    def GetName(self, structuredFile: SDFile) -> str:
        """
        Returns the name for this action, either from its custom name (see :data:`customName`)
        or from the matching chunk in the structured data passed in.
        
        :param SDFile structuredFile: The structured data file for the capture this action is from.
        :return: Returns the best available name for this action.
        :rtype: str
        """
        pass
    
    @property
    def markerColor(self) -> FloatVector:
        """
        A RGBA color specified by a debug marker call.
        
        :type: FloatVector
        """
        pass
    
    @markerColor.setter
    def markerColor(self, value: FloatVector):
        pass
    
    @property
    def numInstances(self) -> int:
        """
        The number of instances for a draw action. 0 if not used.
        
        :type: int
        """
        pass
    
    @numInstances.setter
    def numInstances(self, value: int):
        pass
    
    @property
    def actionId(self) -> int:
        """
        A 1-based index of this action relative to other actions.
        
        :type: int
        """
        pass
    
    @actionId.setter
    def actionId(self, value: int):
        pass
    
    @property
    def dispatchDimension(self) -> Tuple[int, int, int]:
        """
        The 3D number of workgroups to dispatch in a dispatch call.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @dispatchDimension.setter
    def dispatchDimension(self, value: Tuple[int, int, int]):
        pass
    
    @property
    def dispatchThreadsDimension(self) -> Tuple[int, int, int]:
        """
        The 3D size of each workgroup in threads if the call allows an override, or 0 if not.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @dispatchThreadsDimension.setter
    def dispatchThreadsDimension(self, value: Tuple[int, int, int]):
        pass
    
    @property
    def dispatchBase(self) -> Tuple[int, int, int]:
        """
        The 3D base offset of the workgroup ID if the call allows an override, or 0 if not.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @dispatchBase.setter
    def dispatchBase(self, value: Tuple[int, int, int]):
        pass
    
    @property
    def baseVertex(self) -> int:
        """
        For indexed drawcalls, the offset added to each index after fetching.
        
        :type: int
        """
        pass
    
    @baseVertex.setter
    def baseVertex(self, value: int):
        pass
    
    @property
    def customName(self) -> str:
        """
        The custom name of this action.
        
        For markers this will be a user-provided string. In most other cases this will be empty, and the
        name can be generated using structured data. The last listed event in :data:`events` will correspond
        to the event for the overall action, and its chunk will contain a name and any parameters.
        
        Some actions will have a custom name generated for e.g. reading back and directly displaying
        indirect parameters or render pass parameters.
        
        :type: str
        """
        pass
    
    @customName.setter
    def customName(self, value: str):
        pass
    
    @property
    def drawIndex(self) -> int:
        """
        The index of this action in an call with multiple draws, e.g. an indirect action.
        
        0 if not part of a multi-action.
        
        :type: int
        """
        pass
    
    @drawIndex.setter
    def drawIndex(self, value: int):
        pass
    
    @property
    def eventId(self) -> int:
        """
        The :data:`eventId <APIEvent.eventId>` that actually produced the action.
        
        :type: int
        """
        pass
    
    @eventId.setter
    def eventId(self, value: int):
        pass
    
    @property
    def copyDestination(self) -> ResourceId:
        """
        The :class:`ResourceId` identifying the destination object in a copy, resolve or blit
        operation.
        
        :type: ResourceId
        """
        pass
    
    @copyDestination.setter
    def copyDestination(self, value: ResourceId):
        pass
    
    @property
    def numIndices(self) -> int:
        """
        The number of indices or vertices as appropriate for a draw action. 0 if not used.
        
        :type: int
        """
        pass
    
    @numIndices.setter
    def numIndices(self, value: int):
        pass
    
    @property
    def instanceOffset(self) -> int:
        """
        For instanced drawcalls, the offset applied before looking up instanced vertex inputs.
        
        :type: int
        """
        pass
    
    @instanceOffset.setter
    def instanceOffset(self, value: int):
        pass
    
    @property
    def copySource(self) -> ResourceId:
        """
        The :class:`ResourceId` identifying the source object in a copy, resolve or blit
        operation.
        
        :type: ResourceId
        """
        pass
    
    @copySource.setter
    def copySource(self, value: ResourceId):
        pass
    
    @property
    def previousAction(self) -> 'ActionDescription':
        """
        The previous action in the frame, or ``None`` if this is the first action in the
        frame.
        
        :type: ActionDescription
        """
        pass
    
    @previousAction.setter
    def previousAction(self, value: 'ActionDescription'):
        pass
    
    @property
    def outputs(self) -> Tuple[ResourceId, ...]:
        """
        An 8-tuple of the :class:`ResourceId` ids for the color outputs, which can be used
        for very coarse bucketing of actions into similar passes by their outputs.
        
        :type: Tuple[ResourceId,...]
        """
        pass
    
    @outputs.setter
    def outputs(self, value: Tuple[ResourceId, ...]):
        pass
    
    @property
    def flags(self) -> ActionFlags:
        """
        A set of :class:`ActionFlags` properties describing what kind of action this is.
        
        :type: ActionFlags
        """
        pass
    
    @flags.setter
    def flags(self, value: ActionFlags):
        pass
    
    @property
    def indexOffset(self) -> int:
        """
        For indexed drawcalls, the first index to fetch from the index buffer.
        
        :type: int
        """
        pass
    
    @indexOffset.setter
    def indexOffset(self, value: int):
        pass
    
    @property
    def vertexOffset(self) -> int:
        """
        For non-indexed drawcalls, the offset applied before looking up each vertex input.
        
        :type: int
        """
        pass
    
    @vertexOffset.setter
    def vertexOffset(self, value: int):
        pass
    
    @property
    def copySourceSubresource(self) -> Subresource:
        """
        Which part of :data:`copySource` is used.
        
        :type: Subresource
        """
        pass
    
    @copySourceSubresource.setter
    def copySourceSubresource(self, value: Subresource):
        pass
    
    @property
    def copyDestinationSubresource(self) -> Subresource:
        """
        Which part of :data:`copyDestination` is used.
        
        :type: Subresource
        """
        pass
    
    @copyDestinationSubresource.setter
    def copyDestinationSubresource(self, value: Subresource):
        pass
    
    @property
    def depthOut(self) -> ResourceId:
        """
        The resource used for depth output - see :data:`outputs`.
        
        :type: ResourceId
        """
        pass
    
    @depthOut.setter
    def depthOut(self, value: ResourceId):
        pass
    
    @property
    def nextAction(self) -> 'ActionDescription':
        """
        The next action in the frame, or ``None`` if this is the last action in the frame.
        
        :type: ActionDescription
        """
        pass
    
    @nextAction.setter
    def nextAction(self, value: 'ActionDescription'):
        pass
    
    @property
    def children(self) -> List['ActionDescription']:
        """
        The child actions below this one, if it's a marker region or multi-action.
        
        :type: List[ActionDescription]
        """
        pass
    
    @children.setter
    def children(self, value: List['ActionDescription']):
        pass
    
    @property
    def events(self) -> List[APIEvent]:
        """
        The events that happened since the previous action.
        
        :type: List[APIEvent]
        """
        pass
    
    @events.setter
    def events(self, value: List[APIEvent]):
        pass
    
    @property
    def parent(self) -> 'ActionDescription':
        """
        The parent of this action, or ``None`` if there is no parent for this action.
        
        :type: ActionDescription
        """
        pass
    
    @parent.setter
    def parent(self, value: 'ActionDescription'):
        pass
    
