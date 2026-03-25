# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class NewCaptureData(): # skipped bases: <class 'SwigPyObject'>
    """ Information about the a new capture created by the target. """
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
    def api(self) -> str:
        """
The API used for this capture, if available.

.. note::
  May be empty if running with an older version of RenderDoc

:type: str

"""
        pass

    @api.setter
    def api(self, value: str):
        pass

    @property
    def byteSize(self) -> int:
        """
The size of the capture, in bytes.

:type: int

"""
        pass

    @byteSize.setter
    def byteSize(self, value: int):
        pass

    @property
    def captureId(self) -> int:
        """
An identifier to use to refer to this capture.

:type: int

"""
        pass

    @captureId.setter
    def captureId(self, value: int):
        pass

    @property
    def frameNumber(self) -> int:
        """
The frame number that this capture came from.

:type: int

"""
        pass

    @frameNumber.setter
    def frameNumber(self, value: int):
        pass

    @property
    def local(self) -> bool:
        """
``True`` if the target is running on the local system.

:type: bool

"""
        pass

    @local.setter
    def local(self, value: bool):
        pass

    @property
    def path(self) -> str:
        """
The local path on the target system where the capture is saved.

:type: str

"""
        pass

    @path.setter
    def path(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def thumbHeight(self) -> int:
        """
The height of the image contained in :data:`thumbnail`.

:type: int

"""
        pass

    @thumbHeight.setter
    def thumbHeight(self, value: int):
        pass

    @property
    def thumbnail(self) -> bytes:
        """
The raw bytes that contain the capture thumbnail, as RGB8 data.

:type: bytes

"""
        pass

    @thumbnail.setter
    def thumbnail(self, value: bytes):
        pass

    @property
    def thumbWidth(self) -> int:
        """
The width of the image contained in :data:`thumbnail`.

:type: int

"""
        pass

    @thumbWidth.setter
    def thumbWidth(self, value: int):
        pass

    @property
    def timestamp(self) -> int:
        """
The time the capture was created, as a unix timestamp in UTC.

:type: int

"""
        pass

    @timestamp.setter
    def timestamp(self, value: int):
        pass

    @property
    def title(self) -> str:
        """
The custom title for this capture, if empty a default title can be used.

:type: str

"""
        pass

    @title.setter
    def title(self, value: str):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5522FCF0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.NewCaptureData' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.NewCaptureData' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.NewCaptureData' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.NewCaptureData' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.NewCaptureData' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.NewCaptureData' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.NewCaptureData' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.NewCaptureData' objects>, 'frameNumber': <attribute 'frameNumber' of 'renderdoc.NewCaptureData' objects>, 'title': <attribute 'title' of 'renderdoc.NewCaptureData' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.NewCaptureData' objects>, 'thumbHeight': <attribute 'thumbHeight' of 'renderdoc.NewCaptureData' objects>, 'path': <attribute 'path' of 'renderdoc.NewCaptureData' objects>, 'captureId': <attribute 'captureId' of 'renderdoc.NewCaptureData' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.NewCaptureData' objects>, 'local': <attribute 'local' of 'renderdoc.NewCaptureData' objects>, 'thumbWidth': <attribute 'thumbWidth' of 'renderdoc.NewCaptureData' objects>, 'timestamp': <attribute 'timestamp' of 'renderdoc.NewCaptureData' objects>, 'thumbnail': <attribute 'thumbnail' of 'renderdoc.NewCaptureData' objects>, 'api': <attribute 'api' of 'renderdoc.NewCaptureData' objects>, '__doc__': 'Information about the a new capture created by the target.'})"


