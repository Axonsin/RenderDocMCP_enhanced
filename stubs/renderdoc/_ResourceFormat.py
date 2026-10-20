from ._CompType import CompType
from ._ResourceFormatType import ResourceFormatType
from typing import Tuple

from typing import overload

class ResourceFormat():
    # Original docstring
    """
    Description of the format of a resource or element.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ResourceFormat.
        """
        pass
    
    @overload
    def __init__(self, other: 'ResourceFormat'):
        """
        Construct a new ResourceFormat with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def Name(self) -> str:
        """
        :return: The name of the format.
        
        :rtype: str
        """
        pass
    
    
    def Special(self) -> bool:
        """
        :return: ``True`` if the ``ResourceFormat`` is a 'special' non-regular type.
        
        :rtype: bool
        """
        pass
    
    
    def BGRAOrder(self) -> bool:
        """
        :return: ``True`` if the components are to be read in ``BGRA`` order.
        
        .. note::
          The convention is that components are in RGBA order. Whether that means first byte to last byte,
          or in bit-packed formats red in the lowest bits.
        
          With BGRA order this means blue is in the first byte/lowest bits, but alpha is still always
          expected in the last byte/uppermost bits.
        
        :rtype: bool
        """
        pass
    
    
    def SRGBCorrected(self) -> bool:
        """
        Equivalent to checking if :data:`compType` is :data:`CompType.UNormSRGB`
        
        :return: ``True`` if the components are SRGB corrected on read and write.
        :rtype: bool
        """
        pass
    
    
    def YUVSubsampling(self) -> int:
        """
        Get the subsampling rate for a YUV format. Only valid when :data:`type` is
        a YUV format like :attr:`ResourceFormatType.YUV8`.
        
        For other formats, 0 is returned.
        
        :return: The subsampling rate, e.g. 444 for 4:4:4 or 420 for 4:2:0
        :rtype: int
        """
        pass
    
    
    def YUVPlaneCount(self) -> int:
        """
        Get the number of planes for a YUV format. Only valid when :data:`type` is
        a YUV format like :attr:`ResourceFormatType.YUV8`.
        
        For other formats, 1 is returned.
        
        :return: The number of planes
        :rtype: int
        """
        pass
    
    
    def SetBGRAOrder(self, flag: bool):
        """
        Set BGRA order flag. See :meth:`BGRAOrder`.
        
        :param bool flag: The new flag value.
        """
        pass
    
    
    def SetYUVSubsampling(self, subsampling: int):
        """
        Set YUV subsampling rate. See :meth:`YUVSubsampling`.
        
        The value should be e.g. 444 for 4:4:4 or 422 for 4:2:2. Invalid values will result in 0 being set.
        
        :param int subsampling: The new subsampling rate.
        """
        pass
    
    
    def SetYUVPlaneCount(self, planes: int):
        """
        Set number of YUV planes. See :meth:`YUVPlaneCount`.
        
        Invalid values will result in 1 being set.
        
        :param int planes: The new number of YUV planes.
        """
        pass
    
    
    def BlockFormat(self) -> bool:
        """
        :return: ``True`` if the ``ResourceFormat`` is a block-compressed type.
        :rtype: bool
        """
        pass
    
    
    def SetPVRTC(self, version: int, bpp: int):
        """
        Set PVRTC properties. See :meth:`PVRTCVersion` and :meth:`PVRTCBpp`.
        
        Invalid values will result in undefined format properties. Has no effect if the format is
        not already set to be PVRTC.
        
        :param int version: The PVRTC version.
        :param int bpp: The bits per pixel of the PVRTC blocks.
        """
        pass
    
    
    def PVRTCVersion(self) -> int:
        """
        For PVRTC formats, return the version of PVRTC used either 1 or 2.
        
        Will return 0 if the format is not PVRTC.
        
        :return: The version of the current PVRTC format
        :rtype: int
        """
        pass
    
    
    def PVRTCBpp(self) -> int:
        """
        For PVRTC formats, return the bits per pixel rate either 2 or 4. This can also be
        thought of as the block shape since each block is 64-bit. 2bpp is 8x4 and 4bpp is 4x4.
        
        Will return 0 if the format is not PVRTC.
        
        :return: The bpp of the current PVRTC format
        :rtype: int
        """
        pass
    
    
    def SetASTC2D(self, block2D: Tuple[int, int]):
        """
        Set 2D ASTC block properties. See :meth:`ASTCDimension` and :meth:`ASTC2DBlock`.
        
        Invalid values will result in undefined format properties. Has no effect if the format is
        not already set to be ASTC.
        
        :param Tuple[int,int] block2D: The 2D block shape.
        """
        pass
    
    
    def SetASTC3D(self, block3D: Tuple[int, int, int]):
        """
        Set 3D ASTC block properties. See :meth:`ASTCDimension` and :meth:`ASTC3DBlock`.
        
        Invalid values will result in undefined format properties. Has no effect if the format is
        not already set to be ASTC.
        
        :param Tuple[int,int,int] block3D: The 3D block shape.
        """
        pass
    
    
    def ASTCDimension(self) -> int:
        """
        For ASTC formats, return the dimension of the block either 2 or 3.
        
        Will return 0 if the format is not ASTC.
        
        :return: The dimension of the blocks in the current ASTC format
        :rtype: int
        """
        pass
    
    
    def ASTC2DBlock(self) -> Tuple[int, int]:
        """
        For 2D ASTC formats, return the block shape.
        
        Will return all 0s if the format is not ASTC or is not 2D. See :meth:`ASTCDimension`.
        
        :return: The block shape if the format is 2D ASTC
        :rtype: Tuple[int, int]
        """
        pass
    
    
    def ASTC3DBlock(self) -> Tuple[int, int, int]:
        """
        For 3D ASTC formats, return the block shape.
        
        Will return all 0s if the format is not ASTC or is not 3D. See :meth:`ASTCDimension`.
        
        :return: The block shape if the format is 3D ASTC
        :rtype: Tuple[int, int, int]
        """
        pass
    
    
    def ElementSize(self) -> int:
        """
        Return the size of a single element in this format, usually a pixel. For regular sized
        formats this is just :data:`compByteWidth` times :data:`compCount`, for special packed formats it's
        the tightly packed size of a single element, with no padding.
        
        Block-compressed formats define an 'element' as a whole block of texels.
        
        YUV formats where texel size varies depending on subsampling will return the size of a decompressed
        texel.
        
        :return: The size of an element
        :rtype: int
        """
        pass
    
    @property
    def compCount(self) -> int:
        """
        The number of components in each element.
        
        :type: int
        """
        pass
    
    @compCount.setter
    def compCount(self, value: int):
        pass
    
    @property
    def type(self) -> ResourceFormatType:
        """
        The :class:`ResourceFormatType` of this format. If the value is not
        :attr:`ResourceFormatType.Regular` then it's a non-uniform layout like block-compressed.
        
        :type: ResourceFormatType
        """
        pass
    
    @type.setter
    def type(self, value: ResourceFormatType):
        pass
    
    @property
    def compType(self) -> CompType:
        """
        The :class:`type <CompType>` of each component.
        
        :type: CompType
        """
        pass
    
    @compType.setter
    def compType(self, value: CompType):
        pass
    
    @property
    def compByteWidth(self) -> int:
        """
        The width in bytes of each component.
        
        :type: int
        """
        pass
    
    @compByteWidth.setter
    def compByteWidth(self, value: int):
        pass
    
