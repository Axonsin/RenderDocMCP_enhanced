from ._WindowingData import WindowingData


# Synthetic function
def PreviewWindowCallback(active: bool) -> WindowingData:
    """
    Not an actual member function - the signature for any ``PreviewWindowCallback`` callbacks.
    
    Called when a preview window could optionally be opened to display some information. It will be
    called repeatedly with :paramref:`PreviewWindowCallback.active` set to ``True`` to allow any
    platform-specific message pumping.
    
    :param bool active: ``True`` if a preview window is active/opened, ``False`` if it has closed.
    :return: The windowing data for a preview window, or empty/default values if no window should be
      created.
    :rtype: WindowingData
    """
    pass

