from ._ResourceId import ResourceId
from ._SDObjectData import SDObjectData
from ._SDType import SDType

from typing import overload

class SDObject():
    # Original docstring
    """
    Defines a single structured object. Structured objects are defined recursively and one
    object can either be a basic type (integer, float, etc), an array, or a struct. Arrays and structs
    are defined similarly.
    
    Each object owns its children and they will be deleted when it is deleted. You can use
    :meth:`Duplicate` to make a deep copy of an object.
    """
    
    
    @overload
    def __init__(self):
        """
        Construct a new default-initialised SDObject.
        """
        pass
    
    @overload
    def __init__(self, name: str, typeName: str):
        """
        Construct a new SDObject using provided values.
        """
        pass
    
    
    def __init__(self): pass
    
    
    def Duplicate(self) -> 'SDObject':
        """
        :return: A new deep copy of this object, which the caller owns.
        :rtype: SDObject
        """
        pass
    
    
    def HasEqualValue(self, obj: 'SDObject') -> bool:
        """
        Checks if the given object has the same value as this one. This equality is defined
        recursively through children.
        
        :param SDObject obj: The object to compare against
        :return: A boolean indicating if the object is equal to this one.
        :rtype: bool
        """
        pass
    
    
    def AddChild(self, child: 'SDObject'):
        """
        Add a new child object.
        
        :param SDObject child: The new child to add
        """
        pass
    
    
    def FindChild(self, childName: str) -> 'SDObject':
        """
        Find a child object by a given name. If no matching child is found, ``None`` is
        returned.
        
        :param str childName: The name to search for.
        :return: A reference to the child object if found, or ``None`` if not.
        :rtype: SDObject
        """
        pass
    
    
    def FindChildRecursively(self, childName: str) -> 'SDObject':
        """
        Find a child object by a given name recursively. If no matching child is found,
        ``None`` is returned.
        
        The order of the search is not guaranteed, so care should be taken when the name may not be unique.
        
        :param str childName: The name to search for.
        :return: A reference to the child object if found, or ``None`` if not.
        :rtype: SDObject
        """
        pass
    
    
    def CreateChildByKeyPath(self, keyPath: str) -> 'SDObject':
        """
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
    
    
    def FindChildByKeyPath(self, keyPath: str) -> 'SDObject':
        """
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
    
    
    def EraseChildByKeyPath(self, keyPath: str):
        """
        Delete a child object by a key path. All children of the resulting path will be deleted
        as well. If no such path exists, nothing will be changed.
        
        If any path element is not unique in any child the behaviour is undefined, so objects should only be
        manipulated by key path exclusively or not at all.
        
        :param str keyPath: The key path to search for and delete.
        """
        pass
    
    
    def GetChild(self, index: int) -> 'SDObject':
        """
        Find a child object by a given index. If the index is out of bounds, ``None`` is
        returned.
        
        :param int index: The index to look up.
        :return: A reference to the child object if valid, or ``None`` if not.
        :rtype: SDObject
        """
        pass
    
    
    def GetParent(self) -> 'SDObject':
        """
        Get the parent of this object. If this object has no parent, ``None`` is returned.
        
        :return: A reference to the parent object if valid, or ``None`` if not.
        :rtype: SDObject
        """
        pass
    
    
    def RemoveChild(self, index: int):
        """
        Delete the child object at an index. If the index is out of bounds, nothing happens.
        
        :param int index: The index to remove.
        """
        pass
    
    
    def DeleteChildren(self):
        """
        Delete all child objects.
        """
        pass
    
    
    def NumChildren(self) -> int:
        """
        Get the number of child objects.
        
        :return: The number of children this object contains.
        :rtype: int
        """
        pass
    
    
    def AsBool(self) -> bool:
        """
        Interprets the object as a ``bool`` and returns its value.
        Invalid if the object is not actually a ``bool``.
        
        :return: The interpreted bool value.
        :rtype: bool
        """
        pass
    
    
    def AsResourceId(self) -> ResourceId:
        """
        Interprets the object as a :class:`ResourceId` and returns its value.
        Invalid if the object is not actually a :class:`ResourceId`.
        
        :return: The interpreted ID.
        :rtype: ResourceId
        """
        pass
    
    
    def AsInt(self) -> int:
        """
        Interprets the object as an integer and returns its value.
        Invalid if the object is not actually an integer.
        
        :return: The interpreted integer.
        :rtype: int
        """
        pass
    
    
    def AsFloat(self) -> float:
        """
        Interprets the object as a floating point number and returns its value.
        Invalid if the object is not actually a floating point number.
        
        :return: The interpreted float.
        :rtype: float
        """
        pass
    
    
    def AsString(self) -> str:
        """
        Interprets the object as a string and returns its value.
        Invalid if the object is not actually a string.
        
        :return: The interpreted string.
        :rtype: str
        """
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
    def type(self) -> SDType:
        """
        The :class:`SDType` of this object.
        
        :type: SDType
        """
        pass
    
    @type.setter
    def type(self, value: SDType):
        pass
    
