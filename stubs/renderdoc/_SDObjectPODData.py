from ._ResourceId import ResourceId

class SDObjectPODData():
    # Original docstring
    """
    The plain-old-data contents of an :class:`SDObject`.
    
    Only one member is valid, as defined by the type of the :class:`SDObject`.
    """
    
    
    @property
    def i(self) -> int:
        """
        The value as a signed integer.
        
        :type: int
        """
        pass
    
    @i.setter
    def i(self, value: int):
        pass
    
    @property
    def b(self) -> bool:
        """
        The value as a boolean.
        
        :type: bool
        """
        pass
    
    @b.setter
    def b(self, value: bool):
        pass
    
    @property
    def c(self) -> str:
        """
        The value as a single byte character.
        
        :type: str
        """
        pass
    
    @c.setter
    def c(self, value: str):
        pass
    
    @property
    def d(self) -> float:
        """
        The value as a floating point number.
        
        :type: float
        """
        pass
    
    @d.setter
    def d(self, value: float):
        pass
    
    @property
    def id(self) -> ResourceId:
        """
        The value as a :class:`ResourceId`
        
        :type: ResourceId
        """
        pass
    
    @id.setter
    def id(self, value: ResourceId):
        pass
    
    @property
    def u(self) -> int:
        """
        The value as an unsigned integer.
        
        :type: int
        """
        pass
    
    @u.setter
    def u(self, value: int):
        pass
    
