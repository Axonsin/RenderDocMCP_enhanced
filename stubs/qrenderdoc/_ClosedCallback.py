from ._CaptureConnection import CaptureConnection


# Synthetic function
def ClosedCallback(connection: 'CaptureConnection'):
    """
    Not a member function - the signature for any ``ClosedCallback`` callbacks.
    
    Called whenever a capture connection is closed.
    
    :param CaptureConnection connection: The connection window. Invalid to use after the callback
       has returned.
    """
    pass

