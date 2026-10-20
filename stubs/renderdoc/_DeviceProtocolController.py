from ._ResultDetails import ResultDetails
from typing import List

class DeviceProtocolController():
    # Original docstring
    """
    An interface for enumerating and controlling remote devices.
    """
    
    
    
    def GetProtocolName(self) -> str:
        """
        Retrieves the name of this protocol as passed to :func:`GetDeviceProtocolController`.
        
        :return: A string identifying the protocol.
        :rtype: str
        """
        pass
    
    
    def GetDevices(self) -> List[str]:
        """
        Returns a list of devices currently available through the given protocol.
        
        Until a device is enumerated through this function it may not be available for connection through
        other methods such as target control or remote server access, even if the device is physically
        connected, due to initialisation happening only when enumerated.
        
        The returned string is the hostname of the device, which can be connected via
        ``protocol://hostname`` with interfaces that take a hostname.
        
        :return: A list of the devices currently available.
        :rtype: List[str]
        """
        pass
    
    
    def GetFriendlyName(self, URL: str) -> str:
        """
        Retrieves the user friendly name of the given device. This may be easier for a user to
        correlate to a device than the hostname which may be only a programmatic identifier.
        
        :param str URL: The URL of the device in the form ``protocol://host``, with protocol as returned by
          :func:`GetProtocolName` and host as returned by :func:`GetDevices`.
        :return: A string identifying the device.
        :rtype: str
        """
        pass
    
    
    def SupportsMultiplePrograms(self, URL: str) -> bool:
        """
        Query if the device supports multiple programs running and being captured. If not, the
        user can be prompted to close an existing program before a new one is launched.
        
        :param str URL: The URL of the device in the form ``protocol://host``, with protocol as returned by
          :func:`GetProtocolName` and host as returned by :func:`GetDevices`.
        :return: ``True`` if the device supports multiple programs, ``False`` otherwise.
        :rtype: bool
        """
        pass
    
    
    def IsSupported(self, URL: str) -> bool:
        """
        Query if the device supports RenderDoc capture and replay.
        
        :param str URL: The URL of the device in the form ``protocol://host``, with protocol as returned by
          :func:`GetProtocolName` and host as returned by :func:`GetDevices`.
        :return: ``True`` if any the device is supported, ``False`` otherwise.
        :rtype: bool
        """
        pass
    
    
    def StartRemoteServer(self, URL: str) -> ResultDetails:
        """
        Start the remote server running on the given device.
        
        :param str URL: The URL of the device in the form ``protocol://host``, with protocol as returned by
          :func:`GetProtocolName` and host as returned by :func:`GetDevices`.
        :return: The status of starting the server, whether success or failure.
        :rtype: ResultDetails
        """
        pass
    
