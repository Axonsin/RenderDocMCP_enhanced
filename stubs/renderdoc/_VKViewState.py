from ._VKRenderArea import VKRenderArea
from ._VKViewportScissor import VKViewportScissor
from typing import List

from typing import overload

class VKViewState():
    # Original docstring
    """
    Describes the view state in the pipeline.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKViewState.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKViewState'):
        """
        Construct a new VKViewState with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def discardRectanglesExclusive(self) -> bool:
        """
        ``True`` if a fragment in any one of the discard rectangles fails the discard test,
        and a fragment in none of them passes.
        
        ``False`` if a fragment in any one of the discard rectangles passes the discard test,
        and a fragment in none of them is discarded.
        
        .. note::
          A ``True`` value and an empty list of :data:`discardRectangles` means the test is effectively
          disabled, since with no rectangles no fragment can be inside one.
        
        :type: bool
        """
        pass
    
    @discardRectanglesExclusive.setter
    def discardRectanglesExclusive(self, value: bool):
        pass
    
    @property
    def discardRectangles(self) -> List[VKRenderArea]:
        """
        The discard rectangles, if enabled.
        
        :type: List[VKRenderArea]
        """
        pass
    
    @discardRectangles.setter
    def discardRectangles(self, value: List[VKRenderArea]):
        pass
    
    @property
    def viewportScissors(self) -> List[VKViewportScissor]:
        """
        The bound viewports and scissors.
        
        :type: List[VKViewportScissor]
        """
        pass
    
    @viewportScissors.setter
    def viewportScissors(self, value: List[VKViewportScissor]):
        pass
    
    @property
    def depthNegativeOneToOne(self) -> bool:
        """
        Whether depth clip range is set to ``[-1, 1]`` through ``VK_EXT_depth_clip_control``.
        
        :type: bool
        """
        pass
    
    @depthNegativeOneToOne.setter
    def depthNegativeOneToOne(self, value: bool):
        pass
    
