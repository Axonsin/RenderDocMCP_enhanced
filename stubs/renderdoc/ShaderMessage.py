# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderMessageLocation import ShaderMessageLocation
from .ShaderStage import ShaderStage

class ShaderMessage(): # skipped bases: <class 'SwigPyObject'>
    """ A shader printed message. """
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
    def disassemblyLine(self) -> int:
        """
The line (starting from 1) of the disassembly where this message came from, or -1 if
it is not associated with any line.

:type: int

"""
        pass

    @disassemblyLine.setter
    def disassemblyLine(self, value: int):
        pass

    @property
    def location(self) -> ShaderMessageLocation:
        """
The location (thread/invocation) of the shader that this message comes from.

:type: ShaderMessageLocation

"""
        pass

    @location.setter
    def location(self, value: ShaderMessageLocation):
        pass

    @property
    def message(self) -> str:
        """
The formatted message.

:type: str

"""
        pass

    @message.setter
    def message(self, value: str):
        pass

    @property
    def stage(self) -> ShaderStage:
        """
The shader stage this message comes from.

:type: ShaderStage

"""
        pass

    @stage.setter
    def stage(self, value: ShaderStage):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5520CB70>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderMessage' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderMessage' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderMessage' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderMessage' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderMessage' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderMessage' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderMessage' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderMessage' objects>, 'disassemblyLine': <attribute 'disassemblyLine' of 'renderdoc.ShaderMessage' objects>, 'location': <attribute 'location' of 'renderdoc.ShaderMessage' objects>, 'stage': <attribute 'stage' of 'renderdoc.ShaderMessage' objects>, 'message': <attribute 'message' of 'renderdoc.ShaderMessage' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderMessage' objects>, '__doc__': 'A shader printed message.'})"


