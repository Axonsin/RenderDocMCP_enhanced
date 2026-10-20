from ._CompareFunction import CompareFunction
from ._ModificationValue import ModificationValue

from typing import overload

class PixelModification():
    # Original docstring
    """
    An attempt to modify a pixel by a particular event.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised PixelModification.
        """
        pass
    
    @overload
    def __init__(self, other: 'PixelModification'):
        """
        Construct a new PixelModification with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def Passed(self) -> bool:
        """
        Determine if this fragment passed all tests and wrote to the texture.
        
        :return: ``True`` if it passed all tests, ``False`` if it failed any.
        :rtype: bool
        """
        pass
    
    
    def CheckDepthTestQuantised(self, depthBits: int, depthFunc: CompareFunction):
        """
        Update the depth-test failure state based on known shader output depth value and
        :data:`preMod` reference value, quantised to a certain number of depth bits with epsilon.
        
        This is primarily used internally and should not be needed to be called externally.
        
        :param int depthBits: How many bits are in the depth buffer: 16, 24 or 32.
        :param CompareFunction depthFunc: The comparison function active for the depth test
        """
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
    def stencilTestFailed(self) -> bool:
        """
        ``True`` if stencil testing eliminated this fragment.
        
        :type: bool
        """
        pass
    
    @stencilTestFailed.setter
    def stencilTestFailed(self, value: bool):
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
    def viewClipped(self) -> bool:
        """
        ``True`` if viewport clipping eliminated this fragment.
        
        :type: bool
        """
        pass
    
    @viewClipped.setter
    def viewClipped(self, value: bool):
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
    
