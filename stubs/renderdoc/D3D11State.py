# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .D3D11Shader import D3D11Shader
from .ResourceId import ResourceId
from .D3D11InputAssembly import D3D11InputAssembly
from .D3D11OutputMerger import D3D11OutputMerger
from .D3D11Predication import D3D11Predication
from .D3D11Rasterizer import D3D11Rasterizer
from .D3D11StreamOut import D3D11StreamOut

class D3D11State(): # skipped bases: <class 'SwigPyObject'>
    """ The full current D3D11 pipeline state. """
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
    def computeShader(self) -> D3D11Shader:
        """
The compute shader stage.

:type: D3D11Shader

"""
        pass

    @computeShader.setter
    def computeShader(self, value: D3D11Shader):
        pass

    @property
    def descriptorByteSize(self) -> int:
        """
The byte size of a descriptor in the virtual descriptor storage.

:type: int

"""
        pass

    @descriptorByteSize.setter
    def descriptorByteSize(self, value: int):
        pass

    @property
    def descriptorCount(self) -> int:
        """
The number of descriptors in the virtual descriptor storage.

:type: int

"""
        pass

    @descriptorCount.setter
    def descriptorCount(self, value: int):
        pass

    @property
    def descriptorStore(self) -> ResourceId:
        """
The virtual descriptor storage.

:type: ResourceId

"""
        pass

    @descriptorStore.setter
    def descriptorStore(self, value: ResourceId):
        pass

    @property
    def domainShader(self) -> D3D11Shader:
        """
The domain shader stage.

:type: D3D11Shader

"""
        pass

    @domainShader.setter
    def domainShader(self, value: D3D11Shader):
        pass

    @property
    def geometryShader(self) -> D3D11Shader:
        """
The geometry shader stage.

:type: D3D11Shader

"""
        pass

    @geometryShader.setter
    def geometryShader(self, value: D3D11Shader):
        pass

    @property
    def hullShader(self) -> D3D11Shader:
        """
The hull shader stage.

:type: D3D11Shader

"""
        pass

    @hullShader.setter
    def hullShader(self, value: D3D11Shader):
        pass

    @property
    def inputAssembly(self) -> D3D11InputAssembly:
        """
The input assembly pipeline stage.

:type: D3D11InputAssembly

"""
        pass

    @inputAssembly.setter
    def inputAssembly(self, value: D3D11InputAssembly):
        pass

    @property
    def outputMerger(self) -> D3D11OutputMerger:
        """
The output merger pipeline stage.

:type: D3D11OutputMerger

"""
        pass

    @outputMerger.setter
    def outputMerger(self, value: D3D11OutputMerger):
        pass

    @property
    def pixelShader(self) -> D3D11Shader:
        """
The pixel shader stage.

:type: D3D11Shader

"""
        pass

    @pixelShader.setter
    def pixelShader(self, value: D3D11Shader):
        pass

    @property
    def predication(self) -> D3D11Predication:
        """
The predicated rendering state.

:type: D3D11Predication

"""
        pass

    @predication.setter
    def predication(self, value: D3D11Predication):
        pass

    @property
    def rasterizer(self) -> D3D11Rasterizer:
        """
The rasterizer pipeline stage.

:type: D3D11Rasterizer

"""
        pass

    @rasterizer.setter
    def rasterizer(self, value: D3D11Rasterizer):
        pass

    @property
    def streamOut(self) -> D3D11StreamOut:
        """
The stream-out pipeline stage.

:type: D3D11StreamOut

"""
        pass

    @streamOut.setter
    def streamOut(self, value: D3D11StreamOut):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vertexShader(self) -> D3D11Shader:
        """
The vertex shader stage.

:type: D3D11Shader

"""
        pass

    @vertexShader.setter
    def vertexShader(self, value: D3D11Shader):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5520A390>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D11State' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D11State' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D11State' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D11State' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D11State' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D11State' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D11State' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D11State' objects>, 'streamOut': <attribute 'streamOut' of 'renderdoc.D3D11State' objects>, 'outputMerger': <attribute 'outputMerger' of 'renderdoc.D3D11State' objects>, 'predication': <attribute 'predication' of 'renderdoc.D3D11State' objects>, 'descriptorStore': <attribute 'descriptorStore' of 'renderdoc.D3D11State' objects>, 'descriptorCount': <attribute 'descriptorCount' of 'renderdoc.D3D11State' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D11State' objects>, 'inputAssembly': <attribute 'inputAssembly' of 'renderdoc.D3D11State' objects>, 'geometryShader': <attribute 'geometryShader' of 'renderdoc.D3D11State' objects>, 'computeShader': <attribute 'computeShader' of 'renderdoc.D3D11State' objects>, 'descriptorByteSize': <attribute 'descriptorByteSize' of 'renderdoc.D3D11State' objects>, 'rasterizer': <attribute 'rasterizer' of 'renderdoc.D3D11State' objects>, 'vertexShader': <attribute 'vertexShader' of 'renderdoc.D3D11State' objects>, 'hullShader': <attribute 'hullShader' of 'renderdoc.D3D11State' objects>, 'domainShader': <attribute 'domainShader' of 'renderdoc.D3D11State' objects>, 'pixelShader': <attribute 'pixelShader' of 'renderdoc.D3D11State' objects>, '__doc__': 'The full current D3D11 pipeline state.'})"


