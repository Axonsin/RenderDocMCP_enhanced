from ._Offset import Offset
from ._ResourceId import ResourceId
from typing import List, Tuple

from typing import overload

class VKRenderPass():
    # Original docstring
    """
    Describes the setup of a renderpass and subpasses.
    
    .. data:: AttachmentUnused
    
      Alias for ``VK_ATTACHMENT_UNUSED``, for use by the UI to know when a value in ``colorAttachmentLocations``
      or ``colorAttachmentInputIndices`` is mapped to ``VK_ATTACHMENT_UNUSED``.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised VKRenderPass.
        """
        pass
    
    @overload
    def __init__(self, other: 'VKRenderPass'):
        """
        Construct a new VKRenderPass with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    AttachmentUnused = 4294967295
    """
    Alias for ``VK_ATTACHMENT_UNUSED``, for use by the UI to know when a value in ``colorAttachmentLocations``
    or ``colorAttachmentInputIndices`` is mapped to ``VK_ATTACHMENT_UNUSED``.
    """
    
    @property
    def inputAttachments(self) -> List[int]:
        """
        The input attachments for the current subpass, as indices into the framebuffer
        attachments.
        
        :type: List[int]
        """
        pass
    
    @inputAttachments.setter
    def inputAttachments(self, value: List[int]):
        pass
    
    @property
    def colorAttachments(self) -> List[int]:
        """
        The color attachments for the current subpass, as indices into the framebuffer
        attachments.
        
        :type: List[int]
        """
        pass
    
    @colorAttachments.setter
    def colorAttachments(self, value: List[int]):
        pass
    
    @property
    def resolveAttachments(self) -> List[int]:
        """
        The resolve attachments for the current subpass, as indices into the framebuffer
        attachments.
        
        :type: List[int]
        """
        pass
    
    @resolveAttachments.setter
    def resolveAttachments(self, value: List[int]):
        pass
    
    @property
    def multiviews(self) -> List[int]:
        """
        If multiview is enabled, contains a list of view indices to be broadcast to during
        rendering.
        
        If the list is empty, multiview is disabled and rendering is as normal.
        
        :type: List[int]
        """
        pass
    
    @multiviews.setter
    def multiviews(self, value: List[int]):
        pass
    
    @property
    def subpass(self) -> int:
        """
        The index of the current active subpass.
        
        :type: int
        """
        pass
    
    @subpass.setter
    def subpass(self, value: int):
        pass
    
    @property
    def resourceId(self) -> ResourceId:
        """
        The :class:`ResourceId` of the render pass.
        
        :type: ResourceId
        """
        pass
    
    @resourceId.setter
    def resourceId(self, value: ResourceId):
        pass
    
    @property
    def shadingRateTexelSize(self) -> Tuple[int, int]:
        """
        The size of the framebuffer region represented by each texel in
        :data:`shadingRateAttachment`.
        
        For example if this is (2,2) then every texel in the attachment gives the shading rate of a 2x2
        block in the framebuffer so the shading rate attachment is half the size of the other attachments in
        each dimension.
        
        If no attachment is set in :data:`shadingRateAttachment` this will be (1,1).
        
        :type: Tuple[int,int]
        """
        pass
    
    @shadingRateTexelSize.setter
    def shadingRateTexelSize(self, value: Tuple[int, int]):
        pass
    
    @property
    def fragmentDensityOffsets(self) -> List[Offset]:
        """
        If ``VK_QCOM_fragment_density_map_offset`` is enabled, contains a list of offsets applied
        to the fragment density map during rendering.
        
        If the list is empty, ``fdm_offset`` is disabled and rendering is as normal.
        
        :type: List[Offset]
        """
        pass
    
    @fragmentDensityOffsets.setter
    def fragmentDensityOffsets(self, value: List[Offset]):
        pass
    
    @property
    def colorAttachmentInputIndices(self) -> List[int]:
        """
        The color index->input index mapping set up by dynamic rendering local read.
        
        :type: List[int]
        """
        pass
    
    @colorAttachmentInputIndices.setter
    def colorAttachmentInputIndices(self, value: List[int]):
        pass
    
    @property
    def depthstencilAttachment(self) -> int:
        """
        An index into the framebuffer attachments for the depth-stencil attachment.
        
        If there is no depth-stencil attachment, this index is ``-1``.
        
        :type: int
        """
        pass
    
    @depthstencilAttachment.setter
    def depthstencilAttachment(self, value: int):
        pass
    
    @property
    def depthstencilResolveAttachment(self) -> int:
        """
        An index into the framebuffer attachments for the depth-stencil resolve attachment.
        
        If there is no depth-stencil resolve attachment, this index is ``-1``.
        
        :type: int
        """
        pass
    
    @depthstencilResolveAttachment.setter
    def depthstencilResolveAttachment(self, value: int):
        pass
    
    @property
    def fragmentDensityAttachment(self) -> int:
        """
        An index into the framebuffer attachments for the fragment density attachment.
        
        If there is no fragment density attachment, this index is ``-1``.
        
        .. note::
          Only one at most of :data:`fragmentDensityAttachment` and :data:`shadingRateAttachment` will be
          set.
        
        :type: int
        """
        pass
    
    @fragmentDensityAttachment.setter
    def fragmentDensityAttachment(self, value: int):
        pass
    
    @property
    def shadingRateAttachment(self) -> int:
        """
        An index into the framebuffer attachments for the fragment shading rate attachment.
        
        If there is no fragment shading rate attachment, this index is ``-1``.
        
        .. note::
          Only one at most of :data:`fragmentDensityAttachment` and :data:`shadingRateAttachment` will be
          set.
        
        :type: int
        """
        pass
    
    @shadingRateAttachment.setter
    def shadingRateAttachment(self, value: int):
        pass
    
    @property
    def tileOnlyMSAASampleCount(self) -> int:
        """
        If ``VK_EXT_multisampled_render_to_single_sampled`` is enabled, contains the number of
        samples used to render this subpass.
        
        If the subpass is not internally multisampled, ``tileOnlyMSAASampleCount`` is set to 0.
        
        :type: int
        """
        pass
    
    @tileOnlyMSAASampleCount.setter
    def tileOnlyMSAASampleCount(self, value: int):
        pass
    
    @property
    def dynamic(self) -> bool:
        """
        Whether or not dynamic rendering is in use (no render pass or framebuffer objects).
        
        :type: bool
        """
        pass
    
    @dynamic.setter
    def dynamic(self, value: bool):
        pass
    
    @property
    def suspended(self) -> bool:
        """
        Whether or not dynamic rendering is currently suspended.
        
        :type: bool
        """
        pass
    
    @suspended.setter
    def suspended(self, value: bool):
        pass
    
    @property
    def depthInputAttachmentIndex(self) -> int:
        """
        Depth input attachment index if explicit (dynamic rendering).
        
        :type: int
        """
        pass
    
    @depthInputAttachmentIndex.setter
    def depthInputAttachmentIndex(self, value: int):
        pass
    
    @property
    def stencilInputAttachmentIndex(self) -> int:
        """
        Stencil input attachment index if explicit (dynamic rendering).
        
        :type: int
        """
        pass
    
    @stencilInputAttachmentIndex.setter
    def stencilInputAttachmentIndex(self, value: int):
        pass
    
    @property
    def colorAttachmentLocations(self) -> List[int]:
        """
        The color index->location mapping set up by dynamic rendering local read.
        
        :type: List[int]
        """
        pass
    
    @colorAttachmentLocations.setter
    def colorAttachmentLocations(self, value: List[int]):
        pass
    
    @property
    def isDepthInputAttachmentIndexImplicit(self) -> bool:
        """
        Whether or not depth input attachment index is implicit (dynamic rendering).
        
        :type: bool
        """
        pass
    
    @isDepthInputAttachmentIndexImplicit.setter
    def isDepthInputAttachmentIndexImplicit(self, value: bool):
        pass
    
    @property
    def isStencilInputAttachmentIndexImplicit(self) -> bool:
        """
        Whether or not stencil  input attachment index is implicit (dynamic rendering).
        
        :type: bool
        """
        pass
    
    @isStencilInputAttachmentIndexImplicit.setter
    def isStencilInputAttachmentIndexImplicit(self, value: bool):
        pass
    
    @property
    def feedbackLoop(self) -> bool:
        """
        Whether or not there is a potential feedback loop.
        
        :type: bool
        """
        pass
    
    @feedbackLoop.setter
    def feedbackLoop(self, value: bool):
        pass
    
