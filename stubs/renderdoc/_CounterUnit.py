from enum import IntEnum

class CounterUnit(IntEnum):
    # Original docstring
    """
    The unit that GPU counter data is returned in.
    
    .. data:: Absolute
    
      The value is an absolute value and should be interpreted as unitless.
    
    .. data:: Seconds
    
      The value is a duration in seconds.
    
    .. data:: Percentage
    
      The value is a floating point percentage value between 0.0 and 1.0.
    
    .. data:: Ratio
    
      The value describes a ratio between two separate GPU units or counters.
    
    .. data:: Bytes
    
      The value is in bytes.
    
    .. data:: Cycles
    
      The value is a duration in clock cycles.
    
    .. data:: Hertz
    
      The value is a value in Hertz (cycles per second).
    
    .. data:: Volt
    
      The value is a value in Volts.
    
    .. data:: Celsius
    
      The value is a value in Celsius.
    """
    
    
    # Enum values
    
    Absolute = 0
    """
    The value is an absolute value and should be interpreted as unitless.
    """
    
    Seconds = 1
    """
    The value is a duration in seconds.
    """
    
    Percentage = 2
    """
    The value is a floating point percentage value between 0.0 and 1.0.
    """
    
    Ratio = 3
    """
    The value describes a ratio between two separate GPU units or counters.
    """
    
    Bytes = 4
    """
    The value is in bytes.
    """
    
    Cycles = 5
    """
    The value is a duration in clock cycles.
    """
    
    Hertz = 6
    """
    The value is a value in Hertz (cycles per second).
    """
    
    Volt = 7
    """
    The value is a value in Volts.
    """
    
    Celsius = 8
    """
    The value is a value in Celsius.
    """
    

# Assign __doc__ for enum values for easier introspection

CounterUnit.Absolute.__doc__ = """
The value is an absolute value and should be interpreted as unitless.
"""

CounterUnit.Seconds.__doc__ = """
The value is a duration in seconds.
"""

CounterUnit.Percentage.__doc__ = """
The value is a floating point percentage value between 0.0 and 1.0.
"""

CounterUnit.Ratio.__doc__ = """
The value describes a ratio between two separate GPU units or counters.
"""

CounterUnit.Bytes.__doc__ = """
The value is in bytes.
"""

CounterUnit.Cycles.__doc__ = """
The value is a duration in clock cycles.
"""

CounterUnit.Hertz.__doc__ = """
The value is a value in Hertz (cycles per second).
"""

CounterUnit.Volt.__doc__ = """
The value is a value in Volts.
"""

CounterUnit.Celsius.__doc__ = """
The value is a value in Celsius.
"""

