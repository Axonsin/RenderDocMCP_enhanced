from ._CaptureContext import CaptureContext


# Synthetic function
def FilterParseCallback(context: CaptureContext, filter: str, params: str) -> str:
    """
    Not a member function - the signature for any ``FilterParseCallback`` callbacks.
    
    Called once when the filter changes, to allow parsing any any data caching, as well as reporting
    of errors in the filter usage.
    
    :param CaptureContext context: The current capture context.
    :param str filter: The name of the filter function.
    :param str params: The parameters to the filter function.
    :return: An empty string if the parse succeeded, otherwise any error messages to be displayed to
      the user, such as syntax or other errors.
    :rtype: str
    """
    pass

