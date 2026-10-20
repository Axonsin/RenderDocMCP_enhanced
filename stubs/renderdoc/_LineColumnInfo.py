
from typing import overload

class LineColumnInfo():
    # Original docstring
    """
    Details the current region of code that an instruction maps to.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised LineColumnInfo.
        """
        pass
    
    @overload
    def __init__(self, other: 'LineColumnInfo'):
        """
        Construct a new LineColumnInfo with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def SourceEqual(self, o: 'LineColumnInfo') -> bool:
        """
        :param LineColumnInfo o: The object to compare against.
        :return: ``True`` if this object is equal to the parameter, disregarding :data:`disassemblyLine`.
        :rtype: bool
        """
        pass
    
    @property
    def disassemblyLine(self) -> int:
        """
        The line (starting from 1) in the disassembly where this instruction is located.
        
        :type: int
        """
        pass
    
    @disassemblyLine.setter
    def disassemblyLine(self, value: int):
        pass
    
    @property
    def fileIndex(self) -> int:
        """
        The current file, as an index into the list of files for this shader.
        
        If this is negative, no source mapping is available and only :data:`disassemblyLine` is valid.
        
        :type: int
        """
        pass
    
    @fileIndex.setter
    def fileIndex(self, value: int):
        pass
    
    @property
    def lineEnd(self) -> int:
        """
        The ending line-number (starting from 1) of the source code.
        
        :type: int
        """
        pass
    
    @lineEnd.setter
    def lineEnd(self, value: int):
        pass
    
    @property
    def lineStart(self) -> int:
        """
        The starting line-number (starting from 1) of the source code.
        
        :type: int
        """
        pass
    
    @lineStart.setter
    def lineStart(self, value: int):
        pass
    
    @property
    def colStart(self) -> int:
        """
        The column number (starting from 1) of the start of the code on the line specified by
        :data:`lineStart`. If set to 0, no column information is available and the whole lines should be
        treated as covering the code.
        
        :type: int
        """
        pass
    
    @colStart.setter
    def colStart(self, value: int):
        pass
    
    @property
    def colEnd(self) -> int:
        """
        The column number (starting from 1) of the end of the code on the line specified by
        :data:`lineEnd`. If set to 0, no column information is available and the whole lines should be
        treated as covering the code.
        
        :type: int
        """
        pass
    
    @colEnd.setter
    def colEnd(self, value: int):
        pass
    
