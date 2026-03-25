# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class BindType(__enum.IntEnum):
    """
    The type of a shader resource bind.
    
    .. data:: Unknown
    
      An unknown type of binding.
    
    .. data:: ConstantBuffer
    
      A constant or uniform buffer.
    
    .. data:: Sampler
    
      A separate sampler object.
    
    .. data:: ImageSampler
    
      A combined image and sampler object.
    
    .. data:: ReadOnlyImage
    
      An image that can only be sampled from.
    
    .. data:: ReadWriteImage
    
      An image that can be read from and written to arbitrarily.
    
    .. data:: ReadOnlyTBuffer
    
      A texture buffer that can only be read from.
    
    .. data:: ReadWriteTBuffer
    
      A texture buffer that can be read from and written to arbitrarily.
    
    .. data:: ReadOnlyBuffer
    
      A buffer that can only be read from, distinct from :data:`ConstantBuffer`.
    
    .. data:: ReadWriteBuffer
    
      A buffer that can be read from and written to arbitrarily.
    
    .. data:: ReadOnlyResource
    
      A resource that can only be read from
    
    .. data:: ReadWriteResource
    
      A resource that can be read from and written to arbitrarily.
    
    .. data:: InputAttachment
    
      An input attachment for reading from the target currently being written.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    ConstantBuffer = 1
    """ A constant or uniform buffer. """

    ImageSampler = 3
    """ A combined image and sampler object. """

    InputAttachment = 12
    """ An input attachment for reading from the target currently being written. """

    ReadOnlyBuffer = 8
    """ A buffer that can only be read from, distinct from :data:`ConstantBuffer`. """

    ReadOnlyImage = 4
    """ An image that can only be sampled from. """

    ReadOnlyResource = 10
    """ A resource that can only be read from """

    ReadOnlyTBuffer = 6
    """ A texture buffer that can only be read from. """

    ReadWriteBuffer = 9
    """ A buffer that can be read from and written to arbitrarily. """

    ReadWriteImage = 5
    """ An image that can be read from and written to arbitrarily. """

    ReadWriteResource = 11
    """ A resource that can be read from and written to arbitrarily. """

    ReadWriteTBuffer = 7
    """ A texture buffer that can be read from and written to arbitrarily. """

    Sampler = 2
    """ A separate sampler object. """

    Unknown = 0
    """ An unknown type of binding. """



