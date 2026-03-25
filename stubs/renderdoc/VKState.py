# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKColorBlendState import VKColorBlendState
from .VKPipeline import VKPipeline
from .VKShader import VKShader
from .VKConditionalRendering import VKConditionalRendering
from .VKCurrentPass import VKCurrentPass
from .VKDepthStencil import VKDepthStencil
from .VKImageData import VKImageData
from .VKInputAssembly import VKInputAssembly
from .VKMultiSample import VKMultiSample
from .VKRasterizer import VKRasterizer
from .ShaderMessage import ShaderMessage
from .VKTessellation import VKTessellation
from .VKTransformFeedback import VKTransformFeedback
from .VKVertexInput import VKVertexInput
from .VKViewState import VKViewState

class VKState(): # skipped bases: <class 'SwigPyObject'>
    """ The full current Vulkan pipeline state. """
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
    def colorBlend(self) -> VKColorBlendState:
        """
The color blending configuration.

:type: VKColorBlendState

"""
        pass

    @colorBlend.setter
    def colorBlend(self, value: VKColorBlendState):
        pass

    @property
    def compute(self) -> VKPipeline:
        """
The currently bound compute pipeline, if any.

:type: VKPipeline

"""
        pass

    @compute.setter
    def compute(self, value: VKPipeline):
        pass

    @property
    def computeShader(self) -> VKShader:
        """
The compute shader stage.

:type: VKShader

"""
        pass

    @computeShader.setter
    def computeShader(self, value: VKShader):
        pass

    @property
    def conditionalRendering(self) -> VKConditionalRendering:
        """
The current conditional rendering state.

:type: VKConditionalRendering

"""
        pass

    @conditionalRendering.setter
    def conditionalRendering(self, value: VKConditionalRendering):
        pass

    @property
    def currentPass(self) -> VKCurrentPass:
        """
The current renderpass, subpass and framebuffer.

:type: VKCurrentPass

"""
        pass

    @currentPass.setter
    def currentPass(self, value: VKCurrentPass):
        pass

    @property
    def depthStencil(self) -> VKDepthStencil:
        """
The depth-stencil state.

:type: VKDepthStencil

"""
        pass

    @depthStencil.setter
    def depthStencil(self, value: VKDepthStencil):
        pass

    @property
    def fragmentShader(self) -> VKShader:
        """
The fragment shader stage.

:type: VKShader

"""
        pass

    @fragmentShader.setter
    def fragmentShader(self, value: VKShader):
        pass

    @property
    def geometryShader(self) -> VKShader:
        """
The geometry shader stage.

:type: VKShader

"""
        pass

    @geometryShader.setter
    def geometryShader(self, value: VKShader):
        pass

    @property
    def graphics(self) -> VKPipeline:
        """
The currently bound graphics pipeline, if any.

:type: VKPipeline

"""
        pass

    @graphics.setter
    def graphics(self, value: VKPipeline):
        pass

    @property
    def images(self) -> List[VKImageData]:
        """
The resource states for the currently live resources.

:type: List[VKImageData]

"""
        pass

    @images.setter
    def images(self, value: List[VKImageData]):
        pass

    @property
    def inputAssembly(self) -> VKInputAssembly:
        """
The input assembly stage.

:type: VKInputAssembly

"""
        pass

    @inputAssembly.setter
    def inputAssembly(self, value: VKInputAssembly):
        pass

    @property
    def meshShader(self) -> VKShader:
        """
The mesh shader stage.

:type: VKShader

"""
        pass

    @meshShader.setter
    def meshShader(self, value: VKShader):
        pass

    @property
    def multisample(self) -> VKMultiSample:
        """
The multisampling configuration.

:type: VKMultiSample

"""
        pass

    @multisample.setter
    def multisample(self, value: VKMultiSample):
        pass

    @property
    def pushconsts(self) -> bytes:
        """
The raw push constant data.

:type: bytes

"""
        pass

    @pushconsts.setter
    def pushconsts(self, value: bytes):
        pass

    @property
    def rasterizer(self) -> VKRasterizer:
        """
The rasterization configuration.

:type: VKRasterizer

"""
        pass

    @rasterizer.setter
    def rasterizer(self, value: VKRasterizer):
        pass

    @property
    def shaderMessages(self) -> List[ShaderMessage]:
        """
The shader messages retrieved for this action.

:type: List[ShaderMessage]

"""
        pass

    @shaderMessages.setter
    def shaderMessages(self, value: List[ShaderMessage]):
        pass

    @property
    def taskShader(self) -> VKShader:
        """
The task shader stage.

:type: VKShader

"""
        pass

    @taskShader.setter
    def taskShader(self, value: VKShader):
        pass

    @property
    def tessControlShader(self) -> VKShader:
        """
The tessellation control shader stage.

:type: VKShader

"""
        pass

    @tessControlShader.setter
    def tessControlShader(self, value: VKShader):
        pass

    @property
    def tessellation(self) -> VKTessellation:
        """
The tessellation stage.

:type: VKTessellation

"""
        pass

    @tessellation.setter
    def tessellation(self, value: VKTessellation):
        pass

    @property
    def tessEvalShader(self) -> VKShader:
        """
The tessellation evaluation shader stage.

:type: VKShader

"""
        pass

    @tessEvalShader.setter
    def tessEvalShader(self, value: VKShader):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def transformFeedback(self) -> VKTransformFeedback:
        """
The transform feedback stage.

:type: VKTransformFeedback

"""
        pass

    @transformFeedback.setter
    def transformFeedback(self, value: VKTransformFeedback):
        pass

    @property
    def vertexInput(self) -> VKVertexInput:
        """
The vertex input stage.

:type: VKVertexInput

"""
        pass

    @vertexInput.setter
    def vertexInput(self, value: VKVertexInput):
        pass

    @property
    def vertexShader(self) -> VKShader:
        """
The vertex shader stage.

:type: VKShader

"""
        pass

    @vertexShader.setter
    def vertexShader(self, value: VKShader):
        pass

    @property
    def viewportScissor(self) -> VKViewState:
        """
The viewport setup.

:type: VKViewState

"""
        pass

    @viewportScissor.setter
    def viewportScissor(self, value: VKViewState):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551EBE90>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKState' objects>, 'pushconsts': <attribute 'pushconsts' of 'renderdoc.VKState' objects>, 'tessellation': <attribute 'tessellation' of 'renderdoc.VKState' objects>, 'transformFeedback': <attribute 'transformFeedback' of 'renderdoc.VKState' objects>, 'colorBlend': <attribute 'colorBlend' of 'renderdoc.VKState' objects>, 'graphics': <attribute 'graphics' of 'renderdoc.VKState' objects>, 'vertexInput': <attribute 'vertexInput' of 'renderdoc.VKState' objects>, 'currentPass': <attribute 'currentPass' of 'renderdoc.VKState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKState' objects>, 'compute': <attribute 'compute' of 'renderdoc.VKState' objects>, 'inputAssembly': <attribute 'inputAssembly' of 'renderdoc.VKState' objects>, 'conditionalRendering': <attribute 'conditionalRendering' of 'renderdoc.VKState' objects>, 'geometryShader': <attribute 'geometryShader' of 'renderdoc.VKState' objects>, 'computeShader': <attribute 'computeShader' of 'renderdoc.VKState' objects>, 'taskShader': <attribute 'taskShader' of 'renderdoc.VKState' objects>, 'viewportScissor': <attribute 'viewportScissor' of 'renderdoc.VKState' objects>, 'rasterizer': <attribute 'rasterizer' of 'renderdoc.VKState' objects>, 'vertexShader': <attribute 'vertexShader' of 'renderdoc.VKState' objects>, 'tessControlShader': <attribute 'tessControlShader' of 'renderdoc.VKState' objects>, 'tessEvalShader': <attribute 'tessEvalShader' of 'renderdoc.VKState' objects>, 'fragmentShader': <attribute 'fragmentShader' of 'renderdoc.VKState' objects>, 'meshShader': <attribute 'meshShader' of 'renderdoc.VKState' objects>, 'multisample': <attribute 'multisample' of 'renderdoc.VKState' objects>, 'images': <attribute 'images' of 'renderdoc.VKState' objects>, 'depthStencil': <attribute 'depthStencil' of 'renderdoc.VKState' objects>, 'shaderMessages': <attribute 'shaderMessages' of 'renderdoc.VKState' objects>, '__doc__': 'The full current Vulkan pipeline state.'})"


