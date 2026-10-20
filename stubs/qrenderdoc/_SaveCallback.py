from ._CaptureContext import CaptureContext
from ._ShaderViewer import ShaderViewer
from renderdoc import ResourceId, ShaderCompileFlags, ShaderEncoding, ShaderStage


# Synthetic function
def SaveCallback(context: CaptureContext, viewer: 'ShaderViewer', id: ResourceId, stage: ShaderStage, encoding: ShaderEncoding, flags: ShaderCompileFlags, entryFunc: str, source: bytes):
    """
    Not a member function - the signature for any ``SaveCallback`` callbacks.
    
    Called whenever a shader viewer that was open for editing triggers a save/update.
    
    :param CaptureContext context: The current capture context.
    :param ShaderViewer viewer: The open shader viewer.
    :param renderdoc.ResourceId id: The id of the shader being replaced.
    :param renderdoc.ShaderStage stage: The shader stage of the shader being replaced.
    :param renderdoc.ShaderEncoding encoding: The encoding of the files being passed.
    :param renderdoc.ShaderCompileFlags flags: The flags to use during compilation.
    :param str entryFunc: The name of the entry point.
    :param bytes source: The byte buffer containing the source - may just be text depending on the
      encoding.
    """
    pass

