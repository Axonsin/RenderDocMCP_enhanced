# Stubs for {module.__name__}

from typing import List

# Dummy types
from typing import NewType, Optional
QWidget = Optional[NewType('QWidget', int)]

# Classes
from ._APIInspector import APIInspector
from ._AnnotationViewer import AnnotationViewer
from ._BufferInterpreter import BufferInterpreter
from ._BufferViewer import BufferViewer
from ._BugReport import BugReport
from ._CaptureConnection import CaptureConnection
from ._ClosedCallback import ClosedCallback
from .qrenderdoc_circular1 import CaptureContext
from ._CaptureDialog import CaptureDialog
from ._CaptureModifications import CaptureModifications
from ._CaptureSettings import CaptureSettings
from ._CaptureViewer import CaptureViewer
from ._CommentView import CommentView
from ._ConnectedTempCapture import ConnectedTempCapture
from ._ContextMenu import ContextMenu
from ._DebugMessageView import DebugMessageView
from ._DescriptorViewer import DescriptorViewer
from ._DiagnosticLogView import DiagnosticLogView
from ._DialogButton import DialogButton
from ._DockReference import DockReference
from ._EventBookmark import EventBookmark
from .qrenderdoc_circular1 import EventBrowser
from ._EventFilterCallback import EventFilterCallback
from ._FilterParseCallback import FilterParseCallback
from ._AutoCompleteCallback import AutoCompleteCallback
from .qrenderdoc_circular1 import ExtensionManager
from ._ExtensionCallback import ExtensionCallback
from ._ExtensionMetadata import ExtensionMetadata
from ._FollowType import FollowType
from ._MainWindow import MainWindow
from ._ShortcutCallback import ShortcutCallback
from .qrenderdoc_circular1 import MiniQtHelper
from ._WidgetCallback import WidgetCallback
from ._UIInvokeCallback import UIInvokeCallback
from ._OffsetSizeDisplayMode import OffsetSizeDisplayMode
from ._PackingRules import PackingRules
from ._PanelMenu import PanelMenu
from ._ParseError import ParseError
from ._ParsedBufferFormat import ParsedBufferFormat
from ._PerformanceCounterViewer import PerformanceCounterViewer
from ._PersistentConfig import PersistentConfig
from ._PipelineStage import PipelineStage
from ._PipelineStateViewer import PipelineStateViewer
from ._PixelHistoryView import PixelHistoryView
from ._PythonShell import PythonShell
from ._RGPInterop import RGPInterop
from ._RemoteHost import RemoteHost
from ._ReplayManager import ReplayManager
from ._ReplayInvokeCallback import ReplayInvokeCallback
from ._DirectoryBrowseCallback import DirectoryBrowseCallback
from ._ResourceInspector import ResourceInspector
from ._ShaderMessageViewer import ShaderMessageViewer
from ._ShaderProcessingTool import ShaderProcessingTool
from ._ShaderToolOutput import ShaderToolOutput
from ._ShaderViewer import ShaderViewer
from ._SaveCallback import SaveCallback
from ._RevertCallback import RevertCallback
from ._StatisticsViewer import StatisticsViewer
from ._TextureViewer import TextureViewer
from ._TimeUnit import TimeUnit
from ._TimelineBar import TimelineBar
from ._WindowMenu import WindowMenu

# Functions


def AddRecentFile(recentList: List[str], file: str):
    """
    Checks if a given file is in a list. If it is, then it's shuffled to the end. If it's
    not then it's added to the end
    
    As the name suggests, this is used for tracking a 'recent file' list.
    
    :param List[str] recentList: The list that is mutated by the function.
    :param str file: The file to add to the list.
    """
    pass



def ConfigFilePath(filename: str) -> str:
    """
    Retrieve the absolute path where a given file can be stored with other application
    data.
    
    :param str filename: The base filename.
    :return: The absolute path.
    :rtype: str
    """
    pass



def RemoveRecentFile(recentList: List[str], file: str):
    """
    Removes a given file from the list, after normalising the path. If the path isn't
    present then the list is not modified.
    
    As the name suggests, this is used for tracking a 'recent file' list.
    
    :param List[str] recentList: The list that is mutated by the function.
    :param str file: The file to remove from the list.
    """
    pass



def UnitSuffix(unit: TimeUnit) -> str:
    """
    Gets the suffix for a time unit.
    
    :param TimeUnit unit: The unit to get a suffix for.
    :return: The one or two character suffix.
    :rtype: str
    """
    pass

