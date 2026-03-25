# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ExtensionMetadata(): # skipped bases: <class 'SwigPyObject'>
    """ The metadata for an extension. """
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
    def author(self) -> str:
        """
The author of the extension, optionally with an email contact

:type: str

"""
        pass

    @author.setter
    def author(self, value: str):
        pass

    @property
    def description(self) -> str:
        """
A longer description of what the extension does

:type: str

"""
        pass

    @description.setter
    def description(self, value: str):
        pass

    @property
    def extensionAPI(self) -> int:
        """
The version of the extension API that this extension is written against

:type: int

"""
        pass

    @extensionAPI.setter
    def extensionAPI(self, value: int):
        pass

    @property
    def extensionURL(self) -> str:
        """
The URL for where the extension is fetched from

:type: str

"""
        pass

    @extensionURL.setter
    def extensionURL(self, value: str):
        pass

    @property
    def filePath(self) -> str:
        """
The location of this package on disk

:type: str

"""
        pass

    @filePath.setter
    def filePath(self, value: str):
        pass

    @property
    def name(self) -> str:
        """
The short friendly name for the extension

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    @property
    def package(self) -> str:
        """
The python package for this extension, e.g. foo.bar

:type: str

"""
        pass

    @package.setter
    def package(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def version(self) -> str:
        """
The version of the extension

:type: str

"""
        pass

    @version.setter
    def version(self, value: str):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50130A60>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.ExtensionMetadata' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.ExtensionMetadata' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.ExtensionMetadata' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.ExtensionMetadata' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.ExtensionMetadata' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.ExtensionMetadata' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.ExtensionMetadata' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.ExtensionMetadata' objects>, 'package': <attribute 'package' of 'qrenderdoc.ExtensionMetadata' objects>, 'version': <attribute 'version' of 'qrenderdoc.ExtensionMetadata' objects>, 'description': <attribute 'description' of 'qrenderdoc.ExtensionMetadata' objects>, 'extensionAPI': <attribute 'extensionAPI' of 'qrenderdoc.ExtensionMetadata' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.ExtensionMetadata' objects>, 'author': <attribute 'author' of 'qrenderdoc.ExtensionMetadata' objects>, 'extensionURL': <attribute 'extensionURL' of 'qrenderdoc.ExtensionMetadata' objects>, 'name': <attribute 'name' of 'qrenderdoc.ExtensionMetadata' objects>, 'filePath': <attribute 'filePath' of 'qrenderdoc.ExtensionMetadata' objects>, '__doc__': 'The metadata for an extension.'})"


