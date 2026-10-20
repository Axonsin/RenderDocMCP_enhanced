from enum import IntFlag

class VulkanLayerFlags(IntFlag):
    # Original docstring
    """
    INTERNAL: A set of flags giving details of the current status of vulkan layer
    registration.
    
    .. data:: NoFlags
    
      There are no problems with the vulkan layer registration.
    
    .. data:: OtherInstallsRegistered
    
      Other conflicting installs of the same layer in other locations are registered.
    
    .. data:: ThisInstallRegistered
    
      This current install of the layer is registered.
    
    .. data:: NeedElevation
    
      Fixing any issues will require elevation to system administrator privileges.
    
    .. data:: UserRegisterable
    
      This layer can be registered as user-local, as well as system-wide. If :data:`NeedElevation` isn't
      also set then the entire process can be done un-elevated if user-local is desired.
    
      .. note::
    
        If the :data:`NeedElevation` flag is set then elevation is required to fix the layer
        registration, even if a user-local registration is desired.
    
        Most commonly this situation arises if there is no other registration, or the existing one is
        already user-local.
    
    .. data:: RegisterAll
    
      All listed locations for the current layer must be registered for correct functioning.
    
      If this flag is not set, then the listed locations are an 'or' list of alternatives.
    
    .. data:: UpdateAllowed
    
      If the current registrations can be updated or re-pointed to fix the issues.
    
    .. data:: Unfixable
    
      The current situation is not fixable automatically and requires user intervention/disambiguation.
    
    .. data:: Unsupported
    
      Vulkan is not supported by this build of RenderDoc and the layer cannot be registered.
    """
    
    
    # Enum values
    
    NoFlags = 0
    """
    There are no problems with the vulkan layer registration.
    """
    
    OtherInstallsRegistered = 1
    """
    Other conflicting installs of the same layer in other locations are registered.
    """
    
    ThisInstallRegistered = 2
    """
    This current install of the layer is registered.
    """
    
    NeedElevation = 4
    """
    Fixing any issues will require elevation to system administrator privileges.
    """
    
    UserRegisterable = 8
    """
    This layer can be registered as user-local, as well as system-wide. If :data:`NeedElevation` isn't
    also set then the entire process can be done un-elevated if user-local is desired.
    
    .. note::
    
      If the :data:`NeedElevation` flag is set then elevation is required to fix the layer
      registration, even if a user-local registration is desired.
    
      Most commonly this situation arises if there is no other registration, or the existing one is
      already user-local.
    """
    
    RegisterAll = 16
    """
    All listed locations for the current layer must be registered for correct functioning.
    
    If this flag is not set, then the listed locations are an 'or' list of alternatives.
    """
    
    UpdateAllowed = 32
    """
    If the current registrations can be updated or re-pointed to fix the issues.
    """
    
    Unfixable = 64
    """
    The current situation is not fixable automatically and requires user intervention/disambiguation.
    """
    
    Unsupported = 128
    """
    Vulkan is not supported by this build of RenderDoc and the layer cannot be registered.
    """
    

# Assign __doc__ for enum values for easier introspection

VulkanLayerFlags.NoFlags.__doc__ = """
There are no problems with the vulkan layer registration.
"""

VulkanLayerFlags.OtherInstallsRegistered.__doc__ = """
Other conflicting installs of the same layer in other locations are registered.
"""

VulkanLayerFlags.ThisInstallRegistered.__doc__ = """
This current install of the layer is registered.
"""

VulkanLayerFlags.NeedElevation.__doc__ = """
Fixing any issues will require elevation to system administrator privileges.
"""

VulkanLayerFlags.UserRegisterable.__doc__ = """
This layer can be registered as user-local, as well as system-wide. If :data:`NeedElevation` isn't
also set then the entire process can be done un-elevated if user-local is desired.

.. note::

  If the :data:`NeedElevation` flag is set then elevation is required to fix the layer
  registration, even if a user-local registration is desired.

  Most commonly this situation arises if there is no other registration, or the existing one is
  already user-local.
"""

VulkanLayerFlags.RegisterAll.__doc__ = """
All listed locations for the current layer must be registered for correct functioning.

If this flag is not set, then the listed locations are an 'or' list of alternatives.
"""

VulkanLayerFlags.UpdateAllowed.__doc__ = """
If the current registrations can be updated or re-pointed to fix the issues.
"""

VulkanLayerFlags.Unfixable.__doc__ = """
The current situation is not fixable automatically and requires user intervention/disambiguation.
"""

VulkanLayerFlags.Unsupported.__doc__ = """
Vulkan is not supported by this build of RenderDoc and the layer cannot be registered.
"""

