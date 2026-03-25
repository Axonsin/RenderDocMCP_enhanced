# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .CompareFunction import CompareFunction
from .ModificationValue import ModificationValue

class PixelModification(): # skipped bases: <class 'SwigPyObject'>
    """ An attempt to modify a pixel by a particular event. """
    def CheckDepthTestQuantised(self, depthBits: int, depthFunc: CompareFunction): # real signature unknown; restored from __doc__
        """
        CheckDepthTestQuantised(depthBits, depthFunc)
        
        Update the depth-test failure state based on known shader output depth value and
        preMod reference value, quantised to a certain number of depth bits with epsilon.
        
        This is primarily used internally and should not be needed to be called externally.
        
        :param int depthBits: How many bits are in the depth buffer: 16, 24 or 32.
        :param CompareFunction depthFunc: The comparison function active for the depth test
        """
        pass

    def Passed(self) -> bool: # real signature unknown; restored from __doc__
        """
        Passed()
        
        Determine if this fragment passed all tests and wrote to the texture.
        
        :return: ``True`` if it passed all tests, ``False`` if it failed any.
        :rtype: bool
        """
        pass

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
    def backfaceCulled(self) -> bool:
        """
``True`` if the backface culling test eliminated this fragment.

:type: bool

"""
        pass

    @backfaceCulled.setter
    def backfaceCulled(self, value: bool):
        pass

    @property
    def depthBoundsFailed(self) -> bool:
        """
``True`` if depth bounds clipping eliminated this fragment.

:type: bool

"""
        pass

    @depthBoundsFailed.setter
    def depthBoundsFailed(self, value: bool):
        pass

    @property
    def depthClipped(self) -> bool:
        """
``True`` if depth near/far clipping eliminated this fragment.

:type: bool

"""
        pass

    @depthClipped.setter
    def depthClipped(self, value: bool):
        pass

    @property
    def depthTestFailed(self) -> bool:
        """
``True`` if depth testing eliminated this fragment.

:type: bool

"""
        pass

    @depthTestFailed.setter
    def depthTestFailed(self, value: bool):
        pass

    @property
    def directShaderWrite(self) -> bool:
        """
``True`` if this event came as part of an arbitrary shader write.

:type: bool

"""
        pass

    @directShaderWrite.setter
    def directShaderWrite(self, value: bool):
        pass

    @property
    def eventId(self) -> int:
        """
The :data:`eventId <APIEvent.eventId>` where the modification happened.

:type: int

"""
        pass

    @eventId.setter
    def eventId(self, value: int):
        pass

    @property
    def fragIndex(self) -> int:
        """
A 0-based index of which fragment this modification corresponds to, in the case that
multiple fragments from a single action wrote to a pixel.

:type: int

"""
        pass

    @fragIndex.setter
    def fragIndex(self, value: int):
        pass

    @property
    def postMod(self) -> ModificationValue:
        """
The value of the texture after this fragment ran.

:type: ModificationValue

"""
        pass

    @postMod.setter
    def postMod(self, value: ModificationValue):
        pass

    @property
    def predicationSkipped(self) -> bool:
        """
``True`` if predicated rendering skipped this call.

:type: bool

"""
        pass

    @predicationSkipped.setter
    def predicationSkipped(self, value: bool):
        pass

    @property
    def preMod(self) -> ModificationValue:
        """
The value of the texture before this fragment ran.

This is valid only for the first fragment if multiple fragments in the same event write to the same
pixel.

:type: ModificationValue

"""
        pass

    @preMod.setter
    def preMod(self, value: ModificationValue):
        pass

    @property
    def primitiveID(self) -> int:
        """
The primitive that generated this fragment.

:type: int

"""
        pass

    @primitiveID.setter
    def primitiveID(self, value: int):
        pass

    @property
    def sampleMasked(self) -> bool:
        """
``True`` if the sample mask eliminated this fragment.

:type: bool

"""
        pass

    @sampleMasked.setter
    def sampleMasked(self, value: bool):
        pass

    @property
    def scissorClipped(self) -> bool:
        """
``True`` if scissor clipping eliminated this fragment.

:type: bool

"""
        pass

    @scissorClipped.setter
    def scissorClipped(self, value: bool):
        pass

    @property
    def shaderDiscarded(self) -> bool:
        """
``True`` if the pixel shader executed a discard on this fragment.

:type: bool

"""
        pass

    @shaderDiscarded.setter
    def shaderDiscarded(self, value: bool):
        pass

    @property
    def shaderOut(self) -> ModificationValue:
        """
The value that this fragment wrote from the pixel shader.

:type: ModificationValue

"""
        pass

    @shaderOut.setter
    def shaderOut(self, value: ModificationValue):
        pass

    @property
    def stencilTestFailed(self) -> bool:
        """
``True`` if stencil testing eliminated this fragment.

:type: bool

"""
        pass

    @stencilTestFailed.setter
    def stencilTestFailed(self, value: bool):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def unboundPS(self) -> bool:
        """
``True`` if no pixel shader was bound at this event. On D3D APIs this may also mean
a pixel shader exists but declares no output for the corresponding target and so is skipped.

On other APIs this is only reported if the pixel shader is entirely unbound but this means the
output may have undefined values.

:type: bool

"""
        pass

    @unboundPS.setter
    def unboundPS(self, value: bool):
        pass

    @property
    def viewClipped(self) -> bool:
        """
``True`` if viewport clipping eliminated this fragment.

:type: bool

"""
        pass

    @viewClipped.setter
    def viewClipped(self, value: bool):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551D11A0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.PixelModification' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.PixelModification' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.PixelModification' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.PixelModification' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.PixelModification' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.PixelModification' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.PixelModification' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.PixelModification' objects>, 'Passed': <method 'Passed' of 'renderdoc.PixelModification' objects>, 'CheckDepthTestQuantised': <method 'CheckDepthTestQuantised' of 'renderdoc.PixelModification' objects>, 'depthTestFailed': <attribute 'depthTestFailed' of 'renderdoc.PixelModification' objects>, 'stencilTestFailed': <attribute 'stencilTestFailed' of 'renderdoc.PixelModification' objects>, 'postMod': <attribute 'postMod' of 'renderdoc.PixelModification' objects>, 'directShaderWrite': <attribute 'directShaderWrite' of 'renderdoc.PixelModification' objects>, 'preMod': <attribute 'preMod' of 'renderdoc.PixelModification' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.PixelModification' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.PixelModification' objects>, 'fragIndex': <attribute 'fragIndex' of 'renderdoc.PixelModification' objects>, 'shaderOut': <attribute 'shaderOut' of 'renderdoc.PixelModification' objects>, 'shaderDiscarded': <attribute 'shaderDiscarded' of 'renderdoc.PixelModification' objects>, 'sampleMasked': <attribute 'sampleMasked' of 'renderdoc.PixelModification' objects>, 'depthBoundsFailed': <attribute 'depthBoundsFailed' of 'renderdoc.PixelModification' objects>, 'predicationSkipped': <attribute 'predicationSkipped' of 'renderdoc.PixelModification' objects>, 'primitiveID': <attribute 'primitiveID' of 'renderdoc.PixelModification' objects>, 'backfaceCulled': <attribute 'backfaceCulled' of 'renderdoc.PixelModification' objects>, 'unboundPS': <attribute 'unboundPS' of 'renderdoc.PixelModification' objects>, 'depthClipped': <attribute 'depthClipped' of 'renderdoc.PixelModification' objects>, 'viewClipped': <attribute 'viewClipped' of 'renderdoc.PixelModification' objects>, 'scissorClipped': <attribute 'scissorClipped' of 'renderdoc.PixelModification' objects>, '__doc__': 'An attempt to modify a pixel by a particular event.'})"


