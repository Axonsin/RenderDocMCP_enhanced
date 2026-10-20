from ._InstructionSourceInfo import InstructionSourceInfo
from ._ShaderDebugger import ShaderDebugger
from ._ShaderStage import ShaderStage
from ._ShaderVariable import ShaderVariable
from ._SourceVariableMapping import SourceVariableMapping
from typing import List

class ShaderDebugTrace():
    # Original docstring
    """
    This stores the whole state of a shader's execution from start to finish, with each
    individual debugging step along the way, as well as the immutable global constant values that do not
    change with shader execution.
    """
    
    
    @property
    def constantBlocks(self) -> List[ShaderVariable]:
        """
        Constant buffer backed variables for this shader.
        
        Each entry in this list corresponds to a constant block with the same index in the
        :data:`ShaderReflection.constantBlocks` list, which can be used to look up the metadata.
        
        Depending on the underlying shader representation, the constant block may retain any structure or
        it may have been vectorised and flattened.
        
        :type: List[ShaderVariable]
        """
        pass
    
    @constantBlocks.setter
    def constantBlocks(self, value: List[ShaderVariable]):
        pass
    
    @property
    def samplers(self) -> List[ShaderVariable]:
        """
        The sampler variables for this shader.
        
        The 'value' of the variable is always a single unsigned integer, which is the bindpoint - an index
        into the :data:`ShaderReflection.samplers` list, which can be used to look up the
        other metadata as well as find the binding from the pipeline state.
        
        :type: List[ShaderVariable]
        """
        pass
    
    @samplers.setter
    def samplers(self, value: List[ShaderVariable]):
        pass
    
    @property
    def instInfo(self) -> List[InstructionSourceInfo]:
        """
        An array of the same size as the number of instructions in the shader, with
        per-instruction information such as source line mapping, and source variables.
        
        .. warning::
        
          This array is *not* indexed by instruction. Since it is common for adjacent instructions to have
          effectively identical source information, this array only stores unique information ordered by
          instruction. On some internal representations this may be one entry per instruction, and on others
          it may be sparse and require a binary lookup to locate the corresponding information for an
          instruction. If no direct match is found, the lower bound match is valid (i.e. the data for
          instruction A before the data for instruction B is valid for all instructions in range ``[A, B)``.
        
        :type: List[InstructionSourceInfo]
        """
        pass
    
    @instInfo.setter
    def instInfo(self, value: List[InstructionSourceInfo]):
        pass
    
    @property
    def stage(self) -> ShaderStage:
        """
        The shader stage being debugged in this trace
        
        :type: ShaderStage
        """
        pass
    
    @stage.setter
    def stage(self, value: ShaderStage):
        pass
    
    @property
    def inputs(self) -> List[ShaderVariable]:
        """
        The input variables for this shader.
        
        :type: List[ShaderVariable]
        """
        pass
    
    @inputs.setter
    def inputs(self, value: List[ShaderVariable]):
        pass
    
    @property
    def readOnlyResources(self) -> List[ShaderVariable]:
        """
        The read-only resource variables for this shader.
        
        The 'value' of the variable is always a single unsigned integer, which is the bindpoint - an index
        into the :data:`ShaderReflection.readOnlyResources` list, which can be used to look up the
        other metadata as well as find the binding from the pipeline state.
        
        :type: List[ShaderVariable]
        """
        pass
    
    @readOnlyResources.setter
    def readOnlyResources(self, value: List[ShaderVariable]):
        pass
    
    @property
    def readWriteResources(self) -> List[ShaderVariable]:
        """
        The read-write resource variables for this shader.
        
        The 'value' of the variable is always a single unsigned integer, which is the bindpoint - an index
        into the :data:`ShaderReflection.readWriteResources` list, which can be used to look up the
        other metadata as well as find the binding from the pipeline state.
        
        :type: List[ShaderVariable]
        """
        pass
    
    @readWriteResources.setter
    def readWriteResources(self, value: List[ShaderVariable]):
        pass
    
    @property
    def sourceVars(self) -> List[SourceVariableMapping]:
        """
        An optional mapping from high-level source variables to which debug variables and
        includes extra type information.
        
        This list contains source variable mapping that is valid for the lifetime of a debug trace. It may
        be empty if there is no source variable mapping that extends to the life of the debug trace.
        
        :type: List[SourceVariableMapping]
        """
        pass
    
    @sourceVars.setter
    def sourceVars(self, value: List[SourceVariableMapping]):
        pass
    
    @property
    def debugger(self) -> ShaderDebugger:
        """
        An opaque handle identifying by the underlying debugger, which is used to simulate the
        shader and generate new debug states.
        
        If this is ``None`` then the trace is invalid.
        
        :type: ShaderDebugger
        """
        pass
    
    @debugger.setter
    def debugger(self, value: ShaderDebugger):
        pass
    
