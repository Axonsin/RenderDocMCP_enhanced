# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderGeometryMessageLocation(): # skipped bases: <class 'SwigPyObject'>
    """
    A geometry shader message's location.
    
    .. data:: NoLocation
    
      No frame number is available.
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
    def primitive(self) -> int:
        """
The primitive index

:type: int

"""
        pass

    @primitive.setter
    def primitive(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def view(self) -> int:
        """
The multiview view for this primitive, or ``0`` if multiview is disabled.

:type: int

"""
        pass

    @view.setter
    def view(self, value: int):
        pass


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551C4DB0>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'view\': <attribute \'view\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'primitive\': <attribute \'primitive\' of \'renderdoc.ShaderGeometryMessageLocation\' objects>, \'__doc__\': "\\nA geometry shader message\'s location.\\n\\n.. data:: NoLocation\\n\\n  No frame number is available.\\n\\n"})'


