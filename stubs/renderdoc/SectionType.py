# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class SectionType(__enum.IntEnum):
    """
    The types of several pre-defined and known sections. This allows consumers of the API
    to recognise and understand the contents of the section.
    
    Note that sections above the highest value here may be encountered if they were written in a new
    version of RenderDoc that addes a new section type. They should be considered equal to
    :data:`Unknown` by any processing.
    
    .. data:: Unknown
    
      An unknown section - any custom or non-predefined section will have this type.
    
    .. data:: FrameCapture
    
      This section contains the actual captured frame, in RenderDoc's internal chunked representation.
      The contents can be fetched as structured data with or without replaying the frame.
    
      The name for this section will be "renderdoc/internal/framecapture".
    
    .. data:: ResolveDatabase
    
      This section contains platform-specific data used to resolve callstacks.
    
      The name for this section will be "renderdoc/internal/resolvedb".
    
    .. data:: Bookmarks
    
      This section contains a JSON document with bookmarks added to the capture to highlight important
      events.
    
      The name for this section will be "renderdoc/ui/bookmarks".
    
    .. data:: Notes
    
      This section contains a JSON document with free-form information added for human consumption, e.g.
      details about how the capture was obtained with repro steps in the original program, or with
      driver and machine info.
    
      The name for this section will be "renderdoc/ui/notes".
    
    .. data:: ResourceRenames
    
      This section contains a JSON document with custom names applied to resources in the UI, over and
      above any friendly names specified in the capture itself.
    
      The name for this section will be "renderdoc/ui/resrenames".
    
    .. data:: AMDRGPProfile
    
      This section contains a .rgp profile from AMD's RGP tool, which can be extracted and loaded.
    
      The name for this section will be "amd/rgp/profile".
    
    .. data:: ExtendedThumbnail
    
      This section contains a thumbnail in format other than JPEG. For example, when it needs to be
      lossless.
    
      The name for this section will be "renderdoc/internal/exthumb".
    
    .. data:: EmbeddedLogfile
    
      This section contains the log file at the time of capture, for debugging.
    
      The name for this section will be "renderdoc/internal/logfile".
    
    .. data:: EditedShaders
    
      This section contains any edited shaders.
    
      The name for this section will be "renderdoc/ui/edits".
    
    .. data:: D3D12Core
    
      This section contains an internal copy of D3D12Core for replaying.
    
      The name for this section will be "renderdoc/internal/d3d12core".
    
    .. data:: D3D12SDKLayers
    
      This section contains an internal copy of D3D12SDKLayers for replaying.
    
      The name for this section will be "renderdoc/internal/d3d12sdklayers".
    
    .. data:: EmbeddedExternalFiles
    
      This section contains externally referenced files that have been embedded into the capture.
    
      The name for this section will be "renderdoc/internal/embeddedexternalfiles".
    """
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AMDRGPProfile = 6
    """
    This section contains a .rgp profile from AMD's RGP tool, which can be extracted and loaded.
    
      The name for this section will be "amd/rgp/profile".
    """

    Bookmarks = 3
    """
    This section contains a JSON document with bookmarks added to the capture to highlight important
      events.
    
      The name for this section will be "renderdoc/ui/bookmarks".
    """

    Count = 13
    D3D12Core = 10
    """
    This section contains an internal copy of D3D12Core for replaying.
    
      The name for this section will be "renderdoc/internal/d3d12core".
    """

    D3D12SDKLayers = 11
    """
    This section contains an internal copy of D3D12SDKLayers for replaying.
    
      The name for this section will be "renderdoc/internal/d3d12sdklayers".
    """

    EditedShaders = 9
    """
    This section contains any edited shaders.
    
      The name for this section will be "renderdoc/ui/edits".
    """

    EmbeddedExternalFiles = 12
    """
    This section contains externally referenced files that have been embedded into the capture.
    
      The name for this section will be "renderdoc/internal/embeddedexternalfiles".
    """

    EmbeddedLogfile = 8
    """
    This section contains the log file at the time of capture, for debugging.
    
      The name for this section will be "renderdoc/internal/logfile".
    """

    ExtendedThumbnail = 7
    """
    This section contains a thumbnail in format other than JPEG. For example, when it needs to be
      lossless.
    
      The name for this section will be "renderdoc/internal/exthumb".
    """

    First = 0
    FrameCapture = 1
    """
    This section contains the actual captured frame, in RenderDoc's internal chunked representation.
      The contents can be fetched as structured data with or without replaying the frame.
    
      The name for this section will be "renderdoc/internal/framecapture".
    """

    Notes = 4
    """
    This section contains a JSON document with free-form information added for human consumption, e.g.
      details about how the capture was obtained with repro steps in the original program, or with
      driver and machine info.
    
      The name for this section will be "renderdoc/ui/notes".
    """

    ResolveDatabase = 2
    """
    This section contains platform-specific data used to resolve callstacks.
    
      The name for this section will be "renderdoc/internal/resolvedb".
    """

    ResourceRenames = 5
    """
    This section contains a JSON document with custom names applied to resources in the UI, over and
      above any friendly names specified in the capture itself.
    
      The name for this section will be "renderdoc/ui/resrenames".
    """

    Unknown = 0
    """ An unknown section - any custom or non-predefined section will have this type. """



