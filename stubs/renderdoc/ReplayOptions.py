# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .GPUVendor import GPUVendor
from .ReplayOptimisationLevel import ReplayOptimisationLevel

class ReplayOptions(): # skipped bases: <class 'SwigPyObject'>
    """ The options controlling how replay of a capture should be performed """
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
    def apiValidation(self) -> bool:
        """
Replay with API validation enabled and use debug messages from there, ignoring any
that may be contained in the capture.

The default is not to do any validation.

.. note:: RenderDoc does not handle invalid API use in the general case so validation should still
  be performed at runtime in your program for ground truth results.

:type: bool

"""
        pass

    @apiValidation.setter
    def apiValidation(self, value: bool):
        pass

    @property
    def forceGPUDeviceID(self) -> int:
        """
Force the selection of a GPU by device ID. This allows overriding which GPU is used to
replay on.

When set to 0, specifies no particular device.

See :data:`forceGPUDeviceID` for a full explanation of GPU selection override.

:type: int

"""
        pass

    @forceGPUDeviceID.setter
    def forceGPUDeviceID(self, value: int):
        pass

    @property
    def forceGPUDriverName(self) -> str:
        """
Force the selection of a GPU by driver name. This allows overriding which GPU is used
to replay on.

When set to an empty string, specifies no particular driver.

See :data:`forceGPUDeviceID` for a full explanation of GPU selection override.

:type: str

"""
        pass

    @forceGPUDriverName.setter
    def forceGPUDriverName(self, value: str):
        pass

    @property
    def forceGPUVendor(self) -> GPUVendor:
        """
Force the selection of a GPU by vendor ID. This allows overriding which GPU is used to
replay on, even if a different GPU would be the best match for the capture.

When set to :data:`GPUVendor.Unknown`, specifies no particular vendor.

See also :data:`forceGPUDeviceID` and :data:`forceGPUDriverName`. Available GPUs can be enumerated
using :meth:`CaptureAccess.GetAvailableGPUs`.

The default is not to do any override. The capture contains information about what GPU was used, and
the closest matching GPU is used on replay.

.. note::
  If a GPU is forced that is not available or not supported for a given capture, such as when GPUs
  are only available for some APIs and not others, the default GPU selection will be used. If a GPU
  is available for a capture but fails to open however then there is no fallback to a default GPU.

  OpenGL does not support GPU selection so the default method (which effectively does nothing) will
  always be used.

:type: GPUVendor

"""
        pass

    @forceGPUVendor.setter
    def forceGPUVendor(self, value: GPUVendor):
        pass

    @property
    def optimisation(self) -> ReplayOptimisationLevel:
        """
How much optimisation should be done, potentially at the cost of correctness.

The default is :data:`ReplayOptimisationLevel.Balanced`.

:type: ReplayOptimisationLevel

"""
        pass

    @optimisation.setter
    def optimisation(self, value: ReplayOptimisationLevel):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55204FE0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ReplayOptions' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ReplayOptions' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ReplayOptions' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ReplayOptions' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ReplayOptions' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ReplayOptions' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ReplayOptions' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ReplayOptions' objects>, 'forceGPUDeviceID': <attribute 'forceGPUDeviceID' of 'renderdoc.ReplayOptions' objects>, 'optimisation': <attribute 'optimisation' of 'renderdoc.ReplayOptions' objects>, 'apiValidation': <attribute 'apiValidation' of 'renderdoc.ReplayOptions' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ReplayOptions' objects>, 'forceGPUVendor': <attribute 'forceGPUVendor' of 'renderdoc.ReplayOptions' objects>, 'forceGPUDriverName': <attribute 'forceGPUDriverName' of 'renderdoc.ReplayOptions' objects>, '__doc__': 'The options controlling how replay of a capture should be performed'})"


