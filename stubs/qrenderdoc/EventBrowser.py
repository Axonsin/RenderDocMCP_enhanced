# encoding: utf-8
# module qrenderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from renderdoc.ActionDescription import ActionDescription

from renderdoc.APIEvent import APIEvent

class EventBrowser(): # skipped bases: <class 'SwigPyObject'>
    """
    The event browser window.
    
    This window is retrieved by calling :meth:`CaptureContext.GetEventBrowser`.
    
    .. function:: EventFilterCallback(context, filter, params, eventId, chunk, action, name)
    
      Not a member function - the signature for any ``EventFilterCallback`` callbacks.
    
      Called for each event in a capture when performing filtering in the Event Browser. The associated
      :func:`FilterParseCallback` will be called first to parse the parameters, and is available for caching
      or syntax checking. The same filter name and params string will be passed to this function.
    
      :param CaptureContext context: The current capture context.
      :param str filter: The name of the filter function.
      :param str params: The parameters to the filter function.
      :param int eventId: The event's :data:`eventId <renderdoc.APIEvent.eventId>`.
      :param renderdoc.SDChunk chunk: The structured data chunk for this event.
      :param renderdoc.ActionDescription action: The action that contains this event. If the event is
        the action itself then the event ID will be equal.
      :param str name: The name of the event as shown in the event browser, for string-based filtering.
      :return: Whether or not this event matches the filter
      :rtype: bool
    
    .. function:: FilterParseCallback(context, filter, params)
    
      Not a member function - the signature for any ``FilterParseCallback`` callbacks.
    
      Called once when the filter changes, to allow parsing any any data caching, as well as reporting
      of errors in the filter usage.
    
      :param CaptureContext context: The current capture context.
      :param str filter: The name of the filter function.
      :param str params: The parameters to the filter function.
      :return: An empty string if the parse succeeded, otherwise any error messages to be displayed to
        the user, such as syntax or other errors.
      :rtype: str
    
    .. function:: AutoCompleteCallback(context, filter, params)
    
      Not a member function - the signature for any ``AutoCompleteCallback`` callbacks.
    
      Called when autocompletion is triggered inside a filter. The params passed are any previous
      text inside the filter's parameter list up to where the cursor is. The callback should return a
      list of identifiers used for auto-completion.
    
      The list does not have to be pre-filtered for matches to the :paramref:`params`, that is provided
      to allow different autocompletion at different stages (e.g. if there are no parameters, you can
      autocomplete a property, if a property is already present you can autocomplete valid values for
      it)
    
      :param CaptureContext context: The current capture context.
      :param str filter: The name of the filter function.
      :param str params: The previous parameter text to the filter function.
      :return: A list of strings giving identifiers to autocomplete, or an empty list of there are no
        such identifiers to prompt.
      :rtype: List[str]
    """
    def GetActionForEID(self, eventId: int) -> ActionDescription: # real signature unknown; restored from __doc__
        """
        GetActionForEID(eventId)
        
        Uses the existing caching in the event browser to return a
        :class:`~renderdoc.ActionDescription` for a specified EID. This action may not be the exact EID
        specified, but it will be the action that the EID is associated with. I.e. if you specify the EID for
        a state setting event the next action will be returned.
        
        If no capture is loaded or the EID doesn't correspond to a known event, ``None`` will be returned.
        
        :param int eventId: The EID to look up.
        :return: The action containing the EID, or ``None`` if no such EID exists.
        :rtype: renderdoc.ActionDescription
        """
        pass

    def GetAPIEventForEID(self, eventId: int) -> APIEvent: # real signature unknown; restored from __doc__
        """
        GetAPIEventForEID(eventId)
        
        Uses the existing caching in the event browser to return a :class:`~renderdoc.APIEvent`
        for a specified EID.
        
        If no capture is loaded or the EID doesn't correspond to a known event, an empty struct will be
        returned.
        
        :param int eventId: The EID to look up.
        :return: The event corresponding to the EID, or an empty struct if no such EID exists.
        :rtype: renderdoc.APIEvent
        """
        pass

    def GetCurrentFilterText(self) -> str: # real signature unknown; restored from __doc__
        """
        GetCurrentFilterText()
        
        Returns the current filter text, whether temporary or a saved filter.
        
        :return: The current filter text.
        :rtype: str
        """
        pass

    def GetEventName(self, eventId: int) -> str: # real signature unknown; restored from __doc__
        """
        GetEventName(eventId)
        
        Returns the formatted name of an event according to the current settings, whether
        that be a custom name or an auto-generated name with/without parameter names.
        
        If no capture is loaded or the EID doesn't correspond to a known event, an empty string will be
        returned.
        
        :param int eventId: The EID to look up.
        :return: The formatted name of the specified event, or ``None`` if no such EID exists.
        :rtype: str
        """
        pass

    def GetHighlightedAnnotation(self) -> str: # real signature unknown; restored from __doc__
        """
        GetHighlightedAnnotation()
        
        Returns the current annotation key path as being highlighted in the annotation column.
        
        :return: The current annotation path.
        :rtype: str
        """
        pass

    def IsAPIEventVisible(self, eventId: int) -> bool: # real signature unknown; restored from __doc__
        """
        IsAPIEventVisible(eventId)
        
        Determines if a given EID is visible with the current filters applied to the event
        browser.
        
        If no capture is loaded or the EID doesn't correspond to a known event, ``False`` will be returned.
        
        :param int eventId: The EID to look up.
        :return: Whether or not the event is currently visible (passing the filters).
        :rtype: bool
        """
        pass

    def RegisterEventFilterFunction(self, name: str, description: str, filter: EventFilterCallback, parser: FilterParseCallback, completer: AutoCompleteCallback) -> bool: # real signature unknown; restored from __doc__
        """
        RegisterEventFilterFunction(name, description, filter, parser, completer)
        
        Registers a new event browser filter function.
        
        Filter functions are available as $name() so long as they don't shadow an existing function. The
        filter callback will be called for each event to filter.
        
        The parser callback will be called once when a filter is first specified or the parameters change.
        Note that a filter can be used multiple times in a filter expression! For this reason the parser
        may be called multiple times and the filter callback takes the parameters string. If any expensive
        work is done then the parameters can be used as a cache key to cache any data once per filter
        expression.
        
        :param str name: The name of the filter function.
        :param str description: The description of the filter function. This should explain the available
          parameters (if applicable) and what the filter does. It will be used for documenting to users
          what each filter means.
        :param EventFilterCallback filter: The callback to call for each candidate event to perform
          filtering.
          Callback function signature must match :func:`EventFilterCallback`.
        :param FilterParseCallback parser: The callback to call when the parsing the parameters and checking
          for any errors. This can be ``None`` if no pre-parsing is required.
          Callback function signature must match :func:`FilterParseCallback`.
        :param AutoCompleteCallback completer: The callback to call when trying to provide autocomplete
          suggestions. This can be ``None`` if no completion is desired/applicable.
          Callback function signature must match :func:`AutoCompleteCallback`.
        :return: Whether or not the registration was successful.
        :rtype: bool
        """
        pass

    def SetAnnotationColumnVisible(self, show: bool): # real signature unknown; restored from __doc__
        """
        SetAnnotationColumnVisible(show)
        
        Sets whether or not the annotation column is visible.
        
        :param bool show: If the duration column should be shown.
        """
        pass

    def SetCurrentFilterText(self, text: str): # real signature unknown; restored from __doc__
        """
        SetCurrentFilterText(text)
        
        Sets the current filter text. This will not modify any saved filter but will modify
        the scratch filter. The filter is applied immediately.
        
        :param str text: The filter text.
        """
        pass

    def SetDurationColumnVisible(self, show: bool): # real signature unknown; restored from __doc__
        """
        SetDurationColumnVisible(show)
        
        Sets whether or not the duration column is visible.
        
        :param bool show: If the duration column should be shown.
        """
        pass

    def SetEmptyRegionsVisible(self, show: bool): # real signature unknown; restored from __doc__
        """
        SetEmptyRegionsVisible(show)
        
        Sets whether or not marker regions which have no visible actions.
        
        :param bool show: Whether or not empty regions after filtering will be shown.
        """
        pass

    def SetHighlightedAnnotation(self, annotationPath: str): # real signature unknown; restored from __doc__
        """
        SetHighlightedAnnotation(annotationPath)
        
        Sets the current annotation key path. This will not display the annotation column if
        it is not already visible.
        
        :param str annotationPath: The new annotation path.
        """
        pass

    def SetShowAllParameters(self, show: bool): # real signature unknown; restored from __doc__
        """
        SetShowAllParameters(show)
        
        Sets whether or not all parameters are shown in the events. By default only
        the most significant parameters are shown.
        
        .. note::
          If custom action names are used this will not have an effect for any such actions. See
          :meth:`SetUseCustomActionNames`.
        
        :param bool show: Whether or not parameter names will be shown.
        """
        pass

    def SetShowParameterNames(self, show: bool): # real signature unknown; restored from __doc__
        """
        SetShowParameterNames(show)
        
        Sets whether or not parameter names are shown in the events. If disabled, only the
        value is shown and the parameter is implicit.
        
        .. note::
          If custom action names are used this will not have an effect for any such actions. See
          :meth:`SetUseCustomActionNames`.
        
        :param bool show: Whether or not parameter names will be shown.
        """
        pass

    def SetUseCustomActionNames(self, use: bool): # real signature unknown; restored from __doc__
        """
        SetUseCustomActionNames(use)
        
        Sets whether or not custom action names are used. Certain actions such as indirect
        actions it is useful to show a custom action name which contains the actual indirect parameters
        instead of the 'raw' parameters.
        
        :param bool use: Whether or not custom action names will be used.
        """
        pass

    def UnregisterEventFilterFunction(self, name: str) -> bool: # real signature unknown; restored from __doc__
        """
        UnregisterEventFilterFunction(name)
        
        Unregisters an event browser filter function that was previously registered.
        
        :param str name: The name of the filter function.
        
        :return: Whether or not the unregistration was successful.
        :rtype: bool
        """
        pass

    def UpdateDurationColumn(self): # real signature unknown; restored from __doc__
        """
        UpdateDurationColumn()
        
        Updates the duration column if the selected time unit changes.
        """
        pass

    def Widget(self) -> QWidget: # real signature unknown; restored from __doc__
        """
        Widget()
        
        Retrieves the PySide2 QWidget for this :class:`EventBrowser` if PySide2 is available, or otherwise
        returns a unique opaque pointer that can be passed back to any RenderDoc functions expecting a
        QWidget.
        
        :return: Return the widget handle, either a PySide2 handle or an opaque handle.
        :rtype: QWidget
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


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD50135540>, \'__hash__\': <slot wrapper \'__hash__\' of \'qrenderdoc.EventBrowser\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'qrenderdoc.EventBrowser\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'qrenderdoc.EventBrowser\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'qrenderdoc.EventBrowser\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'qrenderdoc.EventBrowser\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'qrenderdoc.EventBrowser\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'qrenderdoc.EventBrowser\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'qrenderdoc.EventBrowser\' objects>, \'Widget\': <method \'Widget\' of \'qrenderdoc.EventBrowser\' objects>, \'UpdateDurationColumn\': <method \'UpdateDurationColumn\' of \'qrenderdoc.EventBrowser\' objects>, \'GetAPIEventForEID\': <method \'GetAPIEventForEID\' of \'qrenderdoc.EventBrowser\' objects>, \'GetActionForEID\': <method \'GetActionForEID\' of \'qrenderdoc.EventBrowser\' objects>, \'GetEventName\': <method \'GetEventName\' of \'qrenderdoc.EventBrowser\' objects>, \'IsAPIEventVisible\': <method \'IsAPIEventVisible\' of \'qrenderdoc.EventBrowser\' objects>, \'RegisterEventFilterFunction\': <method \'RegisterEventFilterFunction\' of \'qrenderdoc.EventBrowser\' objects>, \'UnregisterEventFilterFunction\': <method \'UnregisterEventFilterFunction\' of \'qrenderdoc.EventBrowser\' objects>, \'SetCurrentFilterText\': <method \'SetCurrentFilterText\' of \'qrenderdoc.EventBrowser\' objects>, \'GetCurrentFilterText\': <method \'GetCurrentFilterText\' of \'qrenderdoc.EventBrowser\' objects>, \'SetUseCustomActionNames\': <method \'SetUseCustomActionNames\' of \'qrenderdoc.EventBrowser\' objects>, \'SetShowParameterNames\': <method \'SetShowParameterNames\' of \'qrenderdoc.EventBrowser\' objects>, \'SetShowAllParameters\': <method \'SetShowAllParameters\' of \'qrenderdoc.EventBrowser\' objects>, \'SetEmptyRegionsVisible\': <method \'SetEmptyRegionsVisible\' of \'qrenderdoc.EventBrowser\' objects>, \'SetHighlightedAnnotation\': <method \'SetHighlightedAnnotation\' of \'qrenderdoc.EventBrowser\' objects>, \'GetHighlightedAnnotation\': <method \'GetHighlightedAnnotation\' of \'qrenderdoc.EventBrowser\' objects>, \'SetDurationColumnVisible\': <method \'SetDurationColumnVisible\' of \'qrenderdoc.EventBrowser\' objects>, \'SetAnnotationColumnVisible\': <method \'SetAnnotationColumnVisible\' of \'qrenderdoc.EventBrowser\' objects>, \'__dict__\': <attribute \'__dict__\' of \'qrenderdoc.EventBrowser\' objects>, \'__doc__\': "\\nThe event browser window.\\n\\nThis window is retrieved by calling :meth:`CaptureContext.GetEventBrowser`.\\n\\n.. function:: EventFilterCallback(context, filter, params, eventId, chunk, action, name)\\n\\n  Not a member function - the signature for any ``EventFilterCallback`` callbacks.\\n\\n  Called for each event in a capture when performing filtering in the Event Browser. The associated\\n  :func:`FilterParseCallback` will be called first to parse the parameters, and is available for caching\\n  or syntax checking. The same filter name and params string will be passed to this function.\\n\\n  :param CaptureContext context: The current capture context.\\n  :param str filter: The name of the filter function.\\n  :param str params: The parameters to the filter function.\\n  :param int eventId: The event\'s :data:`eventId <renderdoc.APIEvent.eventId>`.\\n  :param renderdoc.SDChunk chunk: The structured data chunk for this event.\\n  :param renderdoc.ActionDescription action: The action that contains this event. If the event is\\n    the action itself then the event ID will be equal.\\n  :param str name: The name of the event as shown in the event browser, for string-based filtering.\\n  :return: Whether or not this event matches the filter\\n  :rtype: bool\\n\\n.. function:: FilterParseCallback(context, filter, params)\\n\\n  Not a member function - the signature for any ``FilterParseCallback`` callbacks.\\n\\n  Called once when the filter changes, to allow parsing any any data caching, as well as reporting\\n  of errors in the filter usage.\\n\\n  :param CaptureContext context: The current capture context.\\n  :param str filter: The name of the filter function.\\n  :param str params: The parameters to the filter function.\\n  :return: An empty string if the parse succeeded, otherwise any error messages to be displayed to\\n    the user, such as syntax or other errors.\\n  :rtype: str\\n\\n.. function:: AutoCompleteCallback(context, filter, params)\\n\\n  Not a member function - the signature for any ``AutoCompleteCallback`` callbacks.\\n\\n  Called when autocompletion is triggered inside a filter. The params passed are any previous\\n  text inside the filter\'s parameter list up to where the cursor is. The callback should return a\\n  list of identifiers used for auto-completion.\\n\\n  The list does not have to be pre-filtered for matches to the :paramref:`params`, that is provided\\n  to allow different autocompletion at different stages (e.g. if there are no parameters, you can\\n  autocomplete a property, if a property is already present you can autocomplete valid values for\\n  it)\\n\\n  :param CaptureContext context: The current capture context.\\n  :param str filter: The name of the filter function.\\n  :param str params: The previous parameter text to the filter function.\\n  :return: A list of strings giving identifiers to autocomplete, or an empty list of there are no\\n    such identifiers to prompt.\\n  :rtype: List[str]\\n\\n"})'


