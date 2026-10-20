from enum import IntFlag

class SDTypeFlags(IntFlag):
    # Original docstring
    """
    Bitfield flags that could be applied to a type.
    
    .. data:: NoFlags
    
      This type has no special properties.
    
    .. data:: HasCustomString
    
      This type has a custom string. This could be used for example for enums, to display the string
      value of the enum as well as the integer storage, or perhaps for opaque types that should be
      displayed to the user as a string even if the underlying representation is not a string.
    
    .. data:: Hidden
    
      This type is considered an implementation detail and should not typically be displayed to the user.
    
    .. data:: Nullable
    
      This type is nullable and can sometimes be removed and replaced simply with a Null type. See
      :data:`SDBasic.Null`.
    
    .. data:: NullString
    
      Special flag to indicate that this is a C-string which was NULL, not just empty.
    
    .. data:: FixedArray
    
      Special flag to indicate that this is array was a fixed-size real array, rather than a complex
      container type or a pointer & length.
    
    .. data:: Union
    
      Special flag to indicate that this is structure is stored as a union, meaning all children share
      the same memory and some external flag indicates which element is valid.
    
    .. data:: Important
    
      Indicates that this object is important or significant, to aid in generating a summary/one-line
      view of a particular chunk by only including important children.
    
      This property can be recursive - so an important child which is a structure can have only some
      members which are important.
    
    .. data:: ImportantChildren
    
      Indicates that only important children should be processed, as noted in :data:`Important`. This
      may appear on an object which has no important children - which indicates explicitly that there
      are no important children so when summarising no parameters should be shown.
    
    .. data:: HiddenChildren
    
      Indicates that some children are marked as hidden. This can be important for cases where the
      number of children is important.
    
    .. data:: OffsetOrSize
    
      Special flag to indicate that this type will be used as a byte offset or byte size, which is used to
      control the formatting mode when the value is displayed in the UI.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    This type has no special properties.
    """
    
    HasCustomString = 1
    """
    This type has a custom string. This could be used for example for enums, to display the string
    value of the enum as well as the integer storage, or perhaps for opaque types that should be
    displayed to the user as a string even if the underlying representation is not a string.
    """
    
    Hidden = 2
    """
    This type is considered an implementation detail and should not typically be displayed to the user.
    """
    
    Nullable = 4
    """
    This type is nullable and can sometimes be removed and replaced simply with a Null type. See
    :data:`SDBasic.Null`.
    """
    
    NullString = 8
    """
    Special flag to indicate that this is a C-string which was NULL, not just empty.
    """
    
    FixedArray = 16
    """
    Special flag to indicate that this is array was a fixed-size real array, rather than a complex
    container type or a pointer & length.
    """
    
    Union = 32
    """
    Special flag to indicate that this is structure is stored as a union, meaning all children share
    the same memory and some external flag indicates which element is valid.
    """
    
    Important = 64
    """
    Indicates that this object is important or significant, to aid in generating a summary/one-line
    view of a particular chunk by only including important children.
    
    This property can be recursive - so an important child which is a structure can have only some
    members which are important.
    """
    
    ImportantChildren = 128
    """
    Indicates that only important children should be processed, as noted in :data:`Important`. This
    may appear on an object which has no important children - which indicates explicitly that there
    are no important children so when summarising no parameters should be shown.
    """
    
    HiddenChildren = 256
    """
    Indicates that some children are marked as hidden. This can be important for cases where the
    number of children is important.
    """
    
    OffsetOrSize = 512
    """
    Special flag to indicate that this type will be used as a byte offset or byte size, which is used to
    control the formatting mode when the value is displayed in the UI.
    """
    

# Assign __doc__ for enum values for easier introspection

SDTypeFlags.NoFlags.__doc__ = """
This type has no special properties.
"""

SDTypeFlags.HasCustomString.__doc__ = """
This type has a custom string. This could be used for example for enums, to display the string
value of the enum as well as the integer storage, or perhaps for opaque types that should be
displayed to the user as a string even if the underlying representation is not a string.
"""

SDTypeFlags.Hidden.__doc__ = """
This type is considered an implementation detail and should not typically be displayed to the user.
"""

SDTypeFlags.Nullable.__doc__ = """
This type is nullable and can sometimes be removed and replaced simply with a Null type. See
:data:`SDBasic.Null`.
"""

SDTypeFlags.NullString.__doc__ = """
Special flag to indicate that this is a C-string which was NULL, not just empty.
"""

SDTypeFlags.FixedArray.__doc__ = """
Special flag to indicate that this is array was a fixed-size real array, rather than a complex
container type or a pointer & length.
"""

SDTypeFlags.Union.__doc__ = """
Special flag to indicate that this is structure is stored as a union, meaning all children share
the same memory and some external flag indicates which element is valid.
"""

SDTypeFlags.Important.__doc__ = """
Indicates that this object is important or significant, to aid in generating a summary/one-line
view of a particular chunk by only including important children.

This property can be recursive - so an important child which is a structure can have only some
members which are important.
"""

SDTypeFlags.ImportantChildren.__doc__ = """
Indicates that only important children should be processed, as noted in :data:`Important`. This
may appear on an object which has no important children - which indicates explicitly that there
are no important children so when summarising no parameters should be shown.
"""

SDTypeFlags.HiddenChildren.__doc__ = """
Indicates that some children are marked as hidden. This can be important for cases where the
number of children is important.
"""

SDTypeFlags.OffsetOrSize.__doc__ = """
Special flag to indicate that this type will be used as a byte offset or byte size, which is used to
control the formatting mode when the value is displayed in the UI.
"""

