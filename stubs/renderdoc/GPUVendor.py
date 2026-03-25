# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GPUVendor(__enum.IntEnum):
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
    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    AMD = 2
    """ An AMD GPU """

    ARM = 1
    """ An ARM GPU """

    Broadcom = 3
    """ A Broadcom GPU """

    Imagination = 4
    """ An Imagination GPU """

    Intel = 5
    """ An Intel GPU """

    nVidia = 6
    """ An nVidia GPU """

    Qualcomm = 7
    """ A Qualcomm  GPU """

    Samsung = 10
    """ A Samsung GPU """

    Software = 9
    """ A software-rendering emulated GPU """

    Unknown = 0
    """ A GPU from an unknown vendor """

    Verisilicon = 8
    """ A Verisilicon or Vivante GPU """



