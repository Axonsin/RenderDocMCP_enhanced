# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .DescriptorCategory import DescriptorCategory

class D3D12RootTableRange(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the structure of a single range within a root table definition. """
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
    def appended(self) -> bool:
        """
Whether or not this table was appended after the previous, leading to an auto-calculated
offset in :data:`tableByteOffset`.

:type: bool

"""
        pass

    @appended.setter
    def appended(self, value: bool):
        pass

    @property
    def baseRegister(self) -> int:
        """
The first register in this range.

:type: int

"""
        pass

    @baseRegister.setter
    def baseRegister(self, value: int):
        pass

    @property
    def category(self) -> DescriptorCategory:
        """
The descriptor category specified in this range.

:type: DescriptorCategory

"""
        pass

    @category.setter
    def category(self, value: DescriptorCategory):
        pass

    @property
    def count(self) -> int:
        """
The number of registers in this range.

:type: int

"""
        pass

    @count.setter
    def count(self, value: int):
        pass

    @property
    def space(self) -> int:
        """
The register space of this range.

:type: int

"""
        pass

    @space.setter
    def space(self, value: int):
        pass

    @property
    def tableByteOffset(self) -> int:
        """
The offset in bytes from the start of the table as defined in :class:`D3D12RootParam`.

:type: int

"""
        pass

    @tableByteOffset.setter
    def tableByteOffset(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55235950>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12RootTableRange' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12RootTableRange' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12RootTableRange' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12RootTableRange' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12RootTableRange' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12RootTableRange' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12RootTableRange' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12RootTableRange' objects>, 'count': <attribute 'count' of 'renderdoc.D3D12RootTableRange' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12RootTableRange' objects>, 'appended': <attribute 'appended' of 'renderdoc.D3D12RootTableRange' objects>, 'tableByteOffset': <attribute 'tableByteOffset' of 'renderdoc.D3D12RootTableRange' objects>, 'space': <attribute 'space' of 'renderdoc.D3D12RootTableRange' objects>, 'baseRegister': <attribute 'baseRegister' of 'renderdoc.D3D12RootTableRange' objects>, 'category': <attribute 'category' of 'renderdoc.D3D12RootTableRange' objects>, '__doc__': 'Contains the structure of a single range within a root table definition.'})"


