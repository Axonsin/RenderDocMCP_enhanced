# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .DescriptorAccess import DescriptorAccess
from .Descriptor import Descriptor
from .SamplerDescriptor import SamplerDescriptor

class UsedDescriptor(): # skipped bases: <class 'SwigPyObject'>
    """
    Combined information about a single descriptor that has been used, both the information
    about its access and its contents.
    
    This is a helper struct for the common pipeline state abstraction to trade off simplicity of access
    against optimal access.
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
    def access(self) -> DescriptorAccess:
        """
The access information of which shader reflection object accessed which descriptor.

:type: DescriptorAccess

"""
        pass

    @access.setter
    def access(self, value: DescriptorAccess):
        pass

    @property
    def descriptor(self) -> Descriptor:
        """
The contents of the accessed descriptor, if it is a normal non-sampler descriptor.

For sampler descriptors this is empty.

:type: Descriptor

"""
        pass

    @descriptor.setter
    def descriptor(self, value: Descriptor):
        pass

    @property
    def sampler(self) -> SamplerDescriptor:
        """
The contents of the accessed descriptor, if it is a sampler descriptor.

For normal descriptors this is empty.

:type: SamplerDescriptor

"""
        pass

    @sampler.setter
    def sampler(self, value: SamplerDescriptor):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD552044A0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.UsedDescriptor' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.UsedDescriptor' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.UsedDescriptor' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.UsedDescriptor' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.UsedDescriptor' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.UsedDescriptor' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.UsedDescriptor' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.UsedDescriptor' objects>, 'descriptor': <attribute 'descriptor' of 'renderdoc.UsedDescriptor' objects>, 'sampler': <attribute 'sampler' of 'renderdoc.UsedDescriptor' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.UsedDescriptor' objects>, 'access': <attribute 'access' of 'renderdoc.UsedDescriptor' objects>, '__doc__': '\\nCombined information about a single descriptor that has been used, both the information\\nabout its access and its contents.\\n\\nThis is a helper struct for the common pipeline state abstraction to trade off simplicity of access\\nagainst optimal access.\\n\\n'})"


