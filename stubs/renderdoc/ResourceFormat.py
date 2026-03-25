# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .CompType import CompType
from .ResourceFormatType import ResourceFormatType

class ResourceFormat(): # skipped bases: <class 'SwigPyObject'>
    """ Description of the format of a resource or element. """
    def BGRAOrder(self) -> bool: # real signature unknown; restored from __doc__
        """
        BGRAOrder()
        
        :return: ``True`` if the components are to be read in ``BGRA`` order.
        
        .. note::
          The convention is that components are in RGBA order. Whether that means first byte to last byte,
          or in bit-packed formats red in the lowest bits.
        
          With BGRA order this means blue is in the first byte/lowest bits, but alpha is still always
          expected in the last byte/uppermost bits.
        
        :rtype: bool
        """
        pass

    def BlockFormat(self) -> bool: # real signature unknown; restored from __doc__
        """
        BlockFormat()
        
        :return: ``True`` if the ``ResourceFormat`` is a block-compressed type.
        :rtype: bool
        """
        pass

    def ElementSize(self) -> int: # real signature unknown; restored from __doc__
        """
        ElementSize()
        
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

    def Name(self) -> str: # real signature unknown; restored from __doc__
        """
        Name()
        
        :return: The name of the format.
        
        :rtype: str
        """
        pass

    def SetBGRAOrder(self, flag: bool): # real signature unknown; restored from __doc__
        """
        SetBGRAOrder(flag)
        
        Set BGRA order flag. See :meth:`BGRAOrder`.
        
        :param bool flag: The new flag value.
        """
        pass

    def SetYUVPlaneCount(self, planes: int): # real signature unknown; restored from __doc__
        """
        SetYUVPlaneCount(planes)
        
        Set number of YUV planes. See :meth:`YUVPlaneCount`.
        
        Invalid values will result in 1 being set.
        
        :param int planes: The new number of YUV planes.
        """
        pass

    def SetYUVSubsampling(self, subsampling: int): # real signature unknown; restored from __doc__
        """
        SetYUVSubsampling(subsampling)
        
        Set YUV subsampling rate. See :meth:`YUVSubsampling`.
        
        The value should be e.g. 444 for 4:4:4 or 422 for 4:2:2. Invalid values will result in 0 being set.
        
        :param int subsampling: The new subsampling rate.
        """
        pass

    def Special(self) -> bool: # real signature unknown; restored from __doc__
        """
        Special()
        
        :return: ``True`` if the ``ResourceFormat`` is a 'special' non-regular type.
        
        :rtype: bool
        """
        pass

    def SRGBCorrected(self) -> bool: # real signature unknown; restored from __doc__
        """
        SRGBCorrected()
        
        Equivalent to checking if :data:`compType` is :data:`CompType.UNormSRGB`
        
        :return: ``True`` if the components are SRGB corrected on read and write.
        :rtype: bool
        """
        pass

    def YUVPlaneCount(self) -> int: # real signature unknown; restored from __doc__
        """
        YUVPlaneCount()
        
        Get the number of planes for a YUV format. Only valid when :data:`type` is
        a YUV format like :attr:`ResourceFormatType.YUV8`.
        
        For other formats, 1 is returned.
        
        :return: The number of planes
        :rtype: int
        """
        pass

    def YUVSubsampling(self) -> int: # real signature unknown; restored from __doc__
        """
        YUVSubsampling()
        
        Get the subsampling rate for a YUV format. Only valid when :data:`type` is
        a YUV format like :attr:`ResourceFormatType.YUV8`.
        
        For other formats, 0 is returned.
        
        :return: The subsampling rate, e.g. 444 for 4:4:4 or 420 for 4:2:0
        :rtype: int
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
    def compType(self) -> CompType:
        """
The :class:`type <CompType>` of each component.

:type: CompType

"""
        pass

    @compType.setter
    def compType(self, value: CompType):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551B1DB0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ResourceFormat' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ResourceFormat' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ResourceFormat' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ResourceFormat' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ResourceFormat' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ResourceFormat' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ResourceFormat' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ResourceFormat' objects>, 'Name': <method 'Name' of 'renderdoc.ResourceFormat' objects>, 'Special': <method 'Special' of 'renderdoc.ResourceFormat' objects>, 'BGRAOrder': <method 'BGRAOrder' of 'renderdoc.ResourceFormat' objects>, 'SRGBCorrected': <method 'SRGBCorrected' of 'renderdoc.ResourceFormat' objects>, 'YUVSubsampling': <method 'YUVSubsampling' of 'renderdoc.ResourceFormat' objects>, 'YUVPlaneCount': <method 'YUVPlaneCount' of 'renderdoc.ResourceFormat' objects>, 'SetBGRAOrder': <method 'SetBGRAOrder' of 'renderdoc.ResourceFormat' objects>, 'SetYUVSubsampling': <method 'SetYUVSubsampling' of 'renderdoc.ResourceFormat' objects>, 'SetYUVPlaneCount': <method 'SetYUVPlaneCount' of 'renderdoc.ResourceFormat' objects>, 'BlockFormat': <method 'BlockFormat' of 'renderdoc.ResourceFormat' objects>, 'ElementSize': <method 'ElementSize' of 'renderdoc.ResourceFormat' objects>, 'compCount': <attribute 'compCount' of 'renderdoc.ResourceFormat' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ResourceFormat' objects>, 'type': <attribute 'type' of 'renderdoc.ResourceFormat' objects>, 'compType': <attribute 'compType' of 'renderdoc.ResourceFormat' objects>, 'compByteWidth': <attribute 'compByteWidth' of 'renderdoc.ResourceFormat' objects>, '__doc__': 'Description of the format of a resource or element.'})"


