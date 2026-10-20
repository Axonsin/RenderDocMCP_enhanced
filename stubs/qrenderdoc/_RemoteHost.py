from renderdoc import DeviceProtocolController, RemoteServer, ResultDetails
from typing import Tuple

from typing import overload

class RemoteHost():
    # Original docstring
    """
    A handle for interacting with a remote server on a given host.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised RemoteHost.
        """
        pass
    
    @overload
    def __init__(self, other: 'RemoteHost'):
        """
        Construct a new RemoteHost with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, hostname: str):
        """
        Construct a new RemoteHost using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def CheckStatus(self):
        """
        Ping the host to check current status - if the server is running, connection status, etc.
        """
        pass
    
    
    def Launch(self) -> ResultDetails:
        """
        Runs the command specified in :meth:`RunCommand`. Returns
        :class:`~renderdoc.ResultDetails` which indicates success or the type of failure.
        
        :return: The result from launching the remote server.
        :rtype: renderdoc.ResultDetails
        """
        pass
    
    
    def IsServerRunning(self) -> bool:
        """
        :return: ``True`` if a remote server is currently running on this host.
        :rtype: bool
        """
        pass
    
    
    def IsConnected(self) -> bool:
        """
        :return: ``True`` if an active connection exists to this remote server.
        :rtype: bool
        """
        pass
    
    
    def IsBusy(self) -> bool:
        """
        :return: ``True`` if someone else is currently connected to this server.
        :rtype: bool
        """
        pass
    
    
    def IsVersionMismatch(self) -> bool:
        """
        :return: ``True`` if there is a code version mismatch with this server.
        :rtype: bool
        """
        pass
    
    
    def VersionMismatchError(self) -> str:
        """
        :return: The version mismatch error.
        :rtype: str
        """
        pass
    
    
    def Hostname(self) -> str:
        """
        :return: The hostname of this host.
        :rtype: str
        """
        pass
    
    
    def FriendlyName(self) -> str:
        """
        :return: The friendly name for this host, if available (if empty, the Hostname is used).
        :rtype: str
        """
        pass
    
    
    def RunCommand(self) -> str:
        """
        :return: The command to run locally to try to launch the server remotely.
        :rtype: str
        """
        pass
    
    
    def SetRunCommand(self, cmd: str):
        """
        Sets the run command. See :meth:`RunCommand`.
        
        :param str cmd: The new command to set.
        """
        pass
    
    
    def LastCapturePath(self) -> str:
        """
        :return: The last folder browsed to on this host, to provide a reasonable default path.
        :rtype: str
        """
        pass
    
    
    def SetLastCapturePath(self, path: str):
        """
        Sets the last folder browsed to. See :meth:`LastCapturePath`.
        
        :param str path: The new path to set.
        """
        pass
    
    
    def Connect(self) -> Tuple[ResultDetails, RemoteServer]:
        """
        Create a connection to the remote server.
        
        :return: The status of opening the capture, whether success or failure, and a :class:`~renderdoc.RemoteServer`
          instance if it were successful
        :rtype: Tuple[renderdoc.ResultDetails, renderdoc.RemoteServer]
        """
        pass
    
    
    def Protocol(self) -> DeviceProtocolController:
        """
        :return: The :class:`~renderdoc.DeviceProtocolController` for this host, or ``None`` if no protocol
          is in use
        :rtype: renderdoc.DeviceProtocolController
        """
        pass
    
    
    def Name(self) -> str:
        """
        :return: The name to display for this host in the UI, either :meth:`FriendlyName` if it is valid, or
          :meth:`Hostname` if not.
        :rtype: str
        """
        pass
    
    
    def IsLocalhost(self) -> bool:
        """
        :return: Returns ``True`` if this host represents the special localhost device.
        :rtype: bool
        """
        pass
    
    
    def IsValid(self) -> bool:
        """
        :return: Returns ``True`` if this host represents a valid remote host.
        :rtype: bool
        """
        pass
    
