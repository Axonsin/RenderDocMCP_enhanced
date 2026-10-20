from ._CaptureContext import CaptureContext
from ._ShaderViewer import ShaderViewer
from renderdoc import ResourceId


# Synthetic function
def RevertCallback(context: CaptureContext, viewer: 'ShaderViewer', id: ResourceId):
    """
    Not a member function - the signature for any ``RevertCallback`` callbacks.
    
    Called whenever a shader viewer that was open for editing is closed.
    
    :param CaptureContext context: The current capture context.
    :param ShaderViewer viewer: The open shader viewer.
    :param renderdoc.ResourceId id: The id of the shader being replaced.
    """
    pass

