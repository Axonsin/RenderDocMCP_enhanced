from ._ResultCode import ResultCode

from typing import overload

class ResultDetails():
    # Original docstring
    """
    A general result from an operation with optional string information for failures.
    
    This struct can be compared directly to a :class:`ResultCode` for simple checks of status, and when
    converted to a string it includes the formatted result code and message as appropriate.
    
    .. note::
    
      The string information is only valid until :func:`ShutdownReplay` is called. After that point,
      accessing the string information is invalid and may crash. Care should be taken if
      :func:`ShutdownReplay` is called in response to an error, that the error code is read and saved.
    
      Copying the `ResultDetails` instance is *not* sufficient to preserve the string information. It
      should be copied to e.g. a `Tuple[ResultCode, str]` instead.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ResultDetails.
        """
        pass
    
    @overload
    def __init__(self, other: 'ResultDetails'):
        """
        Construct a new ResultDetails with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def OK(self) -> bool:
        """
        A simple helper function to check if this result is successful.
        
        :return: Whether or not this result is successful
        :rtype: bool
        """
        pass
    
    
    def Message(self) -> str:
        """
        For error codes, this will contain the stringified error code as well as any optional
        extra information that is available about the error.
        
        .. note::
        
          It's not necessary to also display the stringified version of :data:`code` as that is automatically
          included in the message.
        
        :return: A formatted message for failure codes, including the code itself.
        :rtype: str
        """
        pass
    
    @property
    def code(self) -> ResultCode:
        """
        The :class:`ResultCode` resulting from the operation, indicating success or failure.
        
        :type: ResultCode
        """
        pass
    
    @code.setter
    def code(self, value: ResultCode):
        pass
    
