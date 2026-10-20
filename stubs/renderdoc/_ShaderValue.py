from typing import Tuple

from typing import overload

class ShaderValue():
    # Original docstring
    """
    A C union that holds 16 values, with each different basic variable type.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised ShaderValue.
        """
        pass
    
    @overload
    def __init__(self, other: 'ShaderValue'):
        """
        Construct a new ShaderValue with a deep copy of the input.
        """
        pass
    
    
    def __init__(self): pass
    
    @property
    def u32v(self) -> Tuple[int, ...]:
        """
        16-tuple of 32-bit unsigned integer values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @u32v.setter
    def u32v(self, value: Tuple[int, ...]):
        pass
    
    @property
    def s16v(self) -> Tuple[int, ...]:
        """
        16-tuple of 16-bit signed integer values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @s16v.setter
    def s16v(self, value: Tuple[int, ...]):
        pass
    
    @property
    def f32v(self) -> Tuple[float, ...]:
        """
        16-tuple of ``float`` values.
        
        :type: Tuple[float,...]
        """
        pass
    
    @f32v.setter
    def f32v(self, value: Tuple[float, ...]):
        pass
    
    @property
    def u16v(self) -> Tuple[int, ...]:
        """
        16-tuple of 16-bit unsigned integer values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @u16v.setter
    def u16v(self, value: Tuple[int, ...]):
        pass
    
    @property
    def f16v(self) -> Tuple[int, ...]:
        """
        16-tuple of 16-bit half-precision float values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @f16v.setter
    def f16v(self, value: Tuple[int, ...]):
        pass
    
    @property
    def s64v(self) -> Tuple[int, ...]:
        """
        16-tuple of 64-bit signed integer values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @s64v.setter
    def s64v(self, value: Tuple[int, ...]):
        pass
    
    @property
    def s8v(self) -> Tuple[int, ...]:
        """
        16-tuple of 8-bit signed integer values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @s8v.setter
    def s8v(self, value: Tuple[int, ...]):
        pass
    
    @property
    def u64v(self) -> Tuple[int, ...]:
        """
        16-tuple of 64-bit unsigned integer values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @u64v.setter
    def u64v(self, value: Tuple[int, ...]):
        pass
    
    @property
    def f64v(self) -> Tuple[float, ...]:
        """
        16-tuple of ``double`` values.
        
        :type: Tuple[float,...]
        """
        pass
    
    @f64v.setter
    def f64v(self, value: Tuple[float, ...]):
        pass
    
    @property
    def u8v(self) -> Tuple[int, ...]:
        """
        16-tuple of 8-bit unsigned integer values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @u8v.setter
    def u8v(self, value: Tuple[int, ...]):
        pass
    
    @property
    def s32v(self) -> Tuple[int, ...]:
        """
        16-tuple of 32-bit signed integer values.
        
        :type: Tuple[int,...]
        """
        pass
    
    @s32v.setter
    def s32v(self, value: Tuple[int, ...]):
        pass
    
