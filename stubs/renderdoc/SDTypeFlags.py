# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class SDTypeFlags(__enum.IntFlag):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    FixedArray = 16
    """
    Special flag to indicate that this is array was a fixed-size real array, rather than a complex
      container type or a pointer & length.
    """

    HasCustomString = 1
    """
    This type has a custom string. This could be used for example for enums, to display the string
      value of the enum as well as the integer storage, or perhaps for opaque types that should be
      displayed to the user as a string even if the underlying representation is not a string.
    """

    Hidden = 2
    """ This type is considered an implementation detail and should not typically be displayed to the user. """

    HiddenChildren = 256
    """
    Indicates that some children are marked as hidden. This can be important for cases where the
      number of children is important.
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

    NoFlags = 0
    """ This type has no special properties. """

    Nullable = 4
    """
    This type is nullable and can sometimes be removed and replaced simply with a Null type. See
      :data:`SDBasic.Null`.
    """

    NullString = 8
    """ Special flag to indicate that this is a C-string which was NULL, not just empty. """

    OffsetOrSize = 512
    """
    Special flag to indicate that this type will be used as a byte offset or byte size, which is used to 
      control the formatting mode when the value is displayed in the UI.
    """

    Union = 32
    """
    Special flag to indicate that this is structure is stored as a union, meaning all children share
      the same memory and some external flag indicates which element is valid.
    """



