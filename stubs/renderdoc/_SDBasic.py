from enum import IntEnum

class SDBasic(IntEnum):
    # Original docstring
    """
    The basic irreducible type of an object. Every other more complex type is built on these.
    
    .. data:: Chunk
    
      A 'special' type indicating that the object is a chunk. A chunk can be treated like a
      :data:`Struct` otherwise. See :class:`SDChunk`.
    
    .. data:: Struct
    
      A composite type with some number of children of different types, each child with its own name.
      May in some cases be empty, so the presence of children should not be assumed.
    
    .. data:: Array
    
      A composite type with some number of children with an identical type and referred to purely by
      their index in the array. May be empty.
    
    .. data:: Null
    
      An indicator that an object could be here, but is optional and is currently not present. See
      :data:`SDTypeFlags.Nullable`.
    
    .. data:: Buffer
    
      An opaque byte buffer.
    
    .. data:: String
    
      A string, encoded as UTF-8.
    
    .. data:: Enum
    
      An enum value - stored as an integer but with a distinct set of possible named values.
    
    .. data:: UnsignedInteger
    
      An unsigned integer.
    
    .. data:: SignedInteger
    
      An signed integer.
    
    .. data:: Float
    
      A floating point value.
    
    .. data:: Boolean
    
      A boolean true/false value.
    
    .. data:: Character
    
      A single byte character. Wide/multi-byte characters are not supported (these would be stored as a
      string with 1 character and multiple bytes in UTF-8).
    
    .. data:: Resource
    
      A ResourceId. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
      the unique Id of a resource in a capture.
    
    .. data:: GPUAddress
    
      A GPU pointer. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
      the address of a resource in a capture.
    """
    
    
    # Enum values
    
    Chunk = 0
    """
    A 'special' type indicating that the object is a chunk. A chunk can be treated like a
    :data:`Struct` otherwise. See :class:`SDChunk`.
    """
    
    Struct = 1
    """
    A composite type with some number of children of different types, each child with its own name.
    May in some cases be empty, so the presence of children should not be assumed.
    """
    
    Array = 2
    """
    A composite type with some number of children with an identical type and referred to purely by
    their index in the array. May be empty.
    """
    
    Null = 3
    """
    An indicator that an object could be here, but is optional and is currently not present. See
    :data:`SDTypeFlags.Nullable`.
    """
    
    Buffer = 4
    """
    An opaque byte buffer.
    """
    
    String = 5
    """
    A string, encoded as UTF-8.
    """
    
    Enum = 6
    """
    An enum value - stored as an integer but with a distinct set of possible named values.
    """
    
    UnsignedInteger = 7
    """
    An unsigned integer.
    """
    
    SignedInteger = 8
    """
    An signed integer.
    """
    
    Float = 9
    """
    A floating point value.
    """
    
    Boolean = 10
    """
    A boolean true/false value.
    """
    
    Character = 11
    """
    A single byte character. Wide/multi-byte characters are not supported (these would be stored as a
    string with 1 character and multiple bytes in UTF-8).
    """
    
    Resource = 12
    """
    A ResourceId. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
    the unique Id of a resource in a capture.
    """
    
    GPUAddress = 13
    """
    A GPU pointer. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
    the address of a resource in a capture.
    """
    

# Assign __doc__ for enum values for easier introspection

SDBasic.Chunk.__doc__ = """
A 'special' type indicating that the object is a chunk. A chunk can be treated like a
:data:`Struct` otherwise. See :class:`SDChunk`.
"""

SDBasic.Struct.__doc__ = """
A composite type with some number of children of different types, each child with its own name.
May in some cases be empty, so the presence of children should not be assumed.
"""

SDBasic.Array.__doc__ = """
A composite type with some number of children with an identical type and referred to purely by
their index in the array. May be empty.
"""

SDBasic.Null.__doc__ = """
An indicator that an object could be here, but is optional and is currently not present. See
:data:`SDTypeFlags.Nullable`.
"""

SDBasic.Buffer.__doc__ = """
An opaque byte buffer.
"""

SDBasic.String.__doc__ = """
A string, encoded as UTF-8.
"""

SDBasic.Enum.__doc__ = """
An enum value - stored as an integer but with a distinct set of possible named values.
"""

SDBasic.UnsignedInteger.__doc__ = """
An unsigned integer.
"""

SDBasic.SignedInteger.__doc__ = """
An signed integer.
"""

SDBasic.Float.__doc__ = """
A floating point value.
"""

SDBasic.Boolean.__doc__ = """
A boolean true/false value.
"""

SDBasic.Character.__doc__ = """
A single byte character. Wide/multi-byte characters are not supported (these would be stored as a
string with 1 character and multiple bytes in UTF-8).
"""

SDBasic.Resource.__doc__ = """
A ResourceId. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
the unique Id of a resource in a capture.
"""

SDBasic.GPUAddress.__doc__ = """
A GPU pointer. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
the address of a resource in a capture.
"""

