# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.DeviceProtocolController import DeviceProtocolController

from renderdoc.RemoteServer import RemoteServer

from renderdoc.ResultDetails import ResultDetails

class RemoteHost(): # skipped bases: <class 'SwigPyObject'>
    """ A handle for interacting with a remote server on a given host. """
    def CheckStatus(self): # real signature unknown; restored from __doc__
        """
        CheckStatus()
        
        Ping the host to check current status - if the server is running, connection status, etc.
        """
        pass

    def Connect(self, server) -> Tuple[RemoteServer]: # real signature unknown; restored from __doc__
        """
        Connect(server)
        
        Create a connection to the remote server.
        
        :return: The status of opening the capture, whether success or failure, and a :class:`RemoteServer`
          instance if it were successful
        :rtype: Tuple[renderdoc.ResultDetails, renderdoc.RemoteServer]
        """
        pass

    def FriendlyName(self) -> str: # real signature unknown; restored from __doc__
        """
        FriendlyName()
        
        
        :return: The friendly name for this host, if available (if empty, the Hostname is used).
        :rtype: str
        """
        pass

    def Hostname(self) -> str: # real signature unknown; restored from __doc__
        """
        Hostname()
        
        
        :return: The hostname of this host.
        :rtype: str
        """
        pass

    def IsBusy(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsBusy()
        
        
        :return: ``True`` if someone else is currently connected to this server.
        :rtype: bool
        """
        pass

    def IsConnected(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsConnected()
        
        
        :return: ``True`` if an active connection exists to this remote server.
        :rtype: bool
        """
        pass

    def IsLocalhost(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsLocalhost()
        
        
        :return: Returns ``True`` if this host represents the special localhost device.
        :rtype: bool
        """
        pass

    def IsServerRunning(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsServerRunning()
        
        
        :return: ``True`` if a remote server is currently running on this host.
        :rtype: bool
        """
        pass

    def IsValid(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsValid()
        
        Returns ``True`` if this host represents a valid remote host.
        :rtype: bool
        """
        pass

    def IsVersionMismatch(self) -> bool: # real signature unknown; restored from __doc__
        """
        IsVersionMismatch()
        
        
        :return: ``True`` if there is a code version mismatch with this server.
        :rtype: bool
        """
        pass

    def LastCapturePath(self) -> str: # real signature unknown; restored from __doc__
        """
        LastCapturePath()
        
        
        :return: The last folder browsed to on this host, to provide a reasonable default path.
        :rtype: str
        """
        pass

    def Launch(self) -> ResultDetails: # real signature unknown; restored from __doc__
        """
        Launch()
        
        Runs the command specified in :data:`runCommand`. Returns
        :class:`~renderdoc.ResultDetails` which indicates success or the type of failure.
        
        :return: The result from launching the remote server.
        :rtype: renderdoc.ResultDetails
        """
        pass

    def Name(self) -> str: # real signature unknown; restored from __doc__
        """
        Name()
        
        
        :return: The name to display for this host in the UI, either :meth:`FriendlyName` if it is valid, or
          :meth:`Hostname` if not.
        :rtype: str
        """
        pass

    def Protocol(self) -> DeviceProtocolController: # real signature unknown; restored from __doc__
        """
        Protocol()
        
        
        :return: The :class:`~renderdoc.DeviceProtocolController` for this host, or ``None`` if no protocol
          is in use
        :rtype: renderdoc.DeviceProtocolController
        """
        pass

    def RunCommand(self) -> str: # real signature unknown; restored from __doc__
        """
        RunCommand()
        
        
        :return: The command to run locally to try to launch the server remotely.
        :rtype: str
        """
        pass

    def SetLastCapturePath(self, path: str): # real signature unknown; restored from __doc__
        """
        SetLastCapturePath(path)
        
        Sets the last folder browsed to. See :meth:`LastCapturePath`.
        
        :param str path: The new path to set.
        """
        pass

    def SetRunCommand(self, cmd: str): # real signature unknown; restored from __doc__
        """
        SetRunCommand(cmd)
        
        Sets the run command. See :meth:`RunCommand`.
        
        :param str cmd: The new command to set.
        """
        pass

    def VersionMismatchError(self) -> str: # real signature unknown; restored from __doc__
        """
        VersionMismatchError()
        
        
        :return: The version mismatch error.
        :rtype: str
        """
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5012F350>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.RemoteHost' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.RemoteHost' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.RemoteHost' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.RemoteHost' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.RemoteHost' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.RemoteHost' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.RemoteHost' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.RemoteHost' objects>, 'CheckStatus': <method 'CheckStatus' of 'qrenderdoc.RemoteHost' objects>, 'Launch': <method 'Launch' of 'qrenderdoc.RemoteHost' objects>, 'IsServerRunning': <method 'IsServerRunning' of 'qrenderdoc.RemoteHost' objects>, 'IsConnected': <method 'IsConnected' of 'qrenderdoc.RemoteHost' objects>, 'IsBusy': <method 'IsBusy' of 'qrenderdoc.RemoteHost' objects>, 'IsVersionMismatch': <method 'IsVersionMismatch' of 'qrenderdoc.RemoteHost' objects>, 'VersionMismatchError': <method 'VersionMismatchError' of 'qrenderdoc.RemoteHost' objects>, 'Hostname': <method 'Hostname' of 'qrenderdoc.RemoteHost' objects>, 'FriendlyName': <method 'FriendlyName' of 'qrenderdoc.RemoteHost' objects>, 'RunCommand': <method 'RunCommand' of 'qrenderdoc.RemoteHost' objects>, 'SetRunCommand': <method 'SetRunCommand' of 'qrenderdoc.RemoteHost' objects>, 'LastCapturePath': <method 'LastCapturePath' of 'qrenderdoc.RemoteHost' objects>, 'SetLastCapturePath': <method 'SetLastCapturePath' of 'qrenderdoc.RemoteHost' objects>, 'Connect': <method 'Connect' of 'qrenderdoc.RemoteHost' objects>, 'Protocol': <method 'Protocol' of 'qrenderdoc.RemoteHost' objects>, 'Name': <method 'Name' of 'qrenderdoc.RemoteHost' objects>, 'IsLocalhost': <method 'IsLocalhost' of 'qrenderdoc.RemoteHost' objects>, 'IsValid': <method 'IsValid' of 'qrenderdoc.RemoteHost' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.RemoteHost' objects>, '__doc__': 'A handle for interacting with a remote server on a given host.'})"


