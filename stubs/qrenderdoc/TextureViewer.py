# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .FollowType import FollowType

from renderdoc.CompType import CompType

from renderdoc.DebugOverlay import DebugOverlay

from renderdoc.ResourceId import ResourceId

from renderdoc.ShaderStage import ShaderStage

from renderdoc.Subresource import Subresource

class TextureViewer(): # skipped bases: <class 'SwigPyObject'>
    """
    The texture viewer window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetTextureViewer`.
    """
    def GetChannelVisibilityBits(self) -> int: # real signature unknown; restored from __doc__
        """
        GetChannelVisibilityBits()
        
        Return which channels are currently displayed, as a bitmask.
        
        If red is visible ``0x1`` will be set in the returned value, if blue is visible ``0x2`` will be set,
        etc.
        
        :return: The current bitmask showing channel visibility.
        :rtype: int
        """
        pass

    def GetCurrentResource(self) -> ResourceId: # real signature unknown; restored from __doc__
        """
        GetCurrentResource()
        
        Return which resource is currently being displayed in the active tab.
        
        :return: The ID of the resource being displayed.
        :rtype: renderdoc.ResourceId
        """
        pass

    def GetHistogramRange(self) -> Tuple[float,float]: # real signature unknown; restored from __doc__
        """
        GetHistogramRange()
        
        Return the current histogram blackpoint to whitepoint range.
        
        :return: The current histogram range.
        :rtype: Tuple[float,float]
        """
        pass

    def GetPickedLocation(self) -> Tuple[int,int]: # real signature unknown; restored from __doc__
        """
        GetPickedLocation()
        
        Returns the currently selected texel location in the current texture.
        
        If no location is currently selected or there is no current texture, this will return ``(-1, -1)``.
        
        :return: The currently picked pixel location.
        :rtype: Tuple[int,int]
        """
        pass

    def GetSelectedSubresource(self) -> Subresource: # real signature unknown; restored from __doc__
        """
        GetSelectedSubresource()
        
        Return which subresource is currently selected for viewing.
        
        :return: The subresource currently selected.
        :rtype: renderdoc.Subresource
        """
        pass

    def GetTextureOverlay(self) -> DebugOverlay: # real signature unknown; restored from __doc__
        """
        GetTextureOverlay()
        
        Return the currently selected texture overlay.
        
        :return: The currently selected texture overlay.
        :rtype: renderdoc.DebugOverlay
        """
        pass

    def GetZoomLevel(self) -> float: # real signature unknown; restored from __doc__
        """
        GetZoomLevel()
        
        Return the current zoom level, whether manually set or auto-calculated.
        
        :return: The current zoom level, with 100% being represented as 1.0.
        :rtype: float
        """
        pass

    def GotoLocation(self, x: int, y: int): # real signature unknown; restored from __doc__
        """
        GotoLocation(x, y)
        
        Highlights the given pixel location in the current texture.
        
        :param int x: The X co-ordinate.
        :param int y: The Y co-ordinate.
        """
        pass

    def IsZoomAutoFit(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsZoomAutoFit()
        
        Return whether or not the texture viewer is currently auto-fitting the zoom level.
        
        :return: ``True`` if the zoom level is currently auto-fitting.
        :rtype: bool
        """
        pass

    def SetChannelVisibility(self, red: bool, green: bool, blue: bool, alpha: bool): # real signature unknown; restored from __doc__
        """
        SetChannelVisibility(red, green, blue, alpha)
        
        Set the visibility of each channel.
        
        :param bool red: Whether the red channel should be visible.
        :param bool green: Whether the green channel should be visible.
        :param bool blue: Whether the blue channel should be visible.
        :param bool alpha: Whether the alpha channel should be visible.
        """
        pass

    def SetHistogramRange(self, blackpoint: float, whitepoint: float): # real signature unknown; restored from __doc__
        """
        SetHistogramRange(blackpoint, whitepoint)
        
        Set the current histogram blackpoint to whitepoint range.
        
        :param float blackpoint: The value that should be mapped to black, component-wise.
        :param float whitepoint: The value that should be mapped to white, component-wise.
        """
        pass

    def SetSelectedSubresource(self, sub: Subresource): # real signature unknown; restored from __doc__
        """
        SetSelectedSubresource(sub)
        
        Select a particular subresource within the currently selected texture. Any out of
        bounds parameters will be clamped to the available subresources.
        
        :param renderdoc.Subresource sub: The subresource to select.
        """
        pass

    def SetTextureOverlay(self, overlay: DebugOverlay): # real signature unknown; restored from __doc__
        """
        SetTextureOverlay(overlay)
        
        Changes the currently selected overlay the given pixel location in the current texture.
        
        :param renderdoc.DebugOverlay overlay: The overlay to enable.
        """
        pass

    def SetZoomLevel(self, autofit: bool, zoom: float): # real signature unknown; restored from __doc__
        """
        SetZoomLevel(autofit, zoom)
        
        Set the zoom level for displaying textures.
        
        :param bool autofit: ``True`` if the zoom level should be auto-calculated continuously to
          automatically fit the texture completely in view.
        :param float zoom: The zoom level as a percentage, with 100% being 1.0. Ignored if
          :paramref:`autofit` is ``True``.
        """
        pass

    def ViewFollowedResource(self, followType: FollowType, stage: ShaderStage, index: int, arrayElement: int): # real signature unknown; restored from __doc__
        """
        ViewFollowedResource(followType, stage, index, arrayElement)
        
        Select the 'following' view and choose which resource slot to follow.
        
        :param FollowType followType: The type of followed resource.
        :param renderdoc.ShaderStage stage: The shader stage of the shader reflection data to look up.
        :param int index: The index within the given resource list (if applicable) to follow.
        :param int arrayElement: The index within the given resource array (if applicable) to follow.
        """
        pass

    def ViewTexture(self, resourceId: ResourceId, typeCast: CompType, focus: bool): # real signature unknown; restored from __doc__
        """
        ViewTexture(resourceId, typeCast, focus)
        
        Open a texture view, optionally raising this window to the foreground.
        
        :param renderdoc.ResourceId resourceId: The ID of the texture to view.
        :param renderdoc.CompType typeCast: If possible interpret the texture with this type instead of its
          normal type. If set to :data:`~renderdoc.CompType.Typeless` then no cast is applied, otherwise
          where allowed the texture data will be reinterpreted - e.g. from unsigned integers to floats, or
          to unsigned normalised values.
        :param bool focus: ``True`` if the :class:`TextureViewer` should be raised.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`TextureViewer` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50138F80>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.TextureViewer' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.TextureViewer' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.TextureViewer' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.TextureViewer' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.TextureViewer' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.TextureViewer' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.TextureViewer' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.TextureViewer' objects>, 'Widget': <method 'Widget' of 'qrenderdoc.TextureViewer' objects>, 'ViewTexture': <method 'ViewTexture' of 'qrenderdoc.TextureViewer' objects>, 'ViewFollowedResource': <method 'ViewFollowedResource' of 'qrenderdoc.TextureViewer' objects>, 'GetCurrentResource': <method 'GetCurrentResource' of 'qrenderdoc.TextureViewer' objects>, 'GetSelectedSubresource': <method 'GetSelectedSubresource' of 'qrenderdoc.TextureViewer' objects>, 'SetSelectedSubresource': <method 'SetSelectedSubresource' of 'qrenderdoc.TextureViewer' objects>, 'GotoLocation': <method 'GotoLocation' of 'qrenderdoc.TextureViewer' objects>, 'GetPickedLocation': <method 'GetPickedLocation' of 'qrenderdoc.TextureViewer' objects>, 'GetTextureOverlay': <method 'GetTextureOverlay' of 'qrenderdoc.TextureViewer' objects>, 'SetTextureOverlay': <method 'SetTextureOverlay' of 'qrenderdoc.TextureViewer' objects>, 'IsZoomAutoFit': <method 'IsZoomAutoFit' of 'qrenderdoc.TextureViewer' objects>, 'GetZoomLevel': <method 'GetZoomLevel' of 'qrenderdoc.TextureViewer' objects>, 'SetZoomLevel': <method 'SetZoomLevel' of 'qrenderdoc.TextureViewer' objects>, 'GetHistogramRange': <method 'GetHistogramRange' of 'qrenderdoc.TextureViewer' objects>, 'SetHistogramRange': <method 'SetHistogramRange' of 'qrenderdoc.TextureViewer' objects>, 'GetChannelVisibilityBits': <method 'GetChannelVisibilityBits' of 'qrenderdoc.TextureViewer' objects>, 'SetChannelVisibility': <method 'SetChannelVisibility' of 'qrenderdoc.TextureViewer' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.TextureViewer' objects>, '__doc__': '\\nThe texture viewer window.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetTextureViewer`.\\n\\n'})"


