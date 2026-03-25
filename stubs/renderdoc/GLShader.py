# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceId import ResourceId
from .ShaderReflection import ShaderReflection
from .ShaderStage import ShaderStage

class GLShader(): # skipped bases: <class 'SwigPyObject'>
    """ Describes an OpenGL shader stage. """
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
    def programResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the program bound to this stage.

:type: ResourceId

"""
        pass

    @programResourceId.setter
    def programResourceId(self, value: ResourceId):
        pass

    @property
    def reflection(self) -> ShaderReflection:
        """
The reflection data for this shader.

:type: ShaderReflection

"""
        pass

    @reflection.setter
    def reflection(self, value: ShaderReflection):
        pass

    @property
    def shaderResourceId(self) -> ResourceId:
        """
The :class:`ResourceId` of the shader object itself.

:type: ResourceId

"""
        pass

    @shaderResourceId.setter
    def shaderResourceId(self, value: ResourceId):
        pass

    @property
    def stage(self) -> ShaderStage:
        """
A :class:`ShaderStage` identifying which stage this shader is bound to.

:type: ShaderStage

"""
        pass

    @stage.setter
    def stage(self, value: ShaderStage):
        pass

    @property
    def subroutines(self) -> List[int]:
        """
A list of integers with the subroutine values.

:type: List[int]

"""
        pass

    @subroutines.setter
    def subroutines(self, value: List[int]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD5520E5C0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLShader' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLShader' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLShader' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLShader' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLShader' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLShader' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLShader' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLShader' objects>, 'subroutines': <attribute 'subroutines' of 'renderdoc.GLShader' objects>, 'reflection': <attribute 'reflection' of 'renderdoc.GLShader' objects>, 'shaderResourceId': <attribute 'shaderResourceId' of 'renderdoc.GLShader' objects>, 'programResourceId': <attribute 'programResourceId' of 'renderdoc.GLShader' objects>, 'stage': <attribute 'stage' of 'renderdoc.GLShader' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLShader' objects>, '__doc__': 'Describes an OpenGL shader stage.'})"


