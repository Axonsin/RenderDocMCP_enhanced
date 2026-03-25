# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .GLShader import GLShader
from .GLDepthState import GLDepthState
from .ResourceId import ResourceId
from .GLFrameBuffer import GLFrameBuffer
from .GLHints import GLHints
from .GLRasterizer import GLRasterizer
from .GLStencilState import GLStencilState
from .GLTextureCompleteness import GLTextureCompleteness
from .GLFeedback import GLFeedback
from .GLVertexInput import GLVertexInput
from .GLFixedVertexProcessing import GLFixedVertexProcessing

class GLState(): # skipped bases: <class 'SwigPyObject'>
    """ The full current OpenGL pipeline state. """
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
    def computeShader(self) -> GLShader:
        """
The compute shader stage.

:type: GLShader

"""
        pass

    @computeShader.setter
    def computeShader(self, value: GLShader):
        pass

    @property
    def depthState(self) -> GLDepthState:
        """
The depth state.

:type: GLDepthState

"""
        pass

    @depthState.setter
    def depthState(self, value: GLDepthState):
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
    def fragmentShader(self) -> GLShader:
        """
The fragment shader stage.

:type: GLShader

"""
        pass

    @fragmentShader.setter
    def fragmentShader(self, value: GLShader):
        pass

    @property
    def framebuffer(self) -> GLFrameBuffer:
        """
The bound framebuffer.

:type: GLFrameBuffer

"""
        pass

    @framebuffer.setter
    def framebuffer(self, value: GLFrameBuffer):
        pass

    @property
    def geometryShader(self) -> GLShader:
        """
The geometry shader stage.

:type: GLShader

"""
        pass

    @geometryShader.setter
    def geometryShader(self, value: GLShader):
        pass

    @property
    def hints(self) -> GLHints:
        """
The hint state.

:type: GLHints

"""
        pass

    @hints.setter
    def hints(self, value: GLHints):
        pass

    @property
    def pipelineResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the program pipeline (if active).

:type: ResourceId

"""
        pass

    @pipelineResourceId.setter
    def pipelineResourceId(self, value: ResourceId):
        pass

    @property
    def rasterizer(self) -> GLRasterizer:
        """
The rasterization configuration.

:type: GLRasterizer

"""
        pass

    @rasterizer.setter
    def rasterizer(self, value: GLRasterizer):
        pass

    @property
    def stencilState(self) -> GLStencilState:
        """
The stencil state.

:type: GLStencilState

"""
        pass

    @stencilState.setter
    def stencilState(self, value: GLStencilState):
        pass

    @property
    def tessControlShader(self) -> GLShader:
        """
The tessellation control shader stage.

:type: GLShader

"""
        pass

    @tessControlShader.setter
    def tessControlShader(self, value: GLShader):
        pass

    @property
    def tessEvalShader(self) -> GLShader:
        """
The tessellation evaluation shader stage.

:type: GLShader

"""
        pass

    @tessEvalShader.setter
    def tessEvalShader(self, value: GLShader):
        pass

    @property
    def textureCompleteness(self) -> GLTextureCompleteness:
        """
Texture completeness issues of descriptors in the descriptor store.

:type: GLTextureCompleteness

"""
        pass

    @textureCompleteness.setter
    def textureCompleteness(self, value: GLTextureCompleteness):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def transformFeedback(self) -> GLFeedback:
        """
The transform feedback stage.

:type: GLFeedback

"""
        pass

    @transformFeedback.setter
    def transformFeedback(self, value: GLFeedback):
        pass

    @property
    def vertexInput(self) -> GLVertexInput:
        """
The vertex input stage.

:type: GLVertexInput

"""
        pass

    @vertexInput.setter
    def vertexInput(self, value: GLVertexInput):
        pass

    @property
    def vertexProcessing(self) -> GLFixedVertexProcessing:
        """
The fixed-function vertex processing stage.

:type: GLFixedVertexProcessing

"""
        pass

    @vertexProcessing.setter
    def vertexProcessing(self, value: GLFixedVertexProcessing):
        pass

    @property
    def vertexShader(self) -> GLShader:
        """
The vertex shader stage.

:type: GLShader

"""
        pass

    @vertexShader.setter
    def vertexShader(self, value: GLShader):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD55200FC0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLState' objects>, 'transformFeedback': <attribute 'transformFeedback' of 'renderdoc.GLState' objects>, 'stencilState': <attribute 'stencilState' of 'renderdoc.GLState' objects>, 'vertexInput': <attribute 'vertexInput' of 'renderdoc.GLState' objects>, 'framebuffer': <attribute 'framebuffer' of 'renderdoc.GLState' objects>, 'pipelineResourceId': <attribute 'pipelineResourceId' of 'renderdoc.GLState' objects>, 'descriptorStore': <attribute 'descriptorStore' of 'renderdoc.GLState' objects>, 'descriptorCount': <attribute 'descriptorCount' of 'renderdoc.GLState' objects>, 'depthState': <attribute 'depthState' of 'renderdoc.GLState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLState' objects>, 'hints': <attribute 'hints' of 'renderdoc.GLState' objects>, 'vertexProcessing': <attribute 'vertexProcessing' of 'renderdoc.GLState' objects>, 'geometryShader': <attribute 'geometryShader' of 'renderdoc.GLState' objects>, 'computeShader': <attribute 'computeShader' of 'renderdoc.GLState' objects>, 'descriptorByteSize': <attribute 'descriptorByteSize' of 'renderdoc.GLState' objects>, 'textureCompleteness': <attribute 'textureCompleteness' of 'renderdoc.GLState' objects>, 'rasterizer': <attribute 'rasterizer' of 'renderdoc.GLState' objects>, 'vertexShader': <attribute 'vertexShader' of 'renderdoc.GLState' objects>, 'tessControlShader': <attribute 'tessControlShader' of 'renderdoc.GLState' objects>, 'tessEvalShader': <attribute 'tessEvalShader' of 'renderdoc.GLState' objects>, 'fragmentShader': <attribute 'fragmentShader' of 'renderdoc.GLState' objects>, '__doc__': 'The full current OpenGL pipeline state.'})"


