from ._SDObjectPODData import SDObjectPODData

class SDObjectData():
    # Original docstring
    """
    The data inside an :class:`SDObject` whether it's plain old data or complex children.
    """
    
    
    @property
    def string(self) -> str:
        """
        The string contents of the object.
        
        :type: str
        """
        pass
    
    @string.setter
    def string(self, value: str):
        pass
    
    @property
    def basic(self) -> SDObjectPODData:
        """
        The plain-old data contents of the object, in a :class:`SDObjectPODData`.
        
        :type: SDObjectPODData
        """
        pass
    
    @basic.setter
    def basic(self, value: SDObjectPODData):
        pass
    
