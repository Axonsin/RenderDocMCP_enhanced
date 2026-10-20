from ._CaptureContext import CaptureContext
from typing import List


# Synthetic function
def AutoCompleteCallback(context: CaptureContext, filter: str, params: str) -> List[str]:
    """
    Not a member function - the signature for any ``AutoCompleteCallback`` callbacks.
    
    Called when autocompletion is triggered inside a filter. The params passed are any previous
    text inside the filter's parameter list up to where the cursor is. The callback should return a
    list of identifiers used for auto-completion.
    
    The list does not have to be pre-filtered for matches to the :paramref:`AutoCompleteCallback.params`,
    that is provided to allow different autocompletion at different stages (e.g. if there are no
    parameters, you can autocomplete a property, if a property is already present you can
    autocomplete valid values for it)
    
    :param CaptureContext context: The current capture context.
    :param str filter: The name of the filter function.
    :param str params: The previous parameter text to the filter function.
    :return: A list of strings giving identifiers to autocomplete, or an empty list of there are no
      such identifiers to prompt.
    :rtype: List[str]
    """
    pass

