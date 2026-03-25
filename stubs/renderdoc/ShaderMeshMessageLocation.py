# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderMeshMessageLocation(): # skipped bases: <class 'SwigPyObject'>
    """
    A task or mesh message's location.
    
    .. data:: NotUsed
    
      Set for values of task group/thread index when no task shaders were run.
    
      Also set for values of a mesh group or thread index when that dimensionality is unused. For
      example if the shader declares a group dimension of (128,1,1) then the y and z values for
      thread index will be indicated as not used.
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
    def meshGroup(self) -> Tuple[int,int,int]:
        """
The mesh workgroup index within the dispatch or launching task workgroup.

:type: Tuple[int,int,int]

"""
        pass

    @meshGroup.setter
    def meshGroup(self, value: Tuple[int,int,int]):
        pass

    @property
    def taskGroup(self) -> Tuple[int,int,int]:
        """
The task workgroup index between the task dispatch.

.. note::
  If no task shader is in use, this will be :data:`NotUsed`, :data:`NotUsed`, :data:`NotUsed`.

:type: Tuple[int,int,int]

"""
        pass

    @taskGroup.setter
    def taskGroup(self, value: Tuple[int,int,int]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def thread(self) -> Tuple[int,int,int]:
        """
The thread index within the workgroup, either for a task shader or mesh shader.

.. note::
  Since task shaders can only emit one set of meshes per group, the task thread is not relevant
  for mesh shader messages, so this is the thread either for a task or a mesh shader message.

:type: Tuple[int,int,int]

"""
        pass

    @thread.setter
    def thread(self, value: Tuple[int,int,int]):
        pass


    NotUsed = 4294967295
    __dict__ = None # (!) real value is 'mappingproxy({\'NotUsed\': 4294967295, \'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D6250>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'meshGroup\': <attribute \'meshGroup\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'taskGroup\': <attribute \'taskGroup\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'thread\': <attribute \'thread\' of \'renderdoc.ShaderMeshMessageLocation\' objects>, \'__doc__\': "\\nA task or mesh message\'s location.\\n\\n.. data:: NotUsed\\n\\n  Set for values of task group/thread index when no task shaders were run.\\n\\n  Also set for values of a mesh group or thread index when that dimensionality is unused. For\\n  example if the shader declares a group dimension of (128,1,1) then the y and z values for\\n  thread index will be indicated as not used.\\n\\n"})'


