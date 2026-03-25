# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VulkanLayerFlags import VulkanLayerFlags

class VulkanLayerRegistrationInfo(): # skipped bases: <class 'SwigPyObject'>
    """ INTERNAL: Information about vulkan layer registration """
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
    def flags(self) -> VulkanLayerFlags:
        """
:class:`VulkanLayerFlags` detailing the current registration.

:type: VulkanLayerFlags

"""
        pass

    @flags.setter
    def flags(self, value: VulkanLayerFlags):
        pass

    @property
    def myJSONs(self) -> List[str]:
        """
A list of jsons that should be registered

:type: List[str]

"""
        pass

    @myJSONs.setter
    def myJSONs(self, value: List[str]):
        pass

    @property
    def otherJSONs(self) -> List[str]:
        """
A list of jsons that should be unregistered / updated

:type: List[str]

"""
        pass

    @otherJSONs.setter
    def otherJSONs(self, value: List[str]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55230D90>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, 'flags': <attribute 'flags' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, 'myJSONs': <attribute 'myJSONs' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, 'otherJSONs': <attribute 'otherJSONs' of 'renderdoc.VulkanLayerRegistrationInfo' objects>, '__doc__': 'INTERNAL: Information about vulkan layer registration'})"


