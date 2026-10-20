from ._ResultDetails import ResultDetails

from typing import overload

class ExecuteResult():
    # Original docstring
    """
    The result of executing or injecting into a program.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ExecuteResult.
        """
        pass
    
    @overload
    def __init__(self, other: 'ExecuteResult'):
        """
        Construct a new ExecuteResult with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def ident(self) -> int:
        """
        The ident where the new application is listening for target control, or 0 if something
        went wrong.
        
        :type: int
        """
        pass
    
    @ident.setter
    def ident(self, value: int):
        pass
    
    @property
    def result(self) -> ResultDetails:
        """
        The :class:`ResultDetails` resulting from the operation, indicating success or failure.
        
        :type: ResultDetails
        """
        pass
    
    @result.setter
    def result(self, value: ResultDetails):
        pass
    
