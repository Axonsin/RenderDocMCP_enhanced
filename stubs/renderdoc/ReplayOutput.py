# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId
from .Subresource import Subresource
from .CompType import CompType
from .ResultDetails import ResultDetails
from .WindowingData import WindowingData
from .MeshDisplay import MeshDisplay
from .TextureDisplay import TextureDisplay

class ReplayOutput(): # skipped bases: <class 'SwigPyObject'>
    """
    A stateful output handle that contains the current configuration for one particular view
    of the capture. This allows multiple outputs to run independently without interfering with each
    other.
    
    The different types are enumerated in :class:`ReplayOutputType`.
    
    .. data:: NoResult
    
      No result was found in e.g. :meth:`PickVertex`.
    """
    def AddThumbnail(self, window: WindowingData, textureId: ResourceId, sub: Subresource, typeCast: CompType) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        AddThumbnail(window, textureId, sub, typeCast)
        
        Sets up a thumbnail for displaying a particular texture with sensible defaults.
        
        The window handle specified will be filled (in an aspect-ratio preserving way) with the texture.
        
        If the window specified has been used for a thumbnail before, then the texture will be updated but
        otherwise nothing will be created and the existing internal data will be reused. This means that
        you can call this function multiple times to just change the texture.
        
        Should only be called for texture outputs.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :param ResourceId textureId: The texture ID to display in the thumbnail preview.
        :param Subresource sub: The subresource within this texture to use.
        :param CompType typeCast: If possible interpret the texture with this type instead of its normal
          type. If set to :data:`CompType.Typeless` then no cast is applied, otherwise where allowed the
          texture data will be reinterpreted - e.g. from unsigned integers to floats, or to unsigned
          normalised values.
        :return: A result indicating if the thumbnail was successfully created.
        :rtype: ResultDetails
        """
        pass

    def ClearThumbnails(self): # real signature unknown; restored from __doc__
        """
        ClearThumbnails()
        
        Clear and release all thumbnails associated with this output. See :meth:`AddThumbnail`.
        """
        pass

    def DisablePixelContext(self): # real signature unknown; restored from __doc__
        """
        DisablePixelContext()
        
        Disable the pixel context view from rendering.
        """
        pass

    def Display(self): # real signature unknown; restored from __doc__
        """
        Display()
        
        Render to the window handle specified when the output was created.
        
        This will also render any thumbnails and the pixel context, if enabled.
        """
        pass

    def DrawThumbnail(self, width: int, height: int, textureId: ResourceId, sub: Subresource, typeCast: CompType) -> bytes: # real signature unknown; restored from __doc__
        """
        DrawThumbnail(width, height, textureId, sub, typeCast)
        
        Draws a thumbnail for a particular texture with sensible defaults and returns an RGBA8
        byte buffer for display. This does not render to a window but internally to a texture which is read
        back from the GPU.
        
        Should only be called for texture outputs.
        
        :param int width: The width of the desired thumbnail.
        :param int height: The height of the desired thumbnail.
        :param ResourceId textureId: The texture ID to display in the thumbnail preview.
        :param Subresource sub: The subresource within this texture to use.
        :param CompType typeCast: If possible interpret the texture with this type instead of its normal
          type. If set to :data:`CompType.Typeless` then no cast is applied, otherwise where allowed the
          texture data will be reinterpreted - e.g. from unsigned integers to floats, or to unsigned
          normalised values.
        :return: A buffer with the thumbnail RGBA8 data if successful, or empty if something went wrong.
        :rtype: bytes
        """
        pass

    def GetCustomShaderTexID(self) -> ResourceId: # real signature unknown; restored from __doc__
        """
        GetCustomShaderTexID()
        
        Retrieves the :class:`ResourceId` containing the contents of the texture after being
        passed through a custom shader pass.
        
        Should only be called for texture outputs.
        
        :return: The :class:`ResourceId` assigned to the texture with the results of the custom shader.
        :rtype: ResourceId
        """
        pass

    def GetDebugOverlayTexID(self) -> ResourceId: # real signature unknown; restored from __doc__
        """
        GetDebugOverlayTexID()
        
        Retrieves the :class:`ResourceId` containing the contents of the debug overlay
        rendering (if enabled).
        
        Should only be called for texture outputs.
        
        :return: The :class:`ResourceId` assigned to the texture with the debug overlay.
        :rtype: ResourceId
        """
        pass

    def GetDimensions(self) -> Tuple[int,int]: # real signature unknown; restored from __doc__
        """
        GetDimensions()
        
        Retrieve the current dimensions of the output.
        
        :return: The current width and height of the output.
        :rtype: Tuple[int,int]
        """
        pass

    def PickVertex(self, x: int, y: int) -> Tuple[int,int]: # real signature unknown; restored from __doc__
        """
        PickVertex(x, y)
        
        Retrieves the vertex and instance that is under the cursor location, when viewed
        relative to the current window with the current mesh display configuration.
        
        .. note::
          X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
          APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
          fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
          bottom-left co-ordinates, care must be taken to translate them.
        
        Should only be called for mesh outputs.
        
        :param int x: The x co-ordinate to pick from.
        :param int y: The y co-ordinate to pick from.
        :return: A tuple with the first value being the vertex index in the mesh, and the second value being
          the instance index. The values are set to :data:`NoResult` if no vertex was found, 
        :rtype: Tuple[int,int]
        """
        pass

    def ReadbackOutputTexture(self) -> bytes: # real signature unknown; restored from __doc__
        """
        ReadbackOutputTexture()
        
        Read the output texture back as byte data. Primarily useful for headless outputs where
        the output data is not displayed anywhere natively.
        
        :return: The output texture data as tightly packed RGB 3-byte data.
        :rtype: bytes
        """
        pass

    def SetMeshDisplay(self, config: MeshDisplay): # real signature unknown; restored from __doc__
        """
        SetMeshDisplay(config)
        
        Sets the configuration for a mesh output.
        
        :param MeshDisplay config: The configuration.
        """
        pass

    def SetPixelContext(self, window: WindowingData) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        SetPixelContext(window)
        
        Sets up a zoomed in pixel context view around a particular pixel selection.
        
        The texture rendering uses the configuration specified in :meth:`SetTextureDisplay` except with a
        fixed high zoom value and a fixed position, see :meth:`SetPixelContextLocation`.
        
        Should only be called for texture outputs.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :return: A result indicating if the pixel context was successfully configured.
        :rtype: ResultDetails
        """
        pass

    def SetPixelContextLocation(self, x: int, y: int): # real signature unknown; restored from __doc__
        """
        SetPixelContextLocation(x, y)
        
        Sets the pixel that the pixel context should be centred on.
        
        Should only be called for texture outputs.
        
        :param int x: The X co-ordinate to highlight.
        :param int y: The Y co-ordinate to highlight.
        """
        pass

    def SetTextureDisplay(self, config: TextureDisplay): # real signature unknown; restored from __doc__
        """
        SetTextureDisplay(config)
        
        Sets the configuration for a texture output.
        
        :param TextureDisplay config: The configuration.
        """
        pass

    def Shutdown(self): # real signature unknown; restored from __doc__
        """
        Shutdown()
        
        Shutdown this output.
        
        It's optional to call this, as calling :meth:`ReplayController.Shutdown` will shut down all of its
        outputs.
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


    NoResult = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'NoResult': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55205390>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ReplayOutput' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ReplayOutput' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ReplayOutput' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ReplayOutput' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ReplayOutput' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ReplayOutput' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ReplayOutput' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ReplayOutput' objects>, 'Shutdown': <method 'Shutdown' of 'renderdoc.ReplayOutput' objects>, 'SetTextureDisplay': <method 'SetTextureDisplay' of 'renderdoc.ReplayOutput' objects>, 'SetMeshDisplay': <method 'SetMeshDisplay' of 'renderdoc.ReplayOutput' objects>, 'ReadbackOutputTexture': <method 'ReadbackOutputTexture' of 'renderdoc.ReplayOutput' objects>, 'GetDimensions': <method 'GetDimensions' of 'renderdoc.ReplayOutput' objects>, 'ClearThumbnails': <method 'ClearThumbnails' of 'renderdoc.ReplayOutput' objects>, 'AddThumbnail': <method 'AddThumbnail' of 'renderdoc.ReplayOutput' objects>, 'DrawThumbnail': <method 'DrawThumbnail' of 'renderdoc.ReplayOutput' objects>, 'Display': <method 'Display' of 'renderdoc.ReplayOutput' objects>, 'SetPixelContext': <method 'SetPixelContext' of 'renderdoc.ReplayOutput' objects>, 'SetPixelContextLocation': <method 'SetPixelContextLocation' of 'renderdoc.ReplayOutput' objects>, 'DisablePixelContext': <method 'DisablePixelContext' of 'renderdoc.ReplayOutput' objects>, 'GetCustomShaderTexID': <method 'GetCustomShaderTexID' of 'renderdoc.ReplayOutput' objects>, 'GetDebugOverlayTexID': <method 'GetDebugOverlayTexID' of 'renderdoc.ReplayOutput' objects>, 'PickVertex': <method 'PickVertex' of 'renderdoc.ReplayOutput' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ReplayOutput' objects>, '__doc__': '\\nA stateful output handle that contains the current configuration for one particular view\\nof the capture. This allows multiple outputs to run independently without interfering with each\\nother.\\n\\nThe different types are enumerated in :class:`ReplayOutputType`.\\n\\n.. data:: NoResult\\n\\n  No result was found in e.g. :meth:`PickVertex`.\\n\\n'})"


