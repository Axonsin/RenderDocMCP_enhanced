from ._FloatVector import FloatVector

from typing import overload

class AxisMapping():
    # Original docstring
    """
    A transform to map the x, y, and z axes to new directions.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised AxisMapping.
        """
        pass
    
    @overload
    def __init__(self, other: 'AxisMapping'):
        """
        Construct a new AxisMapping with a deep copy of the input.
        """
        pass
    
    @overload
    def __init__(self, xAxis: FloatVector, yAxis: FloatVector, zAxis: FloatVector):
        """
        Construct a new AxisMapping using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def xAxis(self) -> FloatVector:
        """
        The mapping of the x axis.
        
        :type: FloatVector
        """
        pass
    
    @xAxis.setter
    def xAxis(self, value: FloatVector):
        pass
    
    @property
    def zAxis(self) -> FloatVector:
        """
        The mapping of the z axis.
        
        :type: FloatVector
        """
        pass
    
    @zAxis.setter
    def zAxis(self, value: FloatVector):
        pass
    
    @property
    def yAxis(self) -> FloatVector:
        """
        The mapping of the y axis.
        
        :type: FloatVector
        """
        pass
    
    @yAxis.setter
    def yAxis(self, value: FloatVector):
        pass
    
