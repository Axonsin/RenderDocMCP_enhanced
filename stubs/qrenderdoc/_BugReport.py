from datetime import datetime

from typing import overload

class BugReport():
    # Original docstring
    """
    Describes a submitted bug report.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised BugReport.
        """
        pass
    
    @overload
    def __init__(self, other: 'BugReport'):
        """
        Construct a new BugReport with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def URL(self) -> str:
        """
        Gets the URL for this report.
        
        :return: The URL to the report.
        :rtype: str
        """
        pass
    
    @property
    def submitDate(self) -> datetime:
        """
        The original date when this bug was submitted.
        
        :type: datetime
        """
        pass
    
    @submitDate.setter
    def submitDate(self, value: datetime):
        pass
    
    @property
    def checkDate(self) -> datetime:
        """
        The last date that we checked for updates.
        
        :type: datetime
        """
        pass
    
    @checkDate.setter
    def checkDate(self, value: datetime):
        pass
    
    @property
    def reportId(self) -> str:
        """
        The private ID of the bug report.
        
        :type: str
        """
        pass
    
    @reportId.setter
    def reportId(self, value: str):
        pass
    
    @property
    def unreadUpdates(self) -> bool:
        """
        Unread updates to the bug exist
        
        :type: bool
        """
        pass
    
    @unreadUpdates.setter
    def unreadUpdates(self, value: bool):
        pass
    
