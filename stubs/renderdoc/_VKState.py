from ._ShaderMessage import ShaderMessage
from ._VKColorBlendState import VKColorBlendState
from ._VKConditionalRendering import VKConditionalRendering
from ._VKCurrentPass import VKCurrentPass
from ._VKDepthStencil import VKDepthStencil
from ._VKImageData import VKImageData
from ._VKInputAssembly import VKInputAssembly
from ._VKMultiSample import VKMultiSample
from ._VKPipeline import VKPipeline
from ._VKRasterizer import VKRasterizer
from ._VKShader import VKShader
from ._VKTessellation import VKTessellation
from ._VKTransformFeedback import VKTransformFeedback
from ._VKVertexInput import VKVertexInput
from ._VKViewState import VKViewState
from typing import List

class VKState():
    # Original docstring
    """
    The full current Vulkan pipeline state.
    """
    
    
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
    def viewportScissor(self) -> VKViewState:
        """
        The viewport setup.
        
        :type: VKViewState
        """
        pass
    
    @viewportScissor.setter
    def viewportScissor(self, value: VKViewState):
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
    def tessEvalShader(self) -> VKShader:
        """
        The tessellation evaluation shader stage.
        
        :type: VKShader
        """
        pass
    
    @tessEvalShader.setter
    def tessEvalShader(self, value: VKShader):
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
    def shaderMessages(self) -> List[ShaderMessage]:
        """
        The shader messages retrieved for this action.
        
        :type: List[ShaderMessage]
        """
        pass
    
    @shaderMessages.setter
    def shaderMessages(self, value: List[ShaderMessage]):
        pass
    
