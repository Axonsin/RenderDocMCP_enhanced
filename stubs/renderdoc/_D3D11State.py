from ._D3D11InputAssembly import D3D11InputAssembly
from ._D3D11OutputMerger import D3D11OutputMerger
from ._D3D11Predication import D3D11Predication
from ._D3D11Rasterizer import D3D11Rasterizer
from ._D3D11Shader import D3D11Shader
from ._D3D11StreamOut import D3D11StreamOut
from ._ResourceId import ResourceId

class D3D11State():
    # Original docstring
    """
    The full current D3D11 pipeline state.
    """
    
    
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
    def vertexShader(self) -> D3D11Shader:
        """
        The vertex shader stage.
        
        :type: D3D11Shader
        """
        pass
    
    @vertexShader.setter
    def vertexShader(self, value: D3D11Shader):
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
    def pixelShader(self) -> D3D11Shader:
        """
        The pixel shader stage.
        
        :type: D3D11Shader
        """
        pass
    
    @pixelShader.setter
    def pixelShader(self, value: D3D11Shader):
        pass
    
