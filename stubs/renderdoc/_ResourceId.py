from typing import overload

class ResourceId():
    # Original docstring
    """
    This is an opaque identifier that uniquely locates a resource.
    
    .. note::
      These IDs do not overlap ever - textures, buffers, shaders and samplers will all have unique IDs
      and do not reuse the namespace. The IDs assigned for resources during capture are also used
      during replay. Any internal/synthesised resources created during replay will have distinct IDs.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ResourceId.
        """
        pass
    
    @overload
    def __init__(self, other: 'ResourceId'):
        """
        Construct a new ResourceId with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    @staticmethod
    def Null() -> 'ResourceId':
        """
        A helper function that explicitly creates an empty/invalid/null :class:`ResourceId`.
        
        :return: an empty/invalid/null :class:`ResourceId`.
        :rtype: ResourceId
        """
        pass
    
