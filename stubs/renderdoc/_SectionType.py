from enum import IntEnum

class SectionType(IntEnum):
    # Original docstring
    """
    The types of several pre-defined and known sections. This allows consumers of the API
    to recognise and understand the contents of the section.
    
    Note that sections above the highest value here may be encountered if they were written in a new
    version of RenderDoc that added a new section type. They should be considered equal to
    :data:`Unknown` by any processing.
    
    .. data:: Unknown
    
      An unknown section - any custom or non-predefined section will have this type.
    
    .. data:: FrameCapture
    
      This section contains the actual captured frame, in RenderDoc's internal chunked representation.
      The contents can be fetched as structured data with or without replaying the frame.
    
      The name for this section will be ``renderdoc/internal/framecapture``.
    
    .. data:: ResolveDatabase
    
      This section contains platform-specific data used to resolve callstacks.
    
      The name for this section will be ``renderdoc/internal/resolvedb``.
    
    .. data:: Bookmarks
    
      This section contains a JSON document with bookmarks added to the capture to highlight important
      events.
    
      The name for this section will be ``renderdoc/ui/bookmarks``.
    
    .. data:: Notes
    
      This section contains a JSON document with free-form information added for human consumption, e.g.
      details about how the capture was obtained with repro steps in the original program, or with
      driver and machine info.
    
      The name for this section will be ``renderdoc/ui/notes``.
    
    .. data:: ResourceRenames
    
      This section contains a JSON document with custom names applied to resources in the UI, over and
      above any friendly names specified in the capture itself.
    
      The name for this section will be ``renderdoc/ui/resrenames``.
    
    .. data:: AMDRGPProfile
    
      This section contains a .rgp profile from AMD's RGP tool, which can be extracted and loaded.
    
      The name for this section will be ``amd/rgp/profile``.
    
    .. data:: ExtendedThumbnail
    
      This section contains a thumbnail in format other than JPEG. For example, when it needs to be
      lossless.
    
      The name for this section will be ``renderdoc/internal/exthumb``.
    
    .. data:: EmbeddedLogfile
    
      This section contains the log file at the time of capture, for debugging.
    
      The name for this section will be ``renderdoc/internal/logfile``.
    
    .. data:: EditedShaders
    
      This section contains any edited shaders.
    
      The name for this section will be ``renderdoc/ui/edits``.
    
    .. data:: D3D12Core
    
      This section contains an internal copy of D3D12Core for replaying.
    
      The name for this section will be ``renderdoc/internal/d3d12core``.
    
    .. data:: D3D12SDKLayers
    
      This section contains an internal copy of D3D12SDKLayers for replaying.
    
      The name for this section will be ``renderdoc/internal/d3d12sdklayers``.
    
    .. data:: EmbeddedExternalFiles
    
      This section contains externally referenced files that have been embedded into the capture.
    
      The name for this section will be ``renderdoc/internal/embeddedexternalfiles``.
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    An unknown section - any custom or non-predefined section will have this type.
    """
    
    FrameCapture = 1
    """
    This section contains the actual captured frame, in RenderDoc's internal chunked representation.
    The contents can be fetched as structured data with or without replaying the frame.
    
    The name for this section will be ``renderdoc/internal/framecapture``.
    """
    
    ResolveDatabase = 2
    """
    This section contains platform-specific data used to resolve callstacks.
    
    The name for this section will be ``renderdoc/internal/resolvedb``.
    """
    
    Bookmarks = 3
    """
    This section contains a JSON document with bookmarks added to the capture to highlight important
    events.
    
    The name for this section will be ``renderdoc/ui/bookmarks``.
    """
    
    Notes = 4
    """
    This section contains a JSON document with free-form information added for human consumption, e.g.
    details about how the capture was obtained with repro steps in the original program, or with
    driver and machine info.
    
    The name for this section will be ``renderdoc/ui/notes``.
    """
    
    ResourceRenames = 5
    """
    This section contains a JSON document with custom names applied to resources in the UI, over and
    above any friendly names specified in the capture itself.
    
    The name for this section will be ``renderdoc/ui/resrenames``.
    """
    
    AMDRGPProfile = 6
    """
    This section contains a .rgp profile from AMD's RGP tool, which can be extracted and loaded.
    
    The name for this section will be ``amd/rgp/profile``.
    """
    
    ExtendedThumbnail = 7
    """
    This section contains a thumbnail in format other than JPEG. For example, when it needs to be
    lossless.
    
    The name for this section will be ``renderdoc/internal/exthumb``.
    """
    
    EmbeddedLogfile = 8
    """
    This section contains the log file at the time of capture, for debugging.
    
    The name for this section will be ``renderdoc/internal/logfile``.
    """
    
    EditedShaders = 9
    """
    This section contains any edited shaders.
    
    The name for this section will be ``renderdoc/ui/edits``.
    """
    
    D3D12Core = 10
    """
    This section contains an internal copy of D3D12Core for replaying.
    
    The name for this section will be ``renderdoc/internal/d3d12core``.
    """
    
    D3D12SDKLayers = 11
    """
    This section contains an internal copy of D3D12SDKLayers for replaying.
    
    The name for this section will be ``renderdoc/internal/d3d12sdklayers``.
    """
    
    EmbeddedExternalFiles = 12
    """
    This section contains externally referenced files that have been embedded into the capture.
    
    The name for this section will be ``renderdoc/internal/embeddedexternalfiles``.
    """
    
    Count = 13
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

SectionType.Unknown.__doc__ = """
An unknown section - any custom or non-predefined section will have this type.
"""

SectionType.FrameCapture.__doc__ = """
This section contains the actual captured frame, in RenderDoc's internal chunked representation.
The contents can be fetched as structured data with or without replaying the frame.

The name for this section will be ``renderdoc/internal/framecapture``.
"""

SectionType.ResolveDatabase.__doc__ = """
This section contains platform-specific data used to resolve callstacks.

The name for this section will be ``renderdoc/internal/resolvedb``.
"""

SectionType.Bookmarks.__doc__ = """
This section contains a JSON document with bookmarks added to the capture to highlight important
events.

The name for this section will be ``renderdoc/ui/bookmarks``.
"""

SectionType.Notes.__doc__ = """
This section contains a JSON document with free-form information added for human consumption, e.g.
details about how the capture was obtained with repro steps in the original program, or with
driver and machine info.

The name for this section will be ``renderdoc/ui/notes``.
"""

SectionType.ResourceRenames.__doc__ = """
This section contains a JSON document with custom names applied to resources in the UI, over and
above any friendly names specified in the capture itself.

The name for this section will be ``renderdoc/ui/resrenames``.
"""

SectionType.AMDRGPProfile.__doc__ = """
This section contains a .rgp profile from AMD's RGP tool, which can be extracted and loaded.

The name for this section will be ``amd/rgp/profile``.
"""

SectionType.ExtendedThumbnail.__doc__ = """
This section contains a thumbnail in format other than JPEG. For example, when it needs to be
lossless.

The name for this section will be ``renderdoc/internal/exthumb``.
"""

SectionType.EmbeddedLogfile.__doc__ = """
This section contains the log file at the time of capture, for debugging.

The name for this section will be ``renderdoc/internal/logfile``.
"""

SectionType.EditedShaders.__doc__ = """
This section contains any edited shaders.

The name for this section will be ``renderdoc/ui/edits``.
"""

SectionType.D3D12Core.__doc__ = """
This section contains an internal copy of D3D12Core for replaying.

The name for this section will be ``renderdoc/internal/d3d12core``.
"""

SectionType.D3D12SDKLayers.__doc__ = """
This section contains an internal copy of D3D12SDKLayers for replaying.

The name for this section will be ``renderdoc/internal/d3d12sdklayers``.
"""

SectionType.EmbeddedExternalFiles.__doc__ = """
This section contains externally referenced files that have been embedded into the capture.

The name for this section will be ``renderdoc/internal/embeddedexternalfiles``.
"""

SectionType.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

SectionType.First.__doc__ = """
The first enum value, for ease of iteration.
"""

