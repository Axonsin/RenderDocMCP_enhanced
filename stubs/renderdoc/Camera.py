# encoding: utf-8
# module renderdoc
# from C:\Users\13908\Desktop\works\renderdoc_pythonmodules\x64\Development\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .FloatVector import FloatVector

class Camera(): # skipped bases: <class 'SwigPyObject'>
    """
    A handle to a camera controller, used for user interaction and controlling a view of a
    3D scene.
    """
    def GetForward(self) -> FloatVector: # real signature unknown; restored from __doc__
        """
        GetForward()
        
        Retrieves the forward vector of the camera, in the positive Z direction.
        
        :return: The forward vector of the camera. W is set to 1
        :rtype: FloatVector
        """
        pass

    def GetPosition(self) -> FloatVector: # real signature unknown; restored from __doc__
        """
        GetPosition()
        
        Retrieves the position of the camera
        
        :return: The position vector of the camera. W is set to 1
        :rtype: FloatVector
        """
        pass

    def GetRight(self) -> FloatVector: # real signature unknown; restored from __doc__
        """
        GetRight()
        
        Retrieves the right vector of the camera, in the positive X direction.
        
        :return: The right vector of the camera. W is set to 1
        :rtype: FloatVector
        """
        pass

    def GetUp(self) -> FloatVector: # real signature unknown; restored from __doc__
        """
        GetUp()
        
        Retrieves the up vector of the camera, in the positive Y direction.
        
        :return: The up vector of the camera. W is set to 1
        :rtype: FloatVector
        """
        pass

    def ResetArcball(self): # real signature unknown; restored from __doc__
        """
        ResetArcball()
        
        Reset the arcball to defaults.
        """
        pass

    def RotateArcball(self, ax: float, ay: float, bx: float, by: float): # real signature unknown; restored from __doc__
        """
        RotateArcball(ax, ay, bx, by)
        
        Rotates the arcball based on relative window co-ordinates.
        
        The co-ordinates are in pixels and represent the old/new co-ordinates of the mouse cursor over the
        drag.
        
        :param float ax: The X co-ordinate of the previous mouse position.
        :param float ay: The Y co-ordinate of the previous mouse position.
        :param float bx: The X co-ordinate of the new mouse position.
        :param float by: The Y co-ordinate of the new mouse position.
        """
        pass

    def SetArcballDistance(self, dist: float): # real signature unknown; restored from __doc__
        """
        SetArcballDistance(dist)
        
        Sets the distance in units the arcball camera sits away from the lookat position.
        
        :param float dist: The distance of the camera from the lookat position.
        """
        pass

    def SetFPSRotation(self, x: float, y: float, z: float): # real signature unknown; restored from __doc__
        """
        SetFPSRotation(x, y, z)
        
        Sets the rotation for an FPS camera.
        
        It is invalid to call this function for arcball cameras.
        
        :param float x: The rotation around the X axis (pitch).
        :param float y: The rotation around the Y axis (yaw).
        :param float z: The rotation around the Z axis (roll).
        """
        pass

    def SetNearFar(self, n: float, f: float): # real signature unknown; restored from __doc__
        """
        SetNearFar(n, f)
        
        Sets the near and far plane for the camera's display.
        
        The default value is ``0.1 - 100000.0`` if these are not set explicitly.
        
        :param float n: The near plane.
        :param float f: The far plane.
        """
        pass

    def SetPosition(self, x: float, y: float, z: float): # real signature unknown; restored from __doc__
        """
        SetPosition(x, y, z)
        
        Sets the position for the camera, either arcball or FPS.
        
        For arcball cameras, this sets the lookat position at the centre of the arcball.
        
        For FPS look cameras, this sets the position of the camera in space.
        
        :param float x: The X co-ordinate of the position.
        :param float y: The Y co-ordinate of the position.
        :param float z: The Z co-ordinate of the position.
        """
        pass

    def Shutdown(self): # real signature unknown; restored from __doc__
        """
        Shutdown()
        
        Closes the camera handle.
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFD551C2630>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.Camera' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.Camera' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.Camera' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.Camera' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.Camera' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.Camera' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.Camera' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.Camera' objects>, 'Shutdown': <method 'Shutdown' of 'renderdoc.Camera' objects>, 'SetNearFar': <method 'SetNearFar' of 'renderdoc.Camera' objects>, 'SetPosition': <method 'SetPosition' of 'renderdoc.Camera' objects>, 'SetFPSRotation': <method 'SetFPSRotation' of 'renderdoc.Camera' objects>, 'SetArcballDistance': <method 'SetArcballDistance' of 'renderdoc.Camera' objects>, 'ResetArcball': <method 'ResetArcball' of 'renderdoc.Camera' objects>, 'RotateArcball': <method 'RotateArcball' of 'renderdoc.Camera' objects>, 'GetPosition': <method 'GetPosition' of 'renderdoc.Camera' objects>, 'GetForward': <method 'GetForward' of 'renderdoc.Camera' objects>, 'GetRight': <method 'GetRight' of 'renderdoc.Camera' objects>, 'GetUp': <method 'GetUp' of 'renderdoc.Camera' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.Camera' objects>, '__doc__': '\\nA handle to a camera controller, used for user interaction and controlling a view of a\\n3D scene.\\n\\n'})"


