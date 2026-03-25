# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .SDFile import SDFile
from .ResourceId import ResourceId
from .Subresource import Subresource
from .APIEvent import APIEvent
from .ActionFlags import ActionFlags
from .FloatVector import FloatVector

class ActionDescription(): # skipped bases: <class 'SwigPyObject'>
    """
    Describes the properties of an action.
    
    An action is a call such as a draw, a compute dispatch, clears, copies, resolves, etc. Any GPU event
    which may have deliberate visible side-effects to application-visible memory, typically resources
    such as textures and buffers. It also includes markers, which provide a user-generated annotation of
    events and actions.
    """
    def GetName(self, structuredFile: SDFile) -> str: # real signature unknown; restored from __doc__
        """
        GetName(structuredFile)
        
        Returns the name for this action, either from its custom name (see :data:`customName`)
        or from the matching chunk in the structured data passed in.
        
        :param SDFile structuredFile: The structured data file for the capture this action is from.
        :return: Returns the best available name for this action.
        :rtype: str
        """
        pass

    def IsFakeMarker(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsFakeMarker()
        
        Returns whether or not this action corresponds to a fake marker added by
        :meth:`ReplayController.AddFakeMarkers`.
        
        Such actions may break expectations of event IDs and action IDs, so it is recommended to avoid
        processing them wherever possible.
        
        :return: Returns whether or not this action is a fake marker.
        :rtype: bool
        """
        pass

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
    def children(self) -> 'List[ActionDescription]':
        """
The child actions below this one, if it's a marker region or multi-action.

:type: List[ActionDescription]

"""
        pass

    @children.setter
    def children(self, value: 'List[ActionDescription]'):
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
    def dispatchBase(self) -> Tuple[int,int,int]:
        """
The 3D base offset of the workgroup ID if the call allows an override, or 0 if not.

:type: Tuple[int,int,int]

"""
        pass

    @dispatchBase.setter
    def dispatchBase(self, value: Tuple[int,int,int]):
        pass

    @property
    def dispatchDimension(self) -> Tuple[int,int,int]:
        """
The 3D number of workgroups to dispatch in a dispatch call.

:type: Tuple[int,int,int]

"""
        pass

    @dispatchDimension.setter
    def dispatchDimension(self, value: Tuple[int,int,int]):
        pass

    @property
    def dispatchThreadsDimension(self) -> Tuple[int,int,int]:
        """
The 3D size of each workgroup in threads if the call allows an override, or 0 if not.

:type: Tuple[int,int,int]

"""
        pass

    @dispatchThreadsDimension.setter
    def dispatchThreadsDimension(self, value: Tuple[int,int,int]):
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
    def next(self) -> 'ActionDescription':
        """
The next action in the frame, or ``None`` if this is the last action in the frame.

:type: ActionDescription

"""
        pass

    @next.setter
    def next(self, value: 'ActionDescription'):
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
    def outputs(self) -> Tuple[ResourceId,...]:
        """
An 8-tuple of the :class:`ResourceId` ids for the color outputs, which can be used
for very coarse bucketing of actions into similar passes by their outputs.

:type: Tuple[ResourceId,...]

"""
        pass

    @outputs.setter
    def outputs(self, value: Tuple[ResourceId,...]):
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

    @property
    def previous(self) -> 'ActionDescription':
        """
The previous action in the frame, or ``None`` if this is the first action in the
frame.

:type: ActionDescription

"""
        pass

    @previous.setter
    def previous(self, value: 'ActionDescription'):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B6F80>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ActionDescription' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ActionDescription' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ActionDescription' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ActionDescription' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ActionDescription' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ActionDescription' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ActionDescription' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ActionDescription' objects>, 'IsFakeMarker': <method 'IsFakeMarker' of 'renderdoc.ActionDescription' objects>, 'GetName': <method 'GetName' of 'renderdoc.ActionDescription' objects>, 'markerColor': <attribute 'markerColor' of 'renderdoc.ActionDescription' objects>, 'numInstances': <attribute 'numInstances' of 'renderdoc.ActionDescription' objects>, 'actionId': <attribute 'actionId' of 'renderdoc.ActionDescription' objects>, 'dispatchDimension': <attribute 'dispatchDimension' of 'renderdoc.ActionDescription' objects>, 'dispatchThreadsDimension': <attribute 'dispatchThreadsDimension' of 'renderdoc.ActionDescription' objects>, 'previous': <attribute 'previous' of 'renderdoc.ActionDescription' objects>, 'dispatchBase': <attribute 'dispatchBase' of 'renderdoc.ActionDescription' objects>, 'baseVertex': <attribute 'baseVertex' of 'renderdoc.ActionDescription' objects>, 'customName': <attribute 'customName' of 'renderdoc.ActionDescription' objects>, 'drawIndex': <attribute 'drawIndex' of 'renderdoc.ActionDescription' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ActionDescription' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.ActionDescription' objects>, 'copyDestination': <attribute 'copyDestination' of 'renderdoc.ActionDescription' objects>, 'numIndices': <attribute 'numIndices' of 'renderdoc.ActionDescription' objects>, 'instanceOffset': <attribute 'instanceOffset' of 'renderdoc.ActionDescription' objects>, 'copySource': <attribute 'copySource' of 'renderdoc.ActionDescription' objects>, 'outputs': <attribute 'outputs' of 'renderdoc.ActionDescription' objects>, 'flags': <attribute 'flags' of 'renderdoc.ActionDescription' objects>, 'next': <attribute 'next' of 'renderdoc.ActionDescription' objects>, 'indexOffset': <attribute 'indexOffset' of 'renderdoc.ActionDescription' objects>, 'vertexOffset': <attribute 'vertexOffset' of 'renderdoc.ActionDescription' objects>, 'copySourceSubresource': <attribute 'copySourceSubresource' of 'renderdoc.ActionDescription' objects>, 'copyDestinationSubresource': <attribute 'copyDestinationSubresource' of 'renderdoc.ActionDescription' objects>, 'depthOut': <attribute 'depthOut' of 'renderdoc.ActionDescription' objects>, 'children': <attribute 'children' of 'renderdoc.ActionDescription' objects>, 'events': <attribute 'events' of 'renderdoc.ActionDescription' objects>, 'parent': <attribute 'parent' of 'renderdoc.ActionDescription' objects>, '__doc__': '\\nDescribes the properties of an action.\\n\\nAn action is a call such as a draw, a compute dispatch, clears, copies, resolves, etc. Any GPU event\\nwhich may have deliberate visible side-effects to application-visible memory, typically resources\\nsuch as textures and buffers. It also includes markers, which provide a user-generated annotation of\\nevents and actions.\\n\\n'})"


