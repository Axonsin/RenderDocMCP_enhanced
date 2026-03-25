# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .FloatVector import FloatVector
from .ResourceId import ResourceId
from .DebugOverlay import DebugOverlay
from .Subresource import Subresource
from .CompType import CompType

class TextureDisplay(): # skipped bases: <class 'SwigPyObject'>
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
    
      Value for :data:`sampleIdx` if the samples should be averaged.
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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
    def yOffset(self) -> float:
        """
The offset to pan in the Y axis.

:type: float

"""
        pass

    @yOffset.setter
    def yOffset(self, value: float):
        pass


    ResolveSamples = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'ResolveSamples': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551C7A50>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.TextureDisplay' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.TextureDisplay' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.TextureDisplay' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.TextureDisplay' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.TextureDisplay' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.TextureDisplay' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.TextureDisplay' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.TextureDisplay' objects>, 'backgroundColor': <attribute 'backgroundColor' of 'renderdoc.TextureDisplay' objects>, 'overlay': <attribute 'overlay' of 'renderdoc.TextureDisplay' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.TextureDisplay' objects>, 'rangeMin': <attribute 'rangeMin' of 'renderdoc.TextureDisplay' objects>, 'alpha': <attribute 'alpha' of 'renderdoc.TextureDisplay' objects>, 'decodeYUV': <attribute 'decodeYUV' of 'renderdoc.TextureDisplay' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.TextureDisplay' objects>, 'blue': <attribute 'blue' of 'renderdoc.TextureDisplay' objects>, 'rawOutput': <attribute 'rawOutput' of 'renderdoc.TextureDisplay' objects>, 'typeCast': <attribute 'typeCast' of 'renderdoc.TextureDisplay' objects>, 'yOffset': <attribute 'yOffset' of 'renderdoc.TextureDisplay' objects>, 'customShaderId': <attribute 'customShaderId' of 'renderdoc.TextureDisplay' objects>, 'green': <attribute 'green' of 'renderdoc.TextureDisplay' objects>, 'scale': <attribute 'scale' of 'renderdoc.TextureDisplay' objects>, 'subresource': <attribute 'subresource' of 'renderdoc.TextureDisplay' objects>, 'xOffset': <attribute 'xOffset' of 'renderdoc.TextureDisplay' objects>, 'rangeMax': <attribute 'rangeMax' of 'renderdoc.TextureDisplay' objects>, 'red': <attribute 'red' of 'renderdoc.TextureDisplay' objects>, 'flipY': <attribute 'flipY' of 'renderdoc.TextureDisplay' objects>, 'hdrMultiplier': <attribute 'hdrMultiplier' of 'renderdoc.TextureDisplay' objects>, 'linearDisplayAsGamma': <attribute 'linearDisplayAsGamma' of 'renderdoc.TextureDisplay' objects>, '__doc__': '\\n\\nDescribes how to render a texture preview of an image. Describes the zoom and pan settings for the\\ntexture when rendering on a particular output, as well as the modification and selection of a\\nparticular subresource (such as array slice, mip or multi-sampled sample).\\n\\n.. note::\\n  X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between\\n  APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are\\n  fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in\\n  bottom-left co-ordinates, care must be taken to translate them.\\n\\n.. data:: ResolveSamples\\n\\n  Value for :data:`sampleIdx` if the samples should be averaged.\\n\\n'})"


