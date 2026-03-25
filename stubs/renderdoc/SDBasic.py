# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class SDBasic(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    Array = 2
    """
    A composite type with some number of children with an identical type and referred to purely by
      their index in the array. May be empty.
    """

    Boolean = 10
    """ A boolean true/false value. """

    Buffer = 4
    """ An opaque byte buffer. """

    Character = 11
    """
    A single byte character. Wide/multi-byte characters are not supported (these would be stored as a
      string with 1 character and multiple bytes in UTF-8).
    """

    Chunk = 0
    """
    A 'special' type indicating that the object is a chunk. A chunk can be treated like a
      :data:`Struct` otherwise. See :class:`SDChunk`.
    """

    Enum = 6
    """ An enum value - stored as an integer but with a distinct set of possible named values. """

    Float = 9
    """ A floating point value. """

    GPUAddress = 13
    """
    A GPU pointer. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
      the address of a resource in a capture.
    """

    Null = 3
    """
    An indicator that an object could be here, but is optional and is currently not present. See
      :data:`SDTypeFlags.Nullable`.
    """

    Resource = 12
    """
    A ResourceId. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
      the unique Id of a resource in a capture.
    """

    SignedInteger = 8
    """ An signed integer. """

    String = 5
    """ A string, encoded as UTF-8. """

    Struct = 1
    """
    A composite type with some number of children of different types, each child with its own name.
      May in some cases be empty, so the presence of children should not be assumed.
    """

    UnsignedInteger = 7
    """ An unsigned integer. """



