from typing import Tuple

from typing import overload

class ShaderMeshMessageLocation():
    # Original docstring
    """
    A task or mesh message's location.
    
    .. data:: NotUsed
    
      Set for values of task group/thread index when no task shaders were run.
    
      Also set for values of a mesh group or thread index when that dimensionality is unused. For
      example if the shader declares a group dimension of (128,1,1) then the y and z values for
      thread index will be indicated as not used.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderMeshMessageLocation.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderMeshMessageLocation'):
        """
        Construct a new ShaderMeshMessageLocation with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    NotUsed = 4294967295
    """
    Set for values of task group/thread index when no task shaders were run.
    
    Also set for values of a mesh group or thread index when that dimensionality is unused. For
    example if the shader declares a group dimension of (128,1,1) then the y and z values for
    thread index will be indicated as not used.
    """
    
    @property
    def meshGroup(self) -> Tuple[int, int, int]:
        """
        The mesh workgroup index within the dispatch or launching task workgroup.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @meshGroup.setter
    def meshGroup(self, value: Tuple[int, int, int]):
        pass
    
    @property
    def taskGroup(self) -> Tuple[int, int, int]:
        """
        The task workgroup index between the task dispatch.
        
        .. note::
          If no task shader is in use, this will be :data:`NotUsed`, :data:`NotUsed`, :data:`NotUsed`.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @taskGroup.setter
    def taskGroup(self, value: Tuple[int, int, int]):
        pass
    
    @property
    def thread(self) -> Tuple[int, int, int]:
        """
        The thread index within the workgroup, either for a task shader or mesh shader.
        
        .. note::
          Since task shaders can only emit one set of meshes per group, the task thread is not relevant
          for mesh shader messages, so this is the thread either for a task or a mesh shader message.
        
        :type: Tuple[int,int,int]
        """
        pass
    
    @thread.setter
    def thread(self, value: Tuple[int, int, int]):
        pass
    
