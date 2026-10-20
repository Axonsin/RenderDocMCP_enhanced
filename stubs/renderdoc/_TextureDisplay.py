from ._CompType import CompType
from ._DebugOverlay import DebugOverlay
from ._FloatVector import FloatVector
from ._ResourceId import ResourceId
from ._Subresource import Subresource

from typing import overload

class TextureDisplay():
    # Original docstring
    """
    Describes how to render a texture preview of an image. Describes the zoom and pan settings for the
    texture when rendering on a particular output, as well as the modification and selection of a
    particular subresource (such as array slice, mip or multi-sampled sample).
    
    .. note::
      X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
      APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
      fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
      bottom-left co-ordinates, care must be taken to translate them.
    
    .. data:: ResolveSamples
    
      Value for :data:`Subresource.sample` if the samples should be averaged.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised TextureDisplay.
        """
        pass
    
    @overload
    def __init__(self, other: 'TextureDisplay'):
        """
        Construct a new TextureDisplay with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    ResolveSamples = 4294967295
    """
    Value for :data:`Subresource.sample` if the samples should be averaged.
    """
    
    @property
    def backgroundColor(self) -> FloatVector:
        """
        The background color to use behind the texture display.
        
        If set to (0, 0, 0, 0) the global checkerboard colors are used.
        
        :type: FloatVector
        """
        pass
    
    @backgroundColor.setter
    def backgroundColor(self, value: FloatVector):
        pass
    
    @property
    def overlay(self) -> DebugOverlay:
        """
        Selects a :class:`DebugOverlay` to draw over the top of the texture.
        
        :type: DebugOverlay
        """
        pass
    
    @overlay.setter
    def overlay(self, value: DebugOverlay):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the texture to display.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def rangeMin(self) -> float:
        """
        The value in each channel to map to the black point.
        
        :type: float
        """
        pass
    
    @rangeMin.setter
    def rangeMin(self, value: float):
        pass
    
    @property
    def alpha(self) -> bool:
        """
        ``True`` if the alpha channel should be visible. If enabled with any of RGB, the
        texture will be blended to the background color or checkerboard.
        
        If only one channel is selected, it will be rendered in grayscale
        
        :type: bool
        """
        pass
    
    @alpha.setter
    def alpha(self, value: bool):
        pass
    
    @property
    def decodeYUV(self) -> bool:
        """
        ``True`` if the texture should be decoded as if it contains YUV data.
        
        :type: bool
        """
        pass
    
    @decodeYUV.setter
    def decodeYUV(self, value: bool):
        pass
    
    @property
    def blue(self) -> bool:
        """
        ``True`` if the blue channel should be visible.
        
        If only one channel is selected, it will be rendered in grayscale
        
        :type: bool
        """
        pass
    
    @blue.setter
    def blue(self, value: bool):
        pass
    
    @property
    def rawOutput(self) -> bool:
        """
        ``True`` if the rendered image should be as close as possible in value to the input.
        
        This is primarily useful when rendering to a floating point target for retrieving pixel data from
        the input texture in cases where it isn't easy to directly fetch the input texture data.
        
        :type: bool
        """
        pass
    
    @rawOutput.setter
    def rawOutput(self, value: bool):
        pass
    
    @property
    def typeCast(self) -> CompType:
        """
        If possible interpret the texture with this type instead of its normal type.
        
        If set to :data:`CompType.Typeless` then no cast is applied, otherwise where allowed the texture
        data will be reinterpreted - e.g. from unsigned integers to floats, or to unsigned normalised
        values.
        
        :type: CompType
        """
        pass
    
    @typeCast.setter
    def typeCast(self, value: CompType):
        pass
    
    @property
    def yOffset(self) -> float:
        """
        The offset to pan in the Y axis.
        
        :type: float
        """
        pass
    
    @yOffset.setter
    def yOffset(self, value: float):
        pass
    
    @property
    def customShaderId(self) -> ResourceId:
        """
        The :class:`ResourceId` of a custom shader to use when rendering.
        
        See :meth:`ReplayController.BuildCustomShader` for creating an appropriate custom shader.
        
        :type: ResourceId
        """
        pass
    
    @customShaderId.setter
    def customShaderId(self, value: ResourceId):
        pass
    
    @property
    def green(self) -> bool:
        """
        ``True`` if the green channel should be visible.
        
        If only one channel is selected, it will be rendered in grayscale
        
        :type: bool
        """
        pass
    
    @green.setter
    def green(self, value: bool):
        pass
    
    @property
    def scale(self) -> float:
        """
        The scale to apply to the texture when rendering as a floating point value.
        
        ``1.0`` corresponds to ``100%``
        
        :type: float
        """
        pass
    
    @scale.setter
    def scale(self, value: float):
        pass
    
    @property
    def subresource(self) -> Subresource:
        """
        The subresource of the texture to display.
        
        If the :data:`Subresource.sample` member is set to :data:`ResolveSamples` then a default resolve
        will be performed that averages all samples.
        
        :type: Subresource
        """
        pass
    
    @subresource.setter
    def subresource(self, value: Subresource):
        pass
    
    @property
    def xOffset(self) -> float:
        """
        The offset to pan in the X axis.
        
        :type: float
        """
        pass
    
    @xOffset.setter
    def xOffset(self, value: float):
        pass
    
    @property
    def rangeMax(self) -> float:
        """
        The value in each channel to map to the white point.
        
        :type: float
        """
        pass
    
    @rangeMax.setter
    def rangeMax(self, value: float):
        pass
    
    @property
    def red(self) -> bool:
        """
        ``True`` if the red channel should be visible.
        
        If only one channel is selected, it will be rendered in grayscale
        
        :type: bool
        """
        pass
    
    @red.setter
    def red(self, value: bool):
        pass
    
    @property
    def flipY(self) -> bool:
        """
        ``True`` if the texture should be flipped vertically when rendering.
        
        :type: bool
        """
        pass
    
    @flipY.setter
    def flipY(self, value: bool):
        pass
    
    @property
    def hdrMultiplier(self) -> float:
        """
        If ``>= 0.0`` the RGBA values will be viewed as HDRM with this as the multiplier.
        
        :type: float
        """
        pass
    
    @hdrMultiplier.setter
    def hdrMultiplier(self, value: float):
        pass
    
    @property
    def linearDisplayAsGamma(self) -> bool:
        """
        ``True`` if the texture should be interpreted as gamma.
        
        See :ref:`the FAQ entry <gamma-linear-display>`.
        
        :type: bool
        """
        pass
    
    @linearDisplayAsGamma.setter
    def linearDisplayAsGamma(self, value: bool):
        pass
    
