# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .DescriptorCategory import DescriptorCategory

class ShaderBindIndex(): # skipped bases: <class 'SwigPyObject'>
    """
    References a particular individual binding element in a shader interface.
    
    This is the shader interface side of a :class:`DescriptorAccess` and so can be compared to one to
    check if an access refers to a given index or not.
    
    The context of which shader reflection this index refers to must be provided to properly interpret
    this information, as it is relative to a particular :class:`ShaderReflection`.
    """
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
    def arrayElement(self) -> int:
        """
If the binding identified by :data:`category` and :data:`index` is arrayed, this
identifies the particular array index being referred to.

:type: int

"""
        pass

    @arrayElement.setter
    def arrayElement(self, value: int):
        pass

    @property
    def category(self) -> DescriptorCategory:
        """
The type of binding this refers to, with each category referring to a different
shader interface in the :data:`ShaderReflection`.

:type: DescriptorCategory

"""
        pass

    @category.setter
    def category(self, value: DescriptorCategory):
        pass

    @property
    def index(self) -> int:
        """
The index within the given :data:`category` for the binding.

:type: int

"""
        pass

    @index.setter
    def index(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551CCBD0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderBindIndex' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderBindIndex' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderBindIndex' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderBindIndex' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderBindIndex' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderBindIndex' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderBindIndex' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderBindIndex' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderBindIndex' objects>, 'category': <attribute 'category' of 'renderdoc.ShaderBindIndex' objects>, 'index': <attribute 'index' of 'renderdoc.ShaderBindIndex' objects>, 'arrayElement': <attribute 'arrayElement' of 'renderdoc.ShaderBindIndex' objects>, '__doc__': '\\nReferences a particular individual binding element in a shader interface.\\n\\nThis is the shader interface side of a :class:`DescriptorAccess` and so can be compared to one to\\ncheck if an access refers to a given index or not.\\n\\nThe context of which shader reflection this index refers to must be provided to properly interpret\\nthis information, as it is relative to a particular :class:`ShaderReflection`.\\n\\n'})"


