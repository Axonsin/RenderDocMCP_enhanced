# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderPixelMessageLocation(): # skipped bases: <class 'SwigPyObject'>
    """
    A pixel shader message's location.
    
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
The generating primitive, or :data:`NoLocation` if the primitive ID is unavailable.

:type: int

"""
        pass

    @primitive.setter
    def primitive(self, value: int):
        pass

    @property
    def sample(self) -> int:
        """
The sample, or :data:`NoLocation` if sample shading is disabled.

:type: int

"""
        pass

    @sample.setter
    def sample(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def view(self) -> int:
        """
The multiview view for this fragment, or ``0`` if multiview is disabled.

:type: int

"""
        pass

    @view.setter
    def view(self, value: int):
        pass

    @property
    def x(self) -> int:
        """
The x co-ordinate of the pixel.

:type: int

"""
        pass

    @x.setter
    def x(self, value: int):
        pass

    @property
    def y(self) -> int:
        """
The y co-ordinate of the pixel.

:type: int

"""
        pass

    @y.setter
    def y(self, value: int):
        pass


    NoLocation = 4294967295
    __dict__ = None # (!) real value is 'mappingproxy({\'NoLocation\': 4294967295, \'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D7820>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'x\': <attribute \'x\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'y\': <attribute \'y\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'view\': <attribute \'view\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'primitive\': <attribute \'primitive\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'sample\': <attribute \'sample\' of \'renderdoc.ShaderPixelMessageLocation\' objects>, \'__doc__\': "\\nA pixel shader message\'s location.\\n\\n.. data:: NoLocation\\n\\n  No frame number is available.\\n\\n"})'


