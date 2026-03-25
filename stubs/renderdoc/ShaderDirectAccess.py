# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId
from .DescriptorType import DescriptorType

class ShaderDirectAccess(): # skipped bases: <class 'SwigPyObject'>
    """ References a particular resource accessed via the shader using direct heap access (as opposed to a direct binding). """
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
    def byteOffset(self) -> int:
        """
The offset in bytes to the descriptor in the descriptor store.

:type: int

"""
        pass

    @byteOffset.setter
    def byteOffset(self, value: int):
        pass

    @property
    def byteSize(self) -> int:
        """
The size in bytes of the descriptor.

:type: int

"""
        pass

    @byteSize.setter
    def byteSize(self, value: int):
        pass

    @property
    def descriptorStore(self) -> ResourceId:
        """
The backing storage of the descriptor.

:type: ResourceId

"""
        pass

    @descriptorStore.setter
    def descriptorStore(self, value: ResourceId):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> DescriptorType:
        """
The type of the resource being accessed.

:type: DescriptorType

"""
        pass

    @type.setter
    def type(self, value: DescriptorType):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552087C0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderDirectAccess' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderDirectAccess' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderDirectAccess' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderDirectAccess' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderDirectAccess' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderDirectAccess' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderDirectAccess' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderDirectAccess' objects>, 'descriptorStore': <attribute 'descriptorStore' of 'renderdoc.ShaderDirectAccess' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderDirectAccess' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.ShaderDirectAccess' objects>, 'type': <attribute 'type' of 'renderdoc.ShaderDirectAccess' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.ShaderDirectAccess' objects>, '__doc__': '\\nReferences a particular resource accessed via the shader using direct heap access (as opposed to a direct binding).\\n\\n\\n'})"


