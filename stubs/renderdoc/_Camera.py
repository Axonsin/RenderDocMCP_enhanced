from ._FloatVector import FloatVector

class Camera():
    # Original docstring
    """
    A handle to a camera controller, used for user interaction and controlling a view of a
    3D scene.
    """
    
    
    
    def Shutdown(self):
        """
        Closes the camera handle.
        """
        pass
    
    
    def SetNearFar(self, n: float, f: float):
        """
        Sets the near and far plane for the camera's display.
        
        The default value is ``0.1 - 100000.0`` if these are not set explicitly.
        
        :param float n: The near plane.
        :param float f: The far plane.
        """
        pass
    
    
    def SetPosition(self, x: float, y: float, z: float):
        """
        Sets the position for the camera, either arcball or FPS.
        
        For arcball cameras, this sets the lookat position at the centre of the arcball.
        
        For FPS look cameras, this sets the position of the camera in space.
        
        :param float x: The X co-ordinate of the position.
        :param float y: The Y co-ordinate of the position.
        :param float z: The Z co-ordinate of the position.
        """
        pass
    
    
    def SetFPSRotation(self, x: float, y: float, z: float):
        """
        Sets the rotation for an FPS camera.
        
        It is invalid to call this function for arcball cameras.
        
        :param float x: The rotation around the X axis (pitch).
        :param float y: The rotation around the Y axis (yaw).
        :param float z: The rotation around the Z axis (roll).
        """
        pass
    
    
    def SetArcballDistance(self, dist: float):
        """
        Sets the distance in units the arcball camera sits away from the lookat position.
        
        :param float dist: The distance of the camera from the lookat position.
        """
        pass
    
    
    def ResetArcball(self):
        """
        Reset the arcball to defaults.
        """
        pass
    
    
    def RotateArcball(self, ax: float, ay: float, bx: float, by: float):
        """
        Rotates the arcball based on relative window co-ordinates.
        
        The co-ordinates are in pixels and represent the old/new co-ordinates of the mouse cursor over the
        drag.
        
        :param float ax: The X co-ordinate of the previous mouse position.
        :param float ay: The Y co-ordinate of the previous mouse position.
        :param float bx: The X co-ordinate of the new mouse position.
        :param float by: The Y co-ordinate of the new mouse position.
        """
        pass
    
    
    def GetPosition(self) -> FloatVector:
        """
        Retrieves the position of the camera
        
        :return: The position vector of the camera. W is set to 1
        :rtype: FloatVector
        """
        pass
    
    
    def GetForward(self) -> FloatVector:
        """
        Retrieves the forward vector of the camera, in the positive Z direction.
        
        :return: The forward vector of the camera. W is set to 1
        :rtype: FloatVector
        """
        pass
    
    
    def GetRight(self) -> FloatVector:
        """
        Retrieves the right vector of the camera, in the positive X direction.
        
        :return: The right vector of the camera. W is set to 1
        :rtype: FloatVector
        """
        pass
    
    
    def GetUp(self) -> FloatVector:
        """
        Retrieves the up vector of the camera, in the positive Y direction.
        
        :return: The up vector of the camera. W is set to 1
        :rtype: FloatVector
        """
        pass
    
