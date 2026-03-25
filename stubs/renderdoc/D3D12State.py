# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .D3D12Shader import D3D12Shader
from .ResourceId import ResourceId
from .D3D12InputAssembly import D3D12InputAssembly
from .D3D12OM import D3D12OM
from .D3D12Predication import D3D12Predication
from .D3D12Rasterizer import D3D12Rasterizer
from .D3D12ResourceData import D3D12ResourceData
from .D3D12RootSignature import D3D12RootSignature
from .D3D12StreamOut import D3D12StreamOut

class D3D12State(): # skipped bases: <class 'SwigPyObject'>
    """ The full current D3D12 pipeline state. """
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
    def ampShader(self) -> D3D12Shader:
        """
The amplification shader stage.

:type: D3D12Shader

"""
        pass

    @ampShader.setter
    def ampShader(self, value: D3D12Shader):
        pass

    @property
    def computeShader(self) -> D3D12Shader:
        """
The compute shader stage.

:type: D3D12Shader

"""
        pass

    @computeShader.setter
    def computeShader(self, value: D3D12Shader):
        pass

    @property
    def descriptorHeaps(self) -> List[ResourceId]:
        """
The descriptor heaps currently bound.

:type: List[ResourceId]

"""
        pass

    @descriptorHeaps.setter
    def descriptorHeaps(self, value: List[ResourceId]):
        pass

    @property
    def domainShader(self) -> D3D12Shader:
        """
The domain shader stage.

:type: D3D12Shader

"""
        pass

    @domainShader.setter
    def domainShader(self, value: D3D12Shader):
        pass

    @property
    def geometryShader(self) -> D3D12Shader:
        """
The geometry shader stage.

:type: D3D12Shader

"""
        pass

    @geometryShader.setter
    def geometryShader(self, value: D3D12Shader):
        pass

    @property
    def hullShader(self) -> D3D12Shader:
        """
The hull shader stage.

:type: D3D12Shader

"""
        pass

    @hullShader.setter
    def hullShader(self, value: D3D12Shader):
        pass

    @property
    def inputAssembly(self) -> D3D12InputAssembly:
        """
The input assembly pipeline stage.

:type: D3D12InputAssembly

"""
        pass

    @inputAssembly.setter
    def inputAssembly(self, value: D3D12InputAssembly):
        pass

    @property
    def meshShader(self) -> D3D12Shader:
        """
The mesh shader stage.

:type: D3D12Shader

"""
        pass

    @meshShader.setter
    def meshShader(self, value: D3D12Shader):
        pass

    @property
    def outputMerger(self) -> D3D12OM:
        """
The output merger pipeline stage.

:type: D3D12OM

"""
        pass

    @outputMerger.setter
    def outputMerger(self, value: D3D12OM):
        pass

    @property
    def pipelineResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the pipeline state object.

:type: ResourceId

"""
        pass

    @pipelineResourceId.setter
    def pipelineResourceId(self, value: ResourceId):
        pass

    @property
    def pixelShader(self) -> D3D12Shader:
        """
The pixel shader stage.

:type: D3D12Shader

"""
        pass

    @pixelShader.setter
    def pixelShader(self, value: D3D12Shader):
        pass

    @property
    def predication(self) -> D3D12Predication:
        """
The predicated rendering state.

:type: D3D12Predication

"""
        pass

    @predication.setter
    def predication(self, value: D3D12Predication):
        pass

    @property
    def rasterizer(self) -> D3D12Rasterizer:
        """
The rasterizer pipeline stage.

:type: D3D12Rasterizer

"""
        pass

    @rasterizer.setter
    def rasterizer(self, value: D3D12Rasterizer):
        pass

    @property
    def resourceStates(self) -> List[D3D12ResourceData]:
        """
The resource states for the currently live resources.

:type: List[D3D12ResourceData]

"""
        pass

    @resourceStates.setter
    def resourceStates(self, value: List[D3D12ResourceData]):
        pass

    @property
    def rootSignature(self) -> D3D12RootSignature:
        """
Details of the root signature structure and root parameters.

:type: D3D12RootSignature

"""
        pass

    @rootSignature.setter
    def rootSignature(self, value: D3D12RootSignature):
        pass

    @property
    def streamOut(self) -> D3D12StreamOut:
        """
The stream-out pipeline stage.

:type: D3D12StreamOut

"""
        pass

    @streamOut.setter
    def streamOut(self, value: D3D12StreamOut):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vertexShader(self) -> D3D12Shader:
        """
The vertex shader stage.

:type: D3D12Shader

"""
        pass

    @vertexShader.setter
    def vertexShader(self, value: D3D12Shader):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5521F970>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12State' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12State' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12State' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12State' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12State' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12State' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12State' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12State' objects>, 'streamOut': <attribute 'streamOut' of 'renderdoc.D3D12State' objects>, 'outputMerger': <attribute 'outputMerger' of 'renderdoc.D3D12State' objects>, 'predication': <attribute 'predication' of 'renderdoc.D3D12State' objects>, 'pipelineResourceId': <attribute 'pipelineResourceId' of 'renderdoc.D3D12State' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12State' objects>, 'rootSignature': <attribute 'rootSignature' of 'renderdoc.D3D12State' objects>, 'inputAssembly': <attribute 'inputAssembly' of 'renderdoc.D3D12State' objects>, 'geometryShader': <attribute 'geometryShader' of 'renderdoc.D3D12State' objects>, 'computeShader': <attribute 'computeShader' of 'renderdoc.D3D12State' objects>, 'resourceStates': <attribute 'resourceStates' of 'renderdoc.D3D12State' objects>, 'descriptorHeaps': <attribute 'descriptorHeaps' of 'renderdoc.D3D12State' objects>, 'rasterizer': <attribute 'rasterizer' of 'renderdoc.D3D12State' objects>, 'vertexShader': <attribute 'vertexShader' of 'renderdoc.D3D12State' objects>, 'hullShader': <attribute 'hullShader' of 'renderdoc.D3D12State' objects>, 'domainShader': <attribute 'domainShader' of 'renderdoc.D3D12State' objects>, 'pixelShader': <attribute 'pixelShader' of 'renderdoc.D3D12State' objects>, 'ampShader': <attribute 'ampShader' of 'renderdoc.D3D12State' objects>, 'meshShader': <attribute 'meshShader' of 'renderdoc.D3D12State' objects>, '__doc__': 'The full current D3D12 pipeline state.'})"


