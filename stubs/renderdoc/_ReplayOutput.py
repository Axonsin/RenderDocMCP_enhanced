from ._CompType import CompType
from ._MeshDisplay import MeshDisplay
from ._ResourceId import ResourceId
from ._ResultDetails import ResultDetails
from ._Subresource import Subresource
from ._TextureDisplay import TextureDisplay
from ._WindowingData import WindowingData
from typing import Tuple

class ReplayOutput():
    # Original docstring
    """
    A stateful output handle that contains the current configuration for one particular view
    of the capture. This allows multiple outputs to run independently without interfering with each
    other.
    
    The different types are enumerated in :class:`ReplayOutputType`.
    
    .. data:: NoResult
    
      No result was found in e.g. :meth:`PickVertex`.
    """
    
    
    NoResult = 4294967295
    """
    No result was found in e.g. :meth:`PickVertex`.
    """
    
    
    def Shutdown(self):
        """
        Shutdown this output.
        
        It's optional to call this, as calling :meth:`ReplayController.Shutdown` will shut down all of its
        outputs.
        """
        pass
    
    
    def SetTextureDisplay(self, config: TextureDisplay):
        """
        Sets the configuration for a texture output.
        
        :param TextureDisplay config: The configuration.
        """
        pass
    
    
    def SetMeshDisplay(self, config: MeshDisplay):
        """
        Sets the configuration for a mesh output.
        
        :param MeshDisplay config: The configuration.
        """
        pass
    
    
    def ReadbackOutputTexture(self) -> bytes:
        """
        Read the output texture back as byte data. Primarily useful for headless outputs where
        the output data is not displayed anywhere natively.
        
        :return: The output texture data as tightly packed RGB 3-byte data.
        :rtype: bytes
        """
        pass
    
    
    def GetDimensions(self) -> Tuple[int, int]:
        """
        Retrieve the current dimensions of the output.
        
        :return: The current width and height of the output.
        :rtype: Tuple[int,int]
        """
        pass
    
    
    def ClearThumbnails(self):
        """
        Clear and release all thumbnails associated with this output. See :meth:`AddThumbnail`.
        """
        pass
    
    
    def AddThumbnail(self, window: WindowingData, textureId: ResourceId, sub: Subresource, typeCast: CompType) -> ResultDetails:
        """
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
    
    
    def DrawThumbnail(self, width: int, height: int, textureId: ResourceId, sub: Subresource, typeCast: CompType) -> bytes:
        """
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
    
    
    def Display(self):
        """
        Render to the window handle specified when the output was created.
        
        This will also render any thumbnails and the pixel context, if enabled.
        """
        pass
    
    
    def SetPixelContext(self, window: WindowingData) -> ResultDetails:
        """
        Sets up a zoomed in pixel context view around a particular pixel selection.
        
        The texture rendering uses the configuration specified in :meth:`SetTextureDisplay` except with a
        fixed high zoom value and a fixed position, see :meth:`SetPixelContextLocation`.
        
        Should only be called for texture outputs.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :return: A result indicating if the pixel context was successfully configured.
        :rtype: ResultDetails
        """
        pass
    
    
    def SetPixelContextLocation(self, x: int, y: int):
        """
        Sets the pixel that the pixel context should be centred on.
        
        Should only be called for texture outputs.
        
        :param int x: The X co-ordinate to highlight.
        :param int y: The Y co-ordinate to highlight.
        """
        pass
    
    
    def DisablePixelContext(self):
        """
        Disable the pixel context view from rendering.
        """
        pass
    
    
    def GetCustomShaderTexID(self) -> ResourceId:
        """
        Retrieves the :class:`ResourceId` containing the contents of the texture after being
        passed through a custom shader pass.
        
        Should only be called for texture outputs.
        
        :return: The :class:`ResourceId` assigned to the texture with the results of the custom shader.
        :rtype: ResourceId
        """
        pass
    
    
    def GetDebugOverlayTexID(self) -> ResourceId:
        """
        Retrieves the :class:`ResourceId` containing the contents of the debug overlay
        rendering (if enabled).
        
        Should only be called for texture outputs.
        
        :return: The :class:`ResourceId` assigned to the texture with the debug overlay.
        :rtype: ResourceId
        """
        pass
    
    
    def PickVertex(self, x: int, y: int) -> Tuple[int, int]:
        """
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
    
