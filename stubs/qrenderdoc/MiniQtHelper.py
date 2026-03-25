# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.ReplayOutput import ReplayOutput

from renderdoc.WindowingData import WindowingData

class MiniQtHelper(): # skipped bases: <class 'SwigPyObject'>
    """
    Python can have direct access to Qt via PySide2, but this is not always available in
    all RenderDoc builds. To aid extensions to manipulate widgets in a simple but portable fashion this
    helper exposes a small subset of Qt via RenderDoc's python bindings.
    
    The intention is not to allow fully flexible building of Qt panels, but to allow access to some
    basic UI building tools for simple data input and display which can be used on any RenderDoc build.
    
    This manager is retrieved by calling :meth:`ExtensionManager.GetMiniQtHelper`.
    
    .. note::
      The widget handles returned are PySide2 widgets where that is available, so this can be used to
      make a basic UI and optionally customise it further with PySide2 when possible.
    
    .. function:: WidgetCallback(context, widget, text)
    
      Not a member function - the signature for any ``WidgetCallback`` callbacks.
    
      Callback for widgets can be registered at creation time, the text field is optional and may be
      blank depending on the event, but the context and widget are always valid.
    
      :param CaptureContext context: The current capture context.
      :param QWidget widget: The widget sending the callback.
      :param str text: Additional data for the call, such as the current or selected text.
    
    .. function:: InvokeCallback(context, widget, text)
    
      Not a member function - the signature for any ``InvokeCallback`` callbacks.
    
      Callback for invoking onto the UI thread from another thread (in particular the replay thread).
      Takes no parameters as the callback is expected to store its own state.
    """
    def AddGridWidget(self, parent: QWidget, row: int, column: int, child: QWidget, rowSpan: int, columnSpan: int): # real signature unknown; restored from __doc__
        """
        AddGridWidget(parent, row, column, child, rowSpan, columnSpan)
        
        Adds a child widget to a grid layout. If the parent is not a grid layout nothing will
        happen and the widget will not be added anywhere.
        
        :param QWidget parent: The parent grid layout widget.
        :param int row: The row at which to add the child widget.
        :param int column: The column at which to add the child widget.
        :param QWidget child: The child widget to add.
        :param int rowSpan: How many rows should this child span over.
        :param int columnSpan: How many columns should this child span over.
        """
        pass

    def AddWidget(self, parent: QWidget, child: QWidget): # real signature unknown; restored from __doc__
        """
        AddWidget(parent, child)
        
        Adds a child widget to the end of an ordered layout (either horizontal or vertical).
        If the parent is not an ordered layout nothing will happen and the widget will not be added anywhere.
        
        :param QWidget parent: The parent grid layout widget.
        :param QWidget child: The child widget to add.
        """
        pass

    def ClearContainedWidgets(self, parent: QWidget): # real signature unknown; restored from __doc__
        """
        ClearContainedWidgets(parent)
        
        Removes all child widgets from a parent and makes them invisible.
        
        These widgets remain valid and can be re-added to another parent or the same parent.
        
        :param QWidget parent: The parent widget to clear of  children.
        """
        pass

    def CloseCurrentDialog(self, success: bool): # real signature unknown; restored from __doc__
        """
        CloseCurrentDialog(success)
        
        Close the active modal dialog. This does nothing if no dialog is being shown.
        
        .. note::
          Closing a dialog 'sucessfully' does nothing except modify the return value of
          :meth:`CloseCurrentDialog`. It allows quick distinguishing between OK and Cancel actions without
          having to carry that information separately in a global or other state.
        
        :param bool success: ``True`` if the dialog was successful (the user clicked an OK/Accept type
          button).
        """
        pass

    def CloseToplevelWidget(self, widget: QWidget): # real signature unknown; restored from __doc__
        """
        CloseToplevelWidget(widget)
        
        Closes a top-level widget as if the user had clicked to close.
        
        This function is undefined if used on a non top-level widget. It will invoke the closed widget
        callback.
        
        :param QWidget widget: The top-level widget to close.
        """
        pass

    def CreateButton(self, pressed: WidgetCallback) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateButton(pressed)
        
        Create a normal button widget.
        
        :param WidgetCallback pressed: Callback to be called when the button is pressed.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateCheckbox(self, changed: WidgetCallback) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateCheckbox(changed)
        
        Create a checkbox widget which can be toggled between unchecked and checked. When
        created the checkbox is unchecked.
        
        :param WidgetCallback changed: Callback to be called when the widget is toggled.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateComboBox(self, editable: bool, changed: WidgetCallback) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateComboBox(editable, changed)
        
        Create a drop-down combo box widget.
        
        When created there are no pre-defined entries in the drop-down section. This can be changed with
        :meth:`SetComboOptions`.
        
        :param bool editable: ``True`` if the widget should allow the user to enter any text they wish as
          well as being able to select a pre-defined entry.
        :param WidgetCallback changed: Callback to be called when the text in the combobox is changed. This
          will be called both when a new option is selected or when the user edits the text.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateGridContainer(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateGridContainer()
        
        Creates and returns a grid layout widget.
        
        The widget needs to be added to a parent to become part of a panel or window.
        
        Children added to this layout widget are arranged in a grid. Widget sizing follows default logic,
        which typically has some widgets be only large enough for their content and others which are
        'greedy' evenly divide any remaining free space. This will not violate the grid constraint though.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateGroupBox(self, collapsible: bool) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateGroupBox(collapsible)
        
        Create a groupbox widget which can optionally allow collapsing.
        
        This widget can have children added, but it is recommended to immediately add only one child which
        is a layout type widget, to allow customising how children are added. By default the children are
        added in a vertical layout.
        
        The widget needs to be added to a parent to become part of a panel or window.
        
        :param bool collapsible: ``True`` if the groupbox should have a toggle in its header to allow
          collapsing its contents down vertically.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateHorizontalContainer(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateHorizontalContainer()
        
        Creates and returns a horizontal layout widget.
        
        The widget needs to be added to a parent to become part of a panel or window.
        
        Children added to this layout widget are listed horizontally. Widget sizing follows default logic,
        which typically has some widgets be only large enough for their content and others which are
        'greedy' evenly divide any remaining free space.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateLabel(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateLabel()
        
        Create a read-only label widget.
        
        .. note::
          This widget will be blank by default, you can set the text with :meth:`SetWidgetText`.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateOutputRenderingWidget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateOutputRenderingWidget()
        
        Create a widget suitable for rendering to with a :class:`renderdoc.ReplayOutput`. This
        widget takes care of painting on demand and recreating the internal display widget when necessary,
        however this means you must use :meth:`GetWidgetWindowingData` to retrieve the windowing data for
        creating the output as well as call :meth:`SetWidgetReplayOutput` to notify the widget of the
        current output.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateProgressBar(self, horizontal: bool) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateProgressBar(horizontal)
        
        Create a progress bar widget.
        
        By default the progress bar has minimum and maximum values of 0 and 100. These can be changed with
        :meth:`SetProgressBarRange`.
        
        :param bool horizontal: the progress bar orientation, true for horizontal otherwise vertical.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateRadiobox(self, changed: WidgetCallback) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateRadiobox(changed)
        
        Create a radio box widget which can be toggled between unchecked and checked but with
        at most one radio box in any group of sibling radio boxes being checked.
        
        Upon creation the radio box is unchecked, even in a group of other radio boxes that are unchecked.
        If you want a default radio box to be checked, you should use :meth:`SetWidgetChecked`.
        
        :param WidgetCallback changed: Callback to be called when the widget is toggled.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateSpacer(self, horizontal: bool) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateSpacer(horizontal)
        
        Creates and returns a spacer widget.
        
        This widget is completely empty but consumes empty space, meaning all other non-greedy widgets in
        the same container will be minimally sized. This can be useful for simple layouts.
        
        :param bool horizontal: ``True`` if this spacer should consume horizontal space, ``False`` if this
          spacer should consume vertical space. Typically this matches the direction of the layout it is
          in.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateSpinbox(self, decimalPlaces: int, step: float) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateSpinbox(decimalPlaces, step)
        
        Create a spinbox widget with a numerical value and up/down buttons to change it.
        
        The number of decimal places can be set to 0 for an integer spinbox, and in that case the step
        should be set to 1.0.
        
        By default the spinbox has minimum and maximum values of 0.0 and 100.0, these can be changed with
        :meth:`SetSpinboxBounds`.
        
        :param int decimalPlaces: The number of decimal places to display when showing the number.
        :param float step: The step value to apply in each direction when clicking up or down.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateTextBox(self, singleLine: bool, changed: WidgetCallback) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateTextBox(singleLine, changed)
        
        Create a text box widget for the user to enter text into.
        
        :param bool singleLine: ``True`` if the widget should be a single-line entry, otherwise it is a
          multi-line text box.
        :param WidgetCallback changed: Callback to be called when the text in the textbox is changed.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateToplevelWidget(self, windowTitle: str, closed: WidgetCallback) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateToplevelWidget(windowTitle, closed)
        
        Creates and returns a top-level widget for creating layouts.
        
        The widget is not immediately visible. It should be shown either with :meth:`ShowWidgetAsDialog` or
        with :meth:`CaptureContext.AddDockWindow` once it's ready.
        
        This widget can have children added, but it is recommended to immediately add only one child which
        is a layout type widget, to allow customising how children are added. By default the children are
        added in a vertical layout.
        
        :param str windowTitle: The title of any window with this widget as its root.
        :param WidgetCallback closed: A callback that will be called when the widget is closed by the user.
          This implicitly deletes the widget and all its children, which will no longer be valid even if a
          handle to them exists.
          Callback function signature must match :func:`WidgetCallback`.
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def CreateVerticalContainer(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        CreateVerticalContainer()
        
        Creates and returns a vertical layout widget.
        
        The widget needs to be added to a parent to become part of a panel or window.
        
        Children added to this layout widget are listed vertically. Widget sizing follows default logic,
        which typically has some widgets be only large enough for their content and others which are
        'greedy' evenly divide any remaining free space.
        
        :return: The handle to the newly created widget.
        :rtype: QWidget
        """
        pass

    def DestroyWidget(self, widget: QWidget): # real signature unknown; restored from __doc__
        """
        DestroyWidget(widget)
        
        Destroy a widget. Widgets stay alive unless explicitly destroyed here, OR in one other
        case when they are in a widget hiearchy under a top-level window which the user closes, which can
        be detected with the callback parameter in :meth:`CreateToplevelWidget`.
        
        If the widget being destroyed is a top-level window, it will be closed. Otherwise if it is part of a
        widget hierarchy it will be removed from its parent automatically. You can remove a widget and then
        destroy it if you wish, but you must not destroy a widget then attempt to remove it from its parent,
        as after the call to this function the widget is no longer valid to use.
        
        All children under this widget will be destroyed recursively as well, which will be made invalid
        even if a handle to them exists.
        
        :param QWidget widget: The widget to destroy.
        """
        pass

    def FindChildByName(self, parent: QWidget, name: str) -> QWidget: # real signature unknown; restored from __doc__
        """
        FindChildByName(parent, name)
        
        Find a child widget of a parent by internal name.
        
        :param QWidget parent: The widget to start the search from.
        :param str name: The internal name to search for.
        :return: The handle to the first widget with a matching name, or ``None`` if no widget is found.
        :rtype: QWidget
        """
        pass

    def GetChild(self, parent: QWidget, index: int) -> QWidget: # real signature unknown; restored from __doc__
        """
        GetChild(parent, index)
        
        Return a child widget for a parent.
        
        :param QWidget parent: The parent widget to look up.
        :param int index: The child index to return.
        :return: The specified child of the parent, or ``None`` if the index is out of bounds.
        :rtype: QWidget
        """
        pass

    def GetComboCount(self, combo: QWidget) -> int: # real signature unknown; restored from __doc__
        """
        GetComboCount(combo)
        
        Get the number of options in a drop-down combo box. If another type of widget is
        passed ``0`` will be returned.
        
        :param QWidget combo: The combo box.
        :return: The current number of options.
        :rtype: int
        """
        pass

    def GetNumChildren(self, widget: QWidget) -> int: # real signature unknown; restored from __doc__
        """
        GetNumChildren(widget)
        
        Return the number of children this widget has. This is generally only useful for
        layout type widgets.
        
        :param QWidget widget: The widget to query.
        :return: The number of child widgets this widget has.
        :rtype: int
        """
        pass

    def GetParent(self, widget: QWidget) -> QWidget: # real signature unknown; restored from __doc__
        """
        GetParent(widget)
        
        Return the parent of a widget in the widget hierarchy.
        
        .. note::
          The widget returned may not be a widget created through this helper interface if the specified
          widget has been docked somewhere. Beware making changes to any widgets returned as you may modify
          the RenderDoc UI itself.
        
        :param QWidget widget: The widget to query.
        :return: The handle to the parent widget with a matching name, or ``None`` if this widget is either
          not yet parented or is a top-level window.
        :rtype: QWidget
        """
        pass

    def GetProgressBarMaximum(self, pbar: QWidget) -> int: # real signature unknown; restored from __doc__
        """
        GetProgressBarMaximum(pbar)
        
        Get the maximum value of the progress bar's range.
        
        :param QWidget pbar: the progress bar.
        :return: The maximum value of the range.
        :rtype: int
        """
        pass

    def GetProgressBarMinimum(self, pbar: QWidget) -> int: # real signature unknown; restored from __doc__
        """
        GetProgressBarMinimum(pbar)
        
        Get the minimum value of the progress bar's range.
        
        :param QWidget pbar: the progress bar.
        :return: The minimum value of the range.
        :rtype: int
        """
        pass

    def GetProgressBarValue(self, pbar: QWidget) -> int: # real signature unknown; restored from __doc__
        """
        GetProgressBarValue(pbar)
        
        Get the progress bar's current value.
        
        :param QWidget pbar: the progress bar.
        :return: The current value of the progress bar.
        :rtype: int
        """
        pass

    def GetSpinboxValue(self, spinbox: QWidget) -> float: # real signature unknown; restored from __doc__
        """
        GetSpinboxValue(spinbox)
        
        Return the current value of a spinbox widget. If another type of widget is passed
        ``0.0`` will be returned.
        
        :param QWidget spinbox: The widget to query.
        :return: The current  value of the spinbox.
        :rtype: float
        """
        pass

    def GetWidgetName(self, widget: QWidget) -> str: # real signature unknown; restored from __doc__
        """
        GetWidgetName(widget)
        
        Return the internal name of a widget, as set my :meth:`SetWidgetName`.
        
        :param QWidget widget: The widget to query.
        :return: The widget's internal name, which may be an empty string if no name has been set.
        :rtype: str
        """
        pass

    def GetWidgetText(self, widget: QWidget) -> str: # real signature unknown; restored from __doc__
        """
        GetWidgetText(widget)
        
        Return the current text of a widget. See :meth:`SetWidgetText`.
        
        :param QWidget widget: The widget to query.
        :return: The widget's current text, which may be an empty string if no valid text is available.
        :rtype: str
        """
        pass

    def GetWidgetType(self, widget: QWidget) -> str: # real signature unknown; restored from __doc__
        """
        GetWidgetType(widget)
        
        Return the type of the widget as a string. This type is the Qt type name so this
        should only be used for debugging as the name may change even if for the same type of widget.
        
        :param QWidget widget: The widget to query.
        :return: The widget's type name.
        :rtype: str
        """
        pass

    def GetWidgetWindowingData(self, widget: QWidget) -> WindowingData: # real signature unknown; restored from __doc__
        """
        GetWidgetWindowingData(widget)
        
        Return the opaque pointer of windowing data suitable for passing to
        :meth:`~renderdoc.ReplayController.CreateOutput` or other functions that expect windowing data.
        
        If the widget is not a output rendering widget created with :meth:`CreateOutputRenderingWidget` this
        function will fail and return an invalid set of windowing data.
        
        It's important to note that the windowing data is not valid forever, so this function should be
        called as close to where you call :meth:`~renderdoc.ReplayController.CreateOutput` as possible.
        Also don't fetch windowing data unless you are going to create an output, because this function will
        cause the widget to go into an undefined state unless an output is created to render onto it.
        
        .. note::
          This function must be called on the main UI thread.
        
        :param QWidget widget: The widget to create windowing data for.
        :return: The windowing data.
        :rtype: renderdoc.WindowingData
        """
        pass

    def InsertWidget(self, parent: QWidget, index: int, child: QWidget): # real signature unknown; restored from __doc__
        """
        InsertWidget(parent, index, child)
        
        Insert a child widget at the specified index in an ordered layout (either horizontal
        or vertical). If the parent is not an ordered layout nothing will happen and the widget will not be
        added anywhere.
        
        :param QWidget parent: The parent grid layout widget.
        :param int index: The index to insert the widget at. If this index is out of bounds it will be
          clamped, so that negative indices will be equivalent to index 0 and all indices above the number
          of children will append the widget
        :param QWidget child: The child widget to add.
        """
        pass

    def InvokeOntoUIThread(self, callback: InvokeCallback): # real signature unknown; restored from __doc__
        """
        InvokeOntoUIThread(callback)
        
        Invoke a callback on the UI thread. All widget accesses must come from the UI thread,
        so if work has been done on the render thread then this function can be used to asynchronously and
        safely go back to the UI thread.
        
        This function is safe to call on the UI thread, but it will synchronously call the callback
        immediately before returning.
        
        .. note::
          No parameters are provided to the callback, it is assumed that the callback will maintain its own
          context as needed.
        
        :param InvokeCallback callback: The callback to invoke on the UI thread.
          Callback function signature must match :func:`InvokeCallback`.
        """
        pass

    def IsWidgetChecked(self, checkableWidget: QWidget) -> bool: # real signature unknown; restored from __doc__
        """
        IsWidgetChecked(checkableWidget)
        
        Return the current checked-state of a widget. See :meth:`SetWidgetChecked`. If another
        type of widget is passed other than a checkbox or radio box or group box ``False`` will be returned.
        
        :param QWidget checkableWidget: The widget to query.
        :return: ``True`` if the widget is currently checked.
        :rtype: bool
        """
        pass

    def IsWidgetEnabled(self, widget: QWidget) -> bool: # real signature unknown; restored from __doc__
        """
        IsWidgetEnabled(widget)
        
        Return the current enabled-state of a widget. See :meth:`SetWidgetEnabled`.
        
        :param QWidget widget: The widget to query.
        :return: ``True`` if the widget is currently enabled.
        :rtype: bool
        """
        pass

    def IsWidgetVisible(self, widget: QWidget) -> bool: # real signature unknown; restored from __doc__
        """
        IsWidgetVisible(widget)
        
        Return the current visibility of a widget. See :meth:`SetWidgetVisible`.
        
        This query is recursive - a widget could be individually visible, but if it is under a parent which
        is invisible then this widget will be returned as invisible.
        
        :param QWidget widget: The widget to query.
        :return: ``True`` if the widget is currently visible.
        :rtype: bool
        """
        pass

    def ResetProgressBar(self, pbar: QWidget): # real signature unknown; restored from __doc__
        """
        ResetProgressBar(pbar)
        
        Reset a progress bar widget.
        
        Rewinds the progress bar's indicator and hides the indicator's label (theme dependent). If you want
        to keep the label visible, call :meth:`SetProgressBarValue(0)` instead. The minimum and maximum values
        are not changed.
        
        :param QWidget pbar: the progress bar.
        """
        pass

    def SelectComboOption(self, combo: QWidget, option: str): # real signature unknown; restored from __doc__
        """
        SelectComboOption(combo, option)
        
        Select the current option in a drop-down combo box. If another type of widget or
        an unknown option is passed, nothing will happen.
        
        :param QWidget combo: The combo box.
        :param str option: The option to select.
        """
        pass

    def SetComboOptions(self, combo: QWidget, options: List[str]): # real signature unknown; restored from __doc__
        """
        SetComboOptions(combo, options)
        
        Set the pre-defined options in a drop-down combo box. If another type of widget is
        passed nothing will happen.
        
        :param QWidget combo: The combo box.
        :param List[str] options: The new options for the combo box.
        """
        pass

    def SetLabelImage(self, widget: QWidget, data: bytes, width: int, height: int, alpha: bool): # real signature unknown; restored from __doc__
        """
        SetLabelImage(widget, data, width, height, alpha)
        
        Set an image for a label widget. If the widget isn't a label, this call has no effect.
        
        The label will be resized to a fixed size to display the image at 100% scale. Any text in the label
        will not be displayed, but passing an empty image will revert the label back to being text-based.
        
        The data must be in RGB(A) format with the first byte of each texel being R.
        
        :param QWidget widget: The widget to set the picture for.
        :param bytes data: The image data itself, tightly packed.
        :param int width: The width of the image in pixels.
        :param int height: The height of the image in pixels.
        :param bool alpha: ``True`` if the image data contains an alpha channel.
        """
        pass

    def SetProgressBarRange(self, pbar: QWidget, minimum: int, maximum: int): # real signature unknown; restored from __doc__
        """
        SetProgressBarRange(pbar, minimum, maximum)
        
        Set a progress bar's minimum and maximum values.
        
        If maximum is smaller than minimum, minimum is set as the maximum, too. If the current value falls
        outside the new range, the progress bar is reset. Use range (0, 0) to set the progress bar to
        indeterminated state (the progress cannot be estimated or is not being calculated).
        
        :param QWidget pbar: the progress bar.
        :param int minimum: the minimum value.
        :param int maximum: the maximum value.
        """
        pass

    def SetProgressBarValue(self, pbar: QWidget, value: int): # real signature unknown; restored from __doc__
        """
        SetProgressBarValue(pbar, value)
        
        Set the progress bar's current value.
        
        Attempting to change the current value outside the minimum and maximum range does not affect
        the current value.
        
        :param QWidget pbar: the progress bar.
        :param int value: the new current value.
        """
        pass

    def SetSpinboxBounds(self, spinbox: QWidget, minVal: float, maxVal: float): # real signature unknown; restored from __doc__
        """
        SetSpinboxBounds(spinbox, minVal, maxVal)
        
        Set the minimum and maximum values allowed in the spinbox. If another type of widget
        is passed nothing will happen.
        
        :param QWidget spinbox: The spinbox.
        :param float minVal: The minimum value allowed for the spinbox to reach. Lower values entered will
          be clamped to this.
        :param float maxVal: The maximum value allowed for the spinbox to reach. Higher values entered will
          be clamped to this.
        """
        pass

    def SetSpinboxValue(self, spinbox: QWidget, value: float): # real signature unknown; restored from __doc__
        """
        SetSpinboxValue(spinbox, value)
        
        Set the value contained in a spinbox. If another type of widget is passed nothing will
        happen.
        
        :param QWidget spinbox: The spinbox.
        :param float value: The value for the spinbox, which will be clamped by the current bounds.
        """
        pass

    def SetWidgetBackgroundColor(self, widget: QWidget, red: float, green: float, blue: float): # real signature unknown; restored from __doc__
        """
        SetWidgetBackgroundColor(widget, red, green, blue)
        
        Set the default backkground color for a rendering widget. This background color is
        used when no output is currently configured, e.g. when a capture is closed.
        
        For all other widget types this has no effect.
        
        To disable the background color pass negative values for the components, this will cause a default
        checkerboard to be rendered instead. This is the default behaviour when a widget is created.
        
        :param QWidget widget: The widget to set the background color of.
        :param float red: The red component of the color, in the range ``0.0 - 1.0``.
        :param float green: The green component of the color, in the range ``0.0 - 1.0``.
        :param float blue: The blue component of the color, in the range ``0.0 - 1.0``.
        """
        pass

    def SetWidgetChecked(self, checkableWidget: QWidget, checked: bool): # real signature unknown; restored from __doc__
        """
        SetWidgetChecked(checkableWidget, checked)
        
        Set whether the widget is checked or not. This only affects checkboxes and radio
        boxes and group box. If another type of widget is passed nothing will happen.
        
        :param QWidget checkableWidget: The widget to check or uncheck.
        :param bool checked: ``True`` if the widget should be checked.
        """
        pass

    def SetWidgetEnabled(self, widget: QWidget, enabled: bool): # real signature unknown; restored from __doc__
        """
        SetWidgetEnabled(widget, enabled)
        
        Set whether the widget is enabled or not. This generally only affects interactive
        widgets and not fixed widgets, interactive widgets become read-only while still displaying the same
        data.
        
        .. note::
          Disabled widgets can still be modified programmatically, they are only disabled for the user.
        
        :param QWidget widget: The widget to enable or disable.
        :param bool enabled: ``True`` if the widget should be enabled.
        """
        pass

    def SetWidgetFont(self, widget: QWidget, font: str, fontSize: int, bold: bool, italic: bool): # real signature unknown; restored from __doc__
        """
        SetWidgetFont(widget, font, fontSize, bold, italic)
        
        Change the font properties of a widget.
        
        :param QWidget widget: The widget to change font of.
        :param str font: The new font family to use, or an empty string to leave the font family the same.
        :param int fontSize: The new font point size to use, or 0 to leave the size the same.
        :param bool bold: ``True`` if the font should be bold.
        :param bool italic: ``True`` if the font should be italic.
        """
        pass

    def SetWidgetName(self, widget: QWidget, name: str): # real signature unknown; restored from __doc__
        """
        SetWidgetName(widget, name)
        
        Set the internal name of a widget. This is not displayed anywhere but can be used by
        :meth:`FindChildByName` to locate a widget within a hierarchy.
        
        .. note::
          Names are optional and only for your use. Nothing prevents from you from setting duplicate names,
          but this makes searches by name ambiguous.
        
        :param QWidget widget: The widget to set an internal name for.
        :param str name: The internal name to set for the widget.
        """
        pass

    def SetWidgetReplayOutput(self, widget: QWidget, output: ReplayOutput): # real signature unknown; restored from __doc__
        """
        SetWidgetReplayOutput(widget, output)
        
        Set the current output for a widget. This only affects output rendering widgets. If
        another type of widget is passed nothing will happen.
        
        Passing ``None`` as the output will reset the widget and make it display the default background
        until another output is set.
        
        When a capture is closed and all outputs are destroyed, the widget will automatically unset the
        output so there is no need to do that manually.
        
        :param QWidget widget: The widget to set the output for.
        :param renderdoc.ReplayOutput output: The new output to set, or ``None`` to unset any previous
          output.
        """
        pass

    def SetWidgetText(self, widget: QWidget, text: str): # real signature unknown; restored from __doc__
        """
        SetWidgetText(widget, text)
        
        Set the 'text' of a widget. How this manifests depends on the type of the widget, for
        example a text-box or label will set the text directly. For a checkbox or radio button this will
        add text next to it.
        
        :param QWidget widget: The widget to set text for.
        :param str text: The text to set for the widget.
        """
        pass

    def SetWidgetVisible(self, widget: QWidget, visible: bool): # real signature unknown; restored from __doc__
        """
        SetWidgetVisible(widget, visible)
        
        Set whether the widget is visible or not. An invisible widget maintains its position
        in the hierarchy but is not visible and cannot be interacted with in any way.
        
        :param QWidget widget: The widget to show or hide.
        :param bool visible: ``True`` if the widget should be made visible (shown).
        """
        pass

    def ShowWidgetAsDialog(self, widget: QWidget) -> bool: # real signature unknown; restored from __doc__
        """
        ShowWidgetAsDialog(widget)
        
        Show a top-level widget as a blocking modal dialog. This is most useful to prompt the
        user for some specific information.
        
        The dialog is only closed when the user closes the window explicitly or if you call
        :meth:`CloseCurrentDialog` in a widget callback, e.g. upon a button press.
        
        :param QWidget widget: The top-level widget to show as a dialog.
        :return: Whether the dialog was closed successfully, via :meth:`CloseCurrentDialog`.
        :rtype: bool
        """
        pass

    def UpdateProgressBarValue(self, pbar: QWidget, delta: int): # real signature unknown; restored from __doc__
        """
        UpdateProgressBarValue(pbar, delta)
        
        Set the progress bar's current value relative to the existing value.
        
        :param QWidget pbar: the progress bar.
        :param int delta: the relative value to update the current value.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD501315D0>, \'__hash__\': <slot wrapper \'__hash__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'InvokeOntoUIThread\': <method \'InvokeOntoUIThread\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateToplevelWidget\': <method \'CreateToplevelWidget\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CloseToplevelWidget\': <method \'CloseToplevelWidget\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetWidgetName\': <method \'SetWidgetName\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetWidgetName\': <method \'GetWidgetName\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetWidgetType\': <method \'GetWidgetType\' of \'qrenderdoc.MiniQtHelper\' objects>, \'FindChildByName\': <method \'FindChildByName\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetParent\': <method \'GetParent\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetNumChildren\': <method \'GetNumChildren\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetChild\': <method \'GetChild\' of \'qrenderdoc.MiniQtHelper\' objects>, \'DestroyWidget\': <method \'DestroyWidget\' of \'qrenderdoc.MiniQtHelper\' objects>, \'ShowWidgetAsDialog\': <method \'ShowWidgetAsDialog\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CloseCurrentDialog\': <method \'CloseCurrentDialog\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateHorizontalContainer\': <method \'CreateHorizontalContainer\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateVerticalContainer\': <method \'CreateVerticalContainer\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateGridContainer\': <method \'CreateGridContainer\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateSpacer\': <method \'CreateSpacer\' of \'qrenderdoc.MiniQtHelper\' objects>, \'ClearContainedWidgets\': <method \'ClearContainedWidgets\' of \'qrenderdoc.MiniQtHelper\' objects>, \'AddGridWidget\': <method \'AddGridWidget\' of \'qrenderdoc.MiniQtHelper\' objects>, \'AddWidget\': <method \'AddWidget\' of \'qrenderdoc.MiniQtHelper\' objects>, \'InsertWidget\': <method \'InsertWidget\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetWidgetText\': <method \'SetWidgetText\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetWidgetText\': <method \'GetWidgetText\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetWidgetFont\': <method \'SetWidgetFont\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetWidgetEnabled\': <method \'SetWidgetEnabled\' of \'qrenderdoc.MiniQtHelper\' objects>, \'IsWidgetEnabled\': <method \'IsWidgetEnabled\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetWidgetVisible\': <method \'SetWidgetVisible\' of \'qrenderdoc.MiniQtHelper\' objects>, \'IsWidgetVisible\': <method \'IsWidgetVisible\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateGroupBox\': <method \'CreateGroupBox\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateButton\': <method \'CreateButton\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateLabel\': <method \'CreateLabel\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetLabelImage\': <method \'SetLabelImage\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateOutputRenderingWidget\': <method \'CreateOutputRenderingWidget\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetWidgetWindowingData\': <method \'GetWidgetWindowingData\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetWidgetReplayOutput\': <method \'SetWidgetReplayOutput\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetWidgetBackgroundColor\': <method \'SetWidgetBackgroundColor\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateCheckbox\': <method \'CreateCheckbox\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateRadiobox\': <method \'CreateRadiobox\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetWidgetChecked\': <method \'SetWidgetChecked\' of \'qrenderdoc.MiniQtHelper\' objects>, \'IsWidgetChecked\': <method \'IsWidgetChecked\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateSpinbox\': <method \'CreateSpinbox\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetSpinboxBounds\': <method \'SetSpinboxBounds\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetSpinboxValue\': <method \'SetSpinboxValue\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetSpinboxValue\': <method \'GetSpinboxValue\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateTextBox\': <method \'CreateTextBox\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateComboBox\': <method \'CreateComboBox\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetComboOptions\': <method \'SetComboOptions\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetComboCount\': <method \'GetComboCount\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SelectComboOption\': <method \'SelectComboOption\' of \'qrenderdoc.MiniQtHelper\' objects>, \'CreateProgressBar\': <method \'CreateProgressBar\' of \'qrenderdoc.MiniQtHelper\' objects>, \'ResetProgressBar\': <method \'ResetProgressBar\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetProgressBarValue\': <method \'SetProgressBarValue\' of \'qrenderdoc.MiniQtHelper\' objects>, \'UpdateProgressBarValue\': <method \'UpdateProgressBarValue\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetProgressBarValue\': <method \'GetProgressBarValue\' of \'qrenderdoc.MiniQtHelper\' objects>, \'SetProgressBarRange\': <method \'SetProgressBarRange\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetProgressBarMinimum\': <method \'GetProgressBarMinimum\' of \'qrenderdoc.MiniQtHelper\' objects>, \'GetProgressBarMaximum\': <method \'GetProgressBarMaximum\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__dict__\': <attribute \'__dict__\' of \'qrenderdoc.MiniQtHelper\' objects>, \'__doc__\': "\\nPython can have direct access to Qt via PySide2, but this is not always available in\\nall RenderDoc builds. To aid extensions to manipulate widgets in a simple but portable fashion this\\nhelper exposes a small subset of Qt via RenderDoc\'s python bindings.\\n\\nThe intention is not to allow fully flexible building of Qt panels, but to allow access to some\\nbasic UI building tools for simple data input and display which can be used on any RenderDoc build.\\n\\nThis manager is retrieved by calling :meth:`ExtensionManager.GetMiniQtHelper`.\\n\\n.. note::\\n  The widget handles returned are PySide2 widgets where that is available, so this can be used to\\n  make a basic UI and optionally customise it further with PySide2 when possible.\\n\\n.. function:: WidgetCallback(context, widget, text)\\n\\n  Not a member function - the signature for any ``WidgetCallback`` callbacks.\\n\\n  Callback for widgets can be registered at creation time, the text field is optional and may be\\n  blank depending on the event, but the context and widget are always valid.\\n\\n  :param CaptureContext context: The current capture context.\\n  :param QWidget widget: The widget sending the callback.\\n  :param str text: Additional data for the call, such as the current or selected text.\\n\\n.. function:: InvokeCallback(context, widget, text)\\n\\n  Not a member function - the signature for any ``InvokeCallback`` callbacks.\\n\\n  Callback for invoking onto the UI thread from another thread (in particular the replay thread).\\n  Takes no parameters as the callback is expected to store its own state.\\n\\n"})'


