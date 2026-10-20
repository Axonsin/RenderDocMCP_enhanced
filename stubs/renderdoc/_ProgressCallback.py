

# Synthetic function
def ProgressCallback(progress: float):
    """
    Not an actual member function - the signature for any ``ProgressCallback`` callbacks.
    
    Called by an on-going blocking process to update a progress bar or similar user feedback.
    
    The progress value will go from 0.0 to 1.0 as the process completes. Any other value will indicate
    that the process has completed
    
    :param float progress: The latest progress amount.
    """
    pass

