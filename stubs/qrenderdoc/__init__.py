# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


# classes

from .AnnotationViewer import AnnotationViewer
from .APIInspector import APIInspector
from .BufferViewer import BufferViewer
from .BugReport import BugReport
from .CaptureContext import CaptureContext
from .CaptureDialog import CaptureDialog
from .CaptureModifications import CaptureModifications
from .CaptureSettings import CaptureSettings
from .CaptureViewer import CaptureViewer
from .CommentView import CommentView
from .ContextMenu import ContextMenu
from .DebugMessageView import DebugMessageView
from .DescriptorViewer import DescriptorViewer
from .DiagnosticLogView import DiagnosticLogView
from .DialogButton import DialogButton
from .DockReference import DockReference
from .EventBookmark import EventBookmark
from .EventBrowser import EventBrowser
from .ExtensionManager import ExtensionManager
from .ExtensionMetadata import ExtensionMetadata
from .FollowType import FollowType
from .MainWindow import MainWindow
from .MiniQtHelper import MiniQtHelper
from .OffsetSizeDisplayMode import OffsetSizeDisplayMode
from .PanelMenu import PanelMenu
from .PerformanceCounterViewer import PerformanceCounterViewer
from .PersistantConfig import PersistantConfig
from .PipelineStage import PipelineStage
from .PipelineStateViewer import PipelineStateViewer
from .PixelHistoryView import PixelHistoryView
from .PythonShell import PythonShell
from .rdcarray_of_BugReport import rdcarray_of_BugReport
from .rdcarray_of_DialogButton import rdcarray_of_DialogButton
from .rdcarray_of_EventBookmark import rdcarray_of_EventBookmark
from .rdcarray_of_ExtensionMetadata import rdcarray_of_ExtensionMetadata
from .rdcarray_of_ptr_ICaptureViewer import rdcarray_of_ptr_ICaptureViewer
from .rdcarray_of_rdcstrpair import rdcarray_of_rdcstrpair
from .rdcarray_of_RemoteHost import rdcarray_of_RemoteHost
from .rdcarray_of_ShaderProcessingTool import rdcarray_of_ShaderProcessingTool
from .RemoteHost import RemoteHost
from .ReplayManager import ReplayManager
from .ResourceInspector import ResourceInspector
from .RGPInterop import RGPInterop
from .ShaderMessageViewer import ShaderMessageViewer
from .ShaderProcessingTool import ShaderProcessingTool
from .ShaderToolOutput import ShaderToolOutput
from .ShaderViewer import ShaderViewer
from .StatisticsViewer import StatisticsViewer
from .TextureViewer import TextureViewer
from .TimelineBar import TimelineBar
from .TimeUnit import TimeUnit
from .WindowMenu import WindowMenu

# functions

def AddRecentFile(recentList: List[str], file: str): # real signature unknown; restored from __doc__
    """
    AddRecentFile(recentList, file)
    
    Checks if a given file is in a list. If it is, then it's shuffled to the end. If it's
    not then it's added to the end
    
    As the name suggests, this is used for tracking a 'recent file' list.
    
    :param List[str] recentList: The list that is mutated by the function.
    :param str file: The file to add to the list.
    """
    pass

def ConfigFilePath(filename: str) -> str: # real signature unknown; restored from __doc__
    """
    ConfigFilePath(filename)
    
    Retrieve the absolute path where a given file can be stored with other application
    data.
    
    :param str filename: The base filename.
    :return: The absolute path.
    :rtype: str
    """
    pass

def RemoveRecentFile(recentList: List[str], file: str): # real signature unknown; restored from __doc__
    """
    RemoveRecentFile(recentList, file)
    
    Removes a given file from the list, after normalising the path. If the path isn't
    present then the list is not modified.
    
    As the name suggests, this is used for tracking a 'recent file' list.
    
    :param List[str] recentList: The list that is mutated by the function.
    :param str file: The file to remove from the list.
    """
    pass

def SWIG_PyInstanceMethod_New(*args, **kwargs): # real signature unknown
    pass

def UnitSuffix(unit: TimeUnit) -> str: # real signature unknown; restored from __doc__
    """
    UnitSuffix(unit)
    
    Gets the suffix for a time unit.
    
    :param TimeUnit unit: The unit to get a suffix for.
    :return: The one or two character suffix.
    :rtype: str
    """
    pass

# variables with complex values

__all__ = [
    'SWIG_PyInstanceMethod_New',
    'ConfigFilePath',
    'UnitSuffix',
    'AddRecentFile',
    'RemoveRecentFile',
    'CaptureSettings',
    'MainWindow',
    'EventBrowser',
    'APIInspector',
    'AnnotationViewer',
    'PipelineStage',
    'PipelineStateViewer',
    'FollowType',
    'TextureViewer',
    'BufferViewer',
    'ResourceInspector',
    'CaptureDialog',
    'DebugMessageView',
    'DiagnosticLogView',
    'CommentView',
    'StatisticsViewer',
    'TimelineBar',
    'PerformanceCounterViewer',
    'PythonShell',
    'ShaderViewer',
    'ShaderMessageViewer',
    'DescriptorViewer',
    'PixelHistoryView',
    'CaptureViewer',
    'ReplayManager',
    'DockReference',
    'CaptureModifications',
    'EventBookmark',
    'RGPInterop',
    'CaptureContext',
    'ShaderToolOutput',
    'ShaderProcessingTool',
    'BugReport',
    'OffsetSizeDisplayMode',
    'TimeUnit',
    'PersistantConfig',
    'RemoteHost',
    'WindowMenu',
    'PanelMenu',
    'ContextMenu',
    'DialogButton',
    'ExtensionMetadata',
    'MiniQtHelper',
    'ExtensionManager',
    'rdcarray_of_EventBookmark',
    'rdcarray_of_ShaderProcessingTool',
    'rdcarray_of_rdcstrpair',
    'rdcarray_of_BugReport',
    'rdcarray_of_ExtensionMetadata',
    'rdcarray_of_DialogButton',
    'rdcarray_of_RemoteHost',
    'rdcarray_of_ptr_ICaptureViewer',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F816E2C2B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='qrenderdoc', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F816E2C2B0>, origin='C:\\\\Users\\\\13908\\\\Desktop\\\\works\\\\renderdoc_pythonmodules\\\\x64\\\\Development\\\\pymodules\\\\qrenderdoc.pyd')"

