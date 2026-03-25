# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DescriptorType(__enum.IntEnum):
    """
    The type of a descriptor.
    
    .. data:: Unknown
    
      An unknown or uninitialised type of descriptor.
    
    .. data:: ConstantBuffer
    
      A constant or uniform buffer.
    
    .. data:: Sampler
    
      A separate sampler object.
    
    .. data:: ImageSampler
    
      A combined image and sampler object.
    
    .. data:: Image
    
      An image that can only be sampled from.
    
    .. data:: Buffer
    
      A buffer that can only be read from, with data read literally in a shader via raw or structured
      access.
    
    .. data:: TypedBuffer
    
      A typed buffer that can only be read from, interpreting each element via a format decode.
    
    .. data:: ReadWriteImage
    
      An image that can be read from and written to arbitrarily.
    
    .. data:: ReadWriteTypedBuffer
    
      A typed/texture buffer that can be read from and written to arbitrarily.
    
    .. data:: ReadWriteBuffer
    
      A buffer that can be read from and written to arbitrarily.
    
    .. data:: AccelerationStructure
    
      A ray-tracing acceleration structure, read-only in the shader.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AccelerationStructure = 10
    """ A ray-tracing acceleration structure, read-only in the shader. """

    Buffer = 5
    """
    A buffer that can only be read from, with data read literally in a shader via raw or structured
      access.
    """

    ConstantBuffer = 1
    """ A constant or uniform buffer. """

    Image = 4
    """ An image that can only be sampled from. """

    ImageSampler = 3
    """ A combined image and sampler object. """

    ReadWriteBuffer = 9
    """ A buffer that can be read from and written to arbitrarily. """

    ReadWriteImage = 7
    """ An image that can be read from and written to arbitrarily. """

    ReadWriteTypedBuffer = 8
    """ A typed/texture buffer that can be read from and written to arbitrarily. """

    Sampler = 2
    """ A separate sampler object. """

    TypedBuffer = 6
    """ A typed buffer that can only be read from, interpreting each element via a format decode. """

    Unknown = 0
    """ An unknown or uninitialised type of descriptor. """



