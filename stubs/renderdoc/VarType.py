# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class VarType(__enum.IntEnum):
    """
    Represents the base type of a shader variable in debugging or constant blocks.
    
    .. data:: Float
    
      A single-precision (32-bit) floating point value.
    
    .. data:: Double
    
      A double-precision (64-bit) floating point value.
    
    .. data:: Half
    
      A half-precision (16-bit) floating point value.
    
    .. data:: SInt
    
      A signed 32-bit integer value.
    
    .. data:: UInt
    
      An unsigned 32-bit integer value.
    
    .. data:: SShort
    
      A signed 16-bit integer value.
    
    .. data:: UShort
    
      An unsigned 16-bit integer value.
    
    .. data:: SLong
    
      A signed 64-bit integer value.
    
    .. data:: ULong
    
      An unsigned 64-bit integer value.
    
    .. data:: SByte
    
      A signed 8-bit integer value.
    
    .. data:: UByte
    
      An unsigned 8-bit integer value.
    
    .. data:: Bool
    
      A boolean value.
    
    .. data:: Enum
    
      An enum - each member gives a named value, and the type itself is stored as an integer.
    
    .. data:: Struct
    
      A structure with some number of members.
    
    .. data:: GPUPointer
    
      A 64-bit pointer into GPU-addressable memory. Variables with this type are stored with opaque
      contents and should be decoded with :meth:`ShaderVariable.GetPointer`.
    
    .. data:: ConstantBlock
    
      A reference to a constant block bound to the shader. Variables with this type are stored with
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBinding`.
    
    .. data:: ReadOnlyResource
    
      A reference to a read only resource bound to the shader. Variables with this type are stored with
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBinding`.
    
    .. data:: ReadWriteResource
    
      A reference to a read/write resource bound to the shader. Variables with this type are stored with
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBinding`.
    
    .. data:: Sampler
    
      A reference to a sampler bound to the shader. Variables with this type are stored with opaque
      contents and should be decoded with :meth:`ShaderVariable.GetBinding`.
    
    .. data:: Unknown
    
      An unknown type.
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Bool = 11
    """ A boolean value. """

    ConstantBlock = 15
    """
    A reference to a constant block bound to the shader. Variables with this type are stored with
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBinding`.
    """

    Double = 1
    """ A double-precision (64-bit) floating point value. """

    Enum = 12
    """ An enum - each member gives a named value, and the type itself is stored as an integer. """

    Float = 0
    """ A single-precision (32-bit) floating point value. """

    GPUPointer = 14
    """
    A 64-bit pointer into GPU-addressable memory. Variables with this type are stored with opaque
      contents and should be decoded with :meth:`ShaderVariable.GetPointer`.
    """

    Half = 2
    """ A half-precision (16-bit) floating point value. """

    ReadOnlyResource = 16
    """
    A reference to a read only resource bound to the shader. Variables with this type are stored with
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBinding`.
    """

    ReadWriteResource = 17
    """
    A reference to a read/write resource bound to the shader. Variables with this type are stored with
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBinding`.
    """

    Sampler = 18
    """
    A reference to a sampler bound to the shader. Variables with this type are stored with opaque
      contents and should be decoded with :meth:`ShaderVariable.GetBinding`.
    """

    SByte = 9
    """ A signed 8-bit integer value. """

    SInt = 3
    """ A signed 32-bit integer value. """

    SLong = 7
    """ A signed 64-bit integer value. """

    SShort = 5
    """ A signed 16-bit integer value. """

    Struct = 13
    """ A structure with some number of members. """

    UByte = 10
    """ An unsigned 8-bit integer value. """

    UInt = 4
    """ An unsigned 32-bit integer value. """

    ULong = 8
    """ An unsigned 64-bit integer value. """

    Unknown = 255
    """ An unknown type. """

    UShort = 6
    """ An unsigned 16-bit integer value. """



