# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId
from .SDObjectData import SDObjectData
from .SDType import SDType

class SDObject(): # skipped bases: <class 'SwigPyObject'>
    """
    Defines a single structured object. Structured objects are defined recursively and one
    object can either be a basic type (integer, float, etc), an array, or a struct. Arrays and structs
    are defined similarly.
    
    Each object owns its children and they will be deleted when it is deleted. You can use
    :meth:`Duplicate` to make a deep copy of an object.
    """
    def AddChild(self, child: SDObject): # real signature unknown; restored from __doc__
        """
        AddChild(child)
        
        Add a new child object.
        
        :param SDObject child: The new child to add
        """
        pass

    def AsBool(self) -> bool: # real signature unknown; restored from __doc__
        """
        AsBool()
        
        Interprets the object as a ``bool`` and returns its value.
        Invalid if the object is not actually a ``bool``.
        
        :return: The interpreted bool value.
        :rtype: bool
        """
        pass

    def AsFloat(self) -> float: # real signature unknown; restored from __doc__
        """
        AsFloat()
        
        Interprets the object as a floating point number and returns its value.
        Invalid if the object is not actually a floating point number.
        
        :return: The interpreted float.
        :rtype: float
        """
        pass

    def AsInt(self) -> int: # real signature unknown; restored from __doc__
        """
        AsInt()
        
        Interprets the object as an integer and returns its value.
        Invalid if the object is not actually an integer.
        
        :return: The interpreted integer.
        :rtype: int
        """
        pass

    def AsResourceId(self) -> ResourceId: # real signature unknown; restored from __doc__
        """
        AsResourceId()
        
        Interprets the object as a :class:`ResourceId` and returns its value.
        Invalid if the object is not actually a :class:`ResourceId`.
        
        :return: The interpreted ID.
        :rtype: ResourceId
        """
        pass

    def AsString(self) -> str: # real signature unknown; restored from __doc__
        """
        AsString()
        
        Interprets the object as a string and returns its value.
        Invalid if the object is not actually a string.
        
        :return: The interpreted string.
        :rtype: str
        """
        pass

    def CreateChildByKeyPath(self, keyPath: str) -> 'SDObject': # real signature unknown; restored from __doc__
        """
        CreateChildByKeyPath(keyPath)
        
        Create a child object by a key path. Children will be created as necessary to ensure
        that the key path exists, but if they already exist then the existing object will be returned.
        
        Key paths are dotted recursive references, e.g. ``foo.bar`` is the member ``bar`` in parent ``foo``.
        
        Arrays are represented by simple numeric entries e.g. ``foo.0.bar``, ``foo.1.bar``.
        
        Empty entries are ignored so ``foo..bar`` and ``foo.bar`` refer to the same object.
        
        Key paths must not be empty and must not begin with a dot.
        
        If any path element is not unique in any child the behaviour is undefined, so objects should only be
        manipulated by key path exclusively or not at all.
        
        :param str keyPath: The key path to search for and return.
        :return: A reference to the object at the relative key path
        :rtype: SDObject
        """
        pass

    def DeleteChildren(self): # real signature unknown; restored from __doc__
        """
        DeleteChildren()
        
        Delete all child objects.
        """
        pass

    def Duplicate(self) -> 'SDObject': # real signature unknown; restored from __doc__
        """
        Duplicate()
        
        
        :return: A new deep copy of this object, which the caller owns.
        :rtype: SDObject
        """
        pass

    def EraseChildByKeyPath(self, keyPath: str): # real signature unknown; restored from __doc__
        """
        EraseChildByKeyPath(keyPath)
        
        Delete a child object by a key path. All children of the resulting path will be deleted
        as well. If no such path exists, nothing will be changed.
        
        If any path element is not unique in any child the behaviour is undefined, so objects should only be
        manipulated by key path exclusively or not at all.
        
        :param str keyPath: The key path to search for and delete.
        """
        pass

    def FindChild(self, childName: str) -> 'SDObject': # real signature unknown; restored from __doc__
        """
        FindChild(childName)
        
        Find a child object by a given name. If no matching child is found, ``None`` is
        returned.
        
        :param str childName: The name to search for.
        :return: A reference to the child object if found, or ``None`` if not.
        :rtype: SDObject
        """
        pass

    def FindChildByKeyPath(self, keyPath: str) -> 'SDObject': # real signature unknown; restored from __doc__
        """
        FindChildByKeyPath(keyPath)
        
        Find if a child object if it exists by a key path. Children will not be created
        if any element of the path doesn't exist and instead ``None`` will be returned.
        
        Key paths are dotted recursive references, e.g. ``foo.bar`` is the member ``bar`` in parent ``foo``.
        
        Arrays are represented by simple numeric entries e.g. ``foo.0.bar``, ``foo.1.bar``.
        
        Empty entries are ignored so ``foo..bar`` and ``foo.bar`` refer to the same object.
        
        Key paths must not be empty and must not begin with a dot.
        
        If any path element is not unique in any child the behaviour is undefined, so objects should only be
        manipulated by key path exclusively or not at all.
        
        :param str keyPath: The key path to search for and return.
        :return: Whether or not a child exists at the given key path
        :rtype: SDObject
        """
        pass

    def FindChildRecursively(self, childName: str) -> 'SDObject': # real signature unknown; restored from __doc__
        """
        FindChildRecursively(childName)
        
        Find a child object by a given name recursively. If no matching child is found,
        ``None`` is returned.
        
        The order of the search is not guaranteed, so care should be taken when the name may not be unique.
        
        :param str childName: The name to search for.
        :return: A reference to the child object if found, or ``None`` if not.
        :rtype: SDObject
        """
        pass

    def GetChild(self, index: int) -> 'SDObject': # real signature unknown; restored from __doc__
        """
        GetChild(index)
        
        Find a child object by a given index. If the index is out of bounds, ``None`` is
        returned.
        
        :param int index: The index to look up.
        :return: A reference to the child object if valid, or ``None`` if not.
        :rtype: SDObject
        """
        pass

    def GetParent(self) -> 'SDObject': # real signature unknown; restored from __doc__
        """
        GetParent()
        
        Get the parent of this object. If this object has no parent, ``None`` is returned.
        
        :return: A reference to the parent object if valid, or ``None`` if not.
        :rtype: SDObject
        """
        pass

    def HasEqualValue(self, obj: SDObject) -> bool: # real signature unknown; restored from __doc__
        """
        HasEqualValue(obj)
        
        Checks if the given object has the same value as this one. This equality is defined
        recursively through children.
        
        :param SDObject obj: The object to compare against
        :return: A boolean indicating if the object is equal to this one.
        :rtype: bool
        """
        pass

    def NumChildren(self) -> int: # real signature unknown; restored from __doc__
        """
        NumChildren()
        
        Get the number of child objects.
        
        :return: The number of children this object contains.
        :rtype: int
        """
        pass

    def RemoveChild(self, index: int): # real signature unknown; restored from __doc__
        """
        RemoveChild(index)
        
        Delete the child object at an index. If the index is out of bounds, nothing happens.
        
        :param int index: The index to remove.
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

    @property
    def data(self) -> SDObjectData:
        """
The :class:`SDObjectData` with the contents of this object.

:type: SDObjectData

"""
        pass

    @data.setter
    def data(self, value: SDObjectData):
        pass

    @property
    def name(self) -> str:
        """
The name of this object.

:type: str

"""
        pass

    @name.setter
    def name(self, value: str):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self) -> SDType:
        """
The :class:`SDType` of this object.

:type: SDType

"""
        pass

    @type.setter
    def type(self, value: SDType):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551AAC80>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SDObject' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SDObject' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SDObject' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SDObject' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SDObject' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SDObject' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SDObject' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SDObject' objects>, 'Duplicate': <method 'Duplicate' of 'renderdoc.SDObject' objects>, 'HasEqualValue': <method 'HasEqualValue' of 'renderdoc.SDObject' objects>, 'AddChild': <method 'AddChild' of 'renderdoc.SDObject' objects>, 'FindChild': <method 'FindChild' of 'renderdoc.SDObject' objects>, 'FindChildRecursively': <method 'FindChildRecursively' of 'renderdoc.SDObject' objects>, 'CreateChildByKeyPath': <method 'CreateChildByKeyPath' of 'renderdoc.SDObject' objects>, 'FindChildByKeyPath': <method 'FindChildByKeyPath' of 'renderdoc.SDObject' objects>, 'EraseChildByKeyPath': <method 'EraseChildByKeyPath' of 'renderdoc.SDObject' objects>, 'GetChild': <method 'GetChild' of 'renderdoc.SDObject' objects>, 'GetParent': <method 'GetParent' of 'renderdoc.SDObject' objects>, 'RemoveChild': <method 'RemoveChild' of 'renderdoc.SDObject' objects>, 'DeleteChildren': <method 'DeleteChildren' of 'renderdoc.SDObject' objects>, 'NumChildren': <method 'NumChildren' of 'renderdoc.SDObject' objects>, 'AsBool': <method 'AsBool' of 'renderdoc.SDObject' objects>, 'AsResourceId': <method 'AsResourceId' of 'renderdoc.SDObject' objects>, 'AsInt': <method 'AsInt' of 'renderdoc.SDObject' objects>, 'AsFloat': <method 'AsFloat' of 'renderdoc.SDObject' objects>, 'AsString': <method 'AsString' of 'renderdoc.SDObject' objects>, 'name': <attribute 'name' of 'renderdoc.SDObject' objects>, 'data': <attribute 'data' of 'renderdoc.SDObject' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SDObject' objects>, 'type': <attribute 'type' of 'renderdoc.SDObject' objects>, '__doc__': '\\nDefines a single structured object. Structured objects are defined recursively and one\\nobject can either be a basic type (integer, float, etc), an array, or a struct. Arrays and structs\\nare defined similarly.\\n\\nEach object owns its children and they will be deleted when it is deleted. You can use\\n:meth:`Duplicate` to make a deep copy of an object.\\n\\n'})"


