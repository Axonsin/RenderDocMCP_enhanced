# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .LineColumnInfo import LineColumnInfo
from .SourceVariableMapping import SourceVariableMapping

class InstructionSourceInfo(): # skipped bases: <class 'SwigPyObject'>
    """
    Gives per-instruction source code mapping information, including what line(s) correspond
    to this instruction and which source variables exist
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
    def instruction(self) -> int:
        """
The instruction that this information is for.

:type: int

"""
        pass

    @instruction.setter
    def instruction(self, value: int):
        pass

    @property
    def lineInfo(self) -> LineColumnInfo:
        """
The source location that this instruction corresponds to

:type: LineColumnInfo

"""
        pass

    @lineInfo.setter
    def lineInfo(self, value: LineColumnInfo):
        pass

    @property
    def sourceVars(self) -> List[SourceVariableMapping]:
        """
An optional mapping of which high-level source variables map to which debug variables
and including extra type information.

This list contains source variable mapping that is only valid at this instruction, and is fully
complete & redundant including all previous source variables that are still valid at this
instruction.

:type: List[SourceVariableMapping]

"""
        pass

    @sourceVars.setter
    def sourceVars(self, value: List[SourceVariableMapping]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55237BB0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.InstructionSourceInfo' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.InstructionSourceInfo' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.InstructionSourceInfo' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.InstructionSourceInfo' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.InstructionSourceInfo' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.InstructionSourceInfo' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.InstructionSourceInfo' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.InstructionSourceInfo' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.InstructionSourceInfo' objects>, 'lineInfo': <attribute 'lineInfo' of 'renderdoc.InstructionSourceInfo' objects>, 'sourceVars': <attribute 'sourceVars' of 'renderdoc.InstructionSourceInfo' objects>, 'instruction': <attribute 'instruction' of 'renderdoc.InstructionSourceInfo' objects>, '__doc__': '\\nGives per-instruction source code mapping information, including what line(s) correspond\\nto this instruction and which source variables exist\\n\\n'})"


