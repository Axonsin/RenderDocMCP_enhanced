from enum import IntEnum

class GPUVendor(IntEnum):
    # Original docstring
    """
    Identifies a GPU vendor.
    
    .. data:: Unknown
    
      A GPU from an unknown vendor
    
    .. data:: ARM
    
      An ARM GPU
    
    .. data:: AMD
    
      An AMD GPU
    
    .. data:: Broadcom
    
      A Broadcom GPU
    
    .. data:: Imagination
    
      An Imagination GPU
    
    .. data:: Intel
    
      An Intel GPU
    
    .. data:: nVidia
    
      An nVidia GPU
    
    .. data:: Qualcomm
    
      A Qualcomm  GPU
    
    .. data:: Verisilicon
    
      A Verisilicon or Vivante GPU
    
    .. data:: Software
    
      A software-rendering emulated GPU
    
    .. data:: Samsung
    
      A Samsung GPU
    """
    
    
    # Enum values
    
    Unknown = 0
    """
    A GPU from an unknown vendor
    """
    
    ARM = 1
    """
    An ARM GPU
    """
    
    AMD = 2
    """
    An AMD GPU
    """
    
    Broadcom = 3
    """
    A Broadcom GPU
    """
    
    Imagination = 4
    """
    An Imagination GPU
    """
    
    Intel = 5
    """
    An Intel GPU
    """
    
    nVidia = 6
    """
    An nVidia GPU
    """
    
    Qualcomm = 7
    """
    A Qualcomm  GPU
    """
    
    Verisilicon = 8
    """
    A Verisilicon or Vivante GPU
    """
    
    Software = 9
    """
    A software-rendering emulated GPU
    """
    
    Samsung = 10
    """
    A Samsung GPU
    """
    

# Assign __doc__ for enum values for easier introspection

GPUVendor.Unknown.__doc__ = """
A GPU from an unknown vendor
"""

GPUVendor.ARM.__doc__ = """
An ARM GPU
"""

GPUVendor.AMD.__doc__ = """
An AMD GPU
"""

GPUVendor.Broadcom.__doc__ = """
A Broadcom GPU
"""

GPUVendor.Imagination.__doc__ = """
An Imagination GPU
"""

GPUVendor.Intel.__doc__ = """
An Intel GPU
"""

GPUVendor.nVidia.__doc__ = """
An nVidia GPU
"""

GPUVendor.Qualcomm.__doc__ = """
A Qualcomm  GPU
"""

GPUVendor.Verisilicon.__doc__ = """
A Verisilicon or Vivante GPU
"""

GPUVendor.Software.__doc__ = """
A software-rendering emulated GPU
"""

GPUVendor.Samsung.__doc__ = """
A Samsung GPU
"""

