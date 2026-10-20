from ._GLDepthState import GLDepthState
from ._GLFeedback import GLFeedback
from ._GLFixedVertexProcessing import GLFixedVertexProcessing
from ._GLFrameBuffer import GLFrameBuffer
from ._GLHints import GLHints
from ._GLRasterizer import GLRasterizer
from ._GLShader import GLShader
from ._GLStencilState import GLStencilState
from ._GLTextureCompleteness import GLTextureCompleteness
from ._GLVertexInput import GLVertexInput
from ._ResourceId import ResourceId

class GLState():
    # Original docstring
    """
    The full current OpenGL pipeline state.
    """
    
    
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
    def textureCompleteness(self) -> GLTextureCompleteness:
        """
        Texture completeness issues of descriptors in the descriptor store.
        
        :type: GLTextureCompleteness
        """
        pass
    
    @textureCompleteness.setter
    def textureCompleteness(self, value: GLTextureCompleteness):
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
    def vertexShader(self) -> GLShader:
        """
        The vertex shader stage.
        
        :type: GLShader
        """
        pass
    
    @vertexShader.setter
    def vertexShader(self, value: GLShader):
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
    def fragmentShader(self) -> GLShader:
        """
        The fragment shader stage.
        
        :type: GLShader
        """
        pass
    
    @fragmentShader.setter
    def fragmentShader(self, value: GLShader):
        pass
    
