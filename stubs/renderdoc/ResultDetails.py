# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResultCode import ResultCode

class ResultDetails(): # skipped bases: <class 'SwigPyObject'>
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
    def Message(self) -> str: # real signature unknown; restored from __doc__
        """
        Message()
        
        For error codes, this will contain the stringified error code as well as any optional
        extra information that is available about the error.
        
        .. note::
        
          It's not necessary to also display the stringified version of :data:`code` as that is automatically
          included in the message.
        
        :return: A formatted message for failure codes, including the code itself.
        :rtype: str
        """
        pass

    def OK(self) -> bool: # real signature unknown; restored from __doc__
        """
        OK()
        
        A simple helper function to check if this result is successful.
        
        :return: Whether or not this result is successful
        :rtype: bool
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ __nonzero__() """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551AB380>, '__repr__': <slot wrapper '__repr__' of 'renderdoc.ResultDetails' objects>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ResultDetails' objects>, '__str__': <slot wrapper '__str__' of 'renderdoc.ResultDetails' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ResultDetails' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ResultDetails' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ResultDetails' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ResultDetails' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ResultDetails' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ResultDetails' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ResultDetails' objects>, '__bool__': <slot wrapper '__bool__' of 'renderdoc.ResultDetails' objects>, 'OK': <method 'OK' of 'renderdoc.ResultDetails' objects>, '__nonzero__': <method '__nonzero__' of 'renderdoc.ResultDetails' objects>, 'Message': <method 'Message' of 'renderdoc.ResultDetails' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ResultDetails' objects>, 'code': <attribute 'code' of 'renderdoc.ResultDetails' objects>, '__doc__': '\\nA general result from an operation with optional string information for failures.\\n\\nThis struct can be compared directly to a :class:`ResultCode` for simple checks of status, and when\\nconverted to a string it includes the formatted result code and message as appropriate.\\n\\n.. note::\\n\\n  The string information is only valid until :func:`ShutdownReplay` is called. After that point,\\n  accessing the string information is invalid and may crash. Care should be taken if\\n  :func:`ShutdownReplay` is called in response to an error, that the error code is read and saved.\\n\\n  Copying the `ResultDetails` instance is *not* sufficient to preserve the string information. It\\n  should be copied to e.g. a `Tuple[ResultCode, str]` instead.\\n\\n'})"


