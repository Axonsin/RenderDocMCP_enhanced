from enum import IntEnum

class VarType(IntEnum):
    # Original docstring
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
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
    
    .. data:: ReadOnlyResource
    
      A reference to a read only resource bound to the shader. Variables with this type are stored with
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
    
    .. data:: ReadWriteResource
    
      A reference to a read/write resource bound to the shader. Variables with this type are stored with
      opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
    
    .. data:: Sampler
    
      A reference to a sampler bound to the shader. Variables with this type are stored with opaque
      contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
    
    .. data:: Unknown
    
      An unknown type.
    """
    
    
    # Enum values
    
    Float = 0
    """
    A single-precision (32-bit) floating point value.
    """
    
    Double = 1
    """
    A double-precision (64-bit) floating point value.
    """
    
    Half = 2
    """
    A half-precision (16-bit) floating point value.
    """
    
    SInt = 3
    """
    A signed 32-bit integer value.
    """
    
    UInt = 4
    """
    An unsigned 32-bit integer value.
    """
    
    SShort = 5
    """
    A signed 16-bit integer value.
    """
    
    UShort = 6
    """
    An unsigned 16-bit integer value.
    """
    
    SLong = 7
    """
    A signed 64-bit integer value.
    """
    
    ULong = 8
    """
    An unsigned 64-bit integer value.
    """
    
    SByte = 9
    """
    A signed 8-bit integer value.
    """
    
    UByte = 10
    """
    An unsigned 8-bit integer value.
    """
    
    Bool = 11
    """
    A boolean value.
    """
    
    Enum = 12
    """
    An enum - each member gives a named value, and the type itself is stored as an integer.
    """
    
    Struct = 13
    """
    A structure with some number of members.
    """
    
    GPUPointer = 14
    """
    A 64-bit pointer into GPU-addressable memory. Variables with this type are stored with opaque
    contents and should be decoded with :meth:`ShaderVariable.GetPointer`.
    """
    
    ConstantBlock = 15
    """
    A reference to a constant block bound to the shader. Variables with this type are stored with
    opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
    """
    
    ReadOnlyResource = 16
    """
    A reference to a read only resource bound to the shader. Variables with this type are stored with
    opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
    """
    
    ReadWriteResource = 17
    """
    A reference to a read/write resource bound to the shader. Variables with this type are stored with
    opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
    """
    
    Sampler = 18
    """
    A reference to a sampler bound to the shader. Variables with this type are stored with opaque
    contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
    """
    
    Unknown = 255
    """
    An unknown type.
    """
    

# Assign __doc__ for enum values for easier introspection

VarType.Float.__doc__ = """
A single-precision (32-bit) floating point value.
"""

VarType.Double.__doc__ = """
A double-precision (64-bit) floating point value.
"""

VarType.Half.__doc__ = """
A half-precision (16-bit) floating point value.
"""

VarType.SInt.__doc__ = """
A signed 32-bit integer value.
"""

VarType.UInt.__doc__ = """
An unsigned 32-bit integer value.
"""

VarType.SShort.__doc__ = """
A signed 16-bit integer value.
"""

VarType.UShort.__doc__ = """
An unsigned 16-bit integer value.
"""

VarType.SLong.__doc__ = """
A signed 64-bit integer value.
"""

VarType.ULong.__doc__ = """
An unsigned 64-bit integer value.
"""

VarType.SByte.__doc__ = """
A signed 8-bit integer value.
"""

VarType.UByte.__doc__ = """
An unsigned 8-bit integer value.
"""

VarType.Bool.__doc__ = """
A boolean value.
"""

VarType.Enum.__doc__ = """
An enum - each member gives a named value, and the type itself is stored as an integer.
"""

VarType.Struct.__doc__ = """
A structure with some number of members.
"""

VarType.GPUPointer.__doc__ = """
A 64-bit pointer into GPU-addressable memory. Variables with this type are stored with opaque
contents and should be decoded with :meth:`ShaderVariable.GetPointer`.
"""

VarType.ConstantBlock.__doc__ = """
A reference to a constant block bound to the shader. Variables with this type are stored with
opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
"""

VarType.ReadOnlyResource.__doc__ = """
A reference to a read only resource bound to the shader. Variables with this type are stored with
opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
"""

VarType.ReadWriteResource.__doc__ = """
A reference to a read/write resource bound to the shader. Variables with this type are stored with
opaque contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
"""

VarType.Sampler.__doc__ = """
A reference to a sampler bound to the shader. Variables with this type are stored with opaque
contents and should be decoded with :meth:`ShaderVariable.GetBindIndex`.
"""

VarType.Unknown.__doc__ = """
An unknown type.
"""

