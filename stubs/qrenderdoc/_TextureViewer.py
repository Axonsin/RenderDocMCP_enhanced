from ._FollowType import FollowType
from renderdoc import CompType, DebugOverlay, ResourceId, ShaderStage, Subresource, TextureDisplay
from typing import Tuple

# Dummy types
from . import QWidget

class TextureViewer():
    # Original docstring
    """
    The texture viewer window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetTextureViewer`.
    """
    
    
    
    def Widget(self) -> QWidget:
        """
        Retrieves the PySide2 QWidget for this :class:`TextureViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
        """
        pass
    
    
    def ViewTexture(self, resourceId: ResourceId, typeCast: CompType, focus: bool):
        """
        Open a texture view, optionally raising this window to the foreground.
        
        :param renderdoc.ResourceId resourceId: The ID of the texture to view.
        :param renderdoc.CompType typeCast: If possible interpret the texture with this type instead of its
          normal type. If set to :data:`~renderdoc.CompType.Typeless` then no cast is applied, otherwise
          where allowed the texture data will be reinterpreted - e.g. from unsigned integers to floats, or
          to unsigned normalised values.
        :param bool focus: ``True`` if the :class:`TextureViewer` should be raised.
        """
        pass
    
    
    def ViewFollowedResource(self, followType: FollowType, stage: ShaderStage, index: int, arrayElement: int):
        """
        Select the 'following' view and choose which resource slot to follow.
        
        :param FollowType followType: The type of followed resource.
        :param renderdoc.ShaderStage stage: The shader stage of the shader reflection data to look up.
        :param int index: The index within the given resource list (if applicable) to follow.
        :param int arrayElement: The index within the given resource array (if applicable) to follow.
        """
        pass
    
    
    def GetCurrentResource(self) -> ResourceId:
        """
        Return which resource is currently being displayed in the active tab.
        
        :return: The ID of the resource being displayed.
        :rtype: renderdoc.ResourceId
        """
        pass
    
    
    def GetSelectedSubresource(self) -> Subresource:
        """
        Return which subresource is currently selected for viewing.
        
        :return: The subresource currently selected.
        :rtype: renderdoc.Subresource
        """
        pass
    
    
    def SetSelectedSubresource(self, sub: Subresource):
        """
        Select a particular subresource within the currently selected texture. Any out of
        bounds parameters will be clamped to the available subresources.
        
        :param renderdoc.Subresource sub: The subresource to select.
        """
        pass
    
    
    def GotoLocation(self, x: int, y: int):
        """
        Highlights the given pixel location in the current texture.
        
        :param int x: The X co-ordinate.
        :param int y: The Y co-ordinate.
        """
        pass
    
    
    def GetPickedLocation(self) -> Tuple[int, int]:
        """
        Returns the currently selected texel location in the current texture.
        
        If no location is currently selected or there is no current texture, this will return ``(-1, -1)``.
        
        :return: The currently picked pixel location.
        :rtype: Tuple[int,int]
        """
        pass
    
    
    def GetTextureOverlay(self) -> DebugOverlay:
        """
        Return the currently selected texture overlay.
        
        :return: The currently selected texture overlay.
        :rtype: renderdoc.DebugOverlay
        """
        pass
    
    
    def SetTextureOverlay(self, overlay: DebugOverlay):
        """
        Changes the currently selected overlay the given pixel location in the current texture.
        
        :param renderdoc.DebugOverlay overlay: The overlay to enable.
        """
        pass
    
    
    def IsZoomAutoFit(self) -> bool:
        """
        Return whether or not the texture viewer is currently auto-fitting the zoom level.
        
        :return: ``True`` if the zoom level is currently auto-fitting.
        :rtype: bool
        """
        pass
    
    
    def GetTextureDisplay(self) -> TextureDisplay:
        """
        Return the currently configured texture display structure.
        
        :return: The current texture display.
        :rtype: renderdoc.TextureDisplay
        """
        pass
    
    
    def GetZoomLevel(self) -> float:
        """
        Return the current zoom level, whether manually set or auto-calculated.
        
        :return: The current zoom level, with 100% being represented as 1.0.
        :rtype: float
        """
        pass
    
    
    def SetZoomLevel(self, autofit: bool, zoom: float):
        """
        Set the zoom level for displaying textures.
        
        :param bool autofit: ``True`` if the zoom level should be auto-calculated continuously to
          automatically fit the texture completely in view.
        :param float zoom: The zoom level as a percentage, with 100% being 1.0. Ignored if
          :paramref:`SetZoomLevel.autofit` is ``True``.
        """
        pass
    
    
    def GetHistogramRange(self) -> Tuple[float, float]:
        """
        Return the current histogram blackpoint to whitepoint range.
        
        :return: The current histogram range.
        :rtype: Tuple[float,float]
        """
        pass
    
    
    def SetHistogramRange(self, blackpoint: float, whitepoint: float):
        """
        Set the current histogram blackpoint to whitepoint range.
        
        :param float blackpoint: The value that should be mapped to black, component-wise.
        :param float whitepoint: The value that should be mapped to white, component-wise.
        """
        pass
    
    
    def GetChannelVisibilityBits(self) -> int:
        """
        Return which channels are currently displayed, as a bitmask.
        
        If red is visible ``0x1`` will be set in the returned value, if blue is visible ``0x2`` will be set,
        etc.
        
        :return: The current bitmask showing channel visibility.
        :rtype: int
        """
        pass
    
    
    def GetChannelVisibility(self) -> Tuple[bool, bool, bool, bool]:
        """
        Return which channels are currently displayed, as a four-component tuple.
        
        :return: The current channel visibility per component.
        :rtype: Tuple[bool,bool,bool,bool]
        """
        pass
    
    
    def SetChannelVisibility(self, red: bool, green: bool, blue: bool, alpha: bool):
        """
        Set the visibility of each channel.
        
        :param bool red: Whether the red channel should be visible.
        :param bool green: Whether the green channel should be visible.
        :param bool blue: Whether the blue channel should be visible.
        :param bool alpha: Whether the alpha channel should be visible.
        """
        pass
    
