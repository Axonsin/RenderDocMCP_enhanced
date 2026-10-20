from ._D3D12InputAssembly import D3D12InputAssembly
from ._D3D12OM import D3D12OM
from ._D3D12Predication import D3D12Predication
from ._D3D12Rasterizer import D3D12Rasterizer
from ._D3D12ResourceData import D3D12ResourceData
from ._D3D12RootSignature import D3D12RootSignature
from ._D3D12Shader import D3D12Shader
from ._D3D12StreamOut import D3D12StreamOut
from ._ResourceId import ResourceId
from typing import List

class D3D12State():
    # Original docstring
    """
    The full current D3D12 pipeline state.
    """
    
    
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
    def vertexShader(self) -> D3D12Shader:
        """
        The vertex shader stage.
        
        :type: D3D12Shader
        """
        pass
    
    @vertexShader.setter
    def vertexShader(self, value: D3D12Shader):
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
    def meshShader(self) -> D3D12Shader:
        """
        The mesh shader stage.
        
        :type: D3D12Shader
        """
        pass
    
    @meshShader.setter
    def meshShader(self, value: D3D12Shader):
        pass
    
