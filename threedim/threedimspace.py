from threedim.object import Object
from threedim.camera import Camera


class ThreeDimSpace():

    """
    A right-handed 3-dimensional space.
    """

    def __init__(self):
        self.__objects = []
        self.__cameras = []
    
    def get_objects(self) -> list:
        return self.__objects
    def get_cameras(self) -> list:
        return self.__cameras

    def add_object(self, obj) -> None:
        if type(obj) is not Object:
            msg = "ThreeDimSpace.add_object argument 'obj' must be an Object object."
            raise TypeError(msg)
        self.__objects.append(obj)
        return

    def remove_object(self, obj) -> None:
        if type(obj) is not Object:
            msg = "ThreeDimSpace.remove_object argument 'obj' must be an Object object."
            raise TypeError(msg)
        self.__objects.remove(obj)
        return
    
    def add_camera(self, camera) -> None:
        if type(camera) is not Camera:
            msg = "ThreeDimSpace.add_camera argument 'camera' must be a Camera object."
            raise TypeError(msg)
        self.__cameras.append(camera)
        return
    
    def remove_camera(self, camera) -> None:
        if type(Camera) is not Camera:
            msg = "ThreeDimSpace.remove_camera argument 'camera' must be a Camera object."
            raise TypeError(msg)
        self.__cameras.remove(camera)
        return
