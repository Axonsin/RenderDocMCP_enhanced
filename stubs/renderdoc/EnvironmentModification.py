# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .EnvMod import EnvMod
from .EnvSep import EnvSep

class EnvironmentModification(): # skipped bases: <class 'SwigPyObject'>
    """ A modification to a single environment variable. """
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
    def mod(self) -> EnvMod:
        """
The :class:`modification <EnvMod>` to use.

:type: EnvMod

"""
        pass

    @mod.setter
    def mod(self, value: EnvMod):
        pass

    @property
    def name(self) -> str:
        """
The name of the environment variable.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    @property
    def sep(self) -> EnvSep:
        """
The :class:`separator <EnvSep>` to use if needed.

:type: EnvSep

"""
        pass

    @sep.setter
    def sep(self, value: EnvSep):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def value(self) -> str:
        """
The value to use with the modification specified in :data:`mod`.

:type: str

"""
        pass

    @value.setter
    def value(self, value: str):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55207460>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.EnvironmentModification' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.EnvironmentModification' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.EnvironmentModification' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.EnvironmentModification' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.EnvironmentModification' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.EnvironmentModification' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.EnvironmentModification' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.EnvironmentModification' objects>, 'value': <attribute 'value' of 'renderdoc.EnvironmentModification' objects>, 'name': <attribute 'name' of 'renderdoc.EnvironmentModification' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.EnvironmentModification' objects>, 'mod': <attribute 'mod' of 'renderdoc.EnvironmentModification' objects>, 'sep': <attribute 'sep' of 'renderdoc.EnvironmentModification' objects>, '__doc__': 'A modification to a single environment variable.'})"


