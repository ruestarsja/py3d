


class Rotation3D():

    """
    A rotation or orientation in 3-dimensional space.

    theta: rotation in the x-z plane in degrees +x -> +z
    phi: rotation orthogonal to the x-z plane in degrees theta -> +y
    """

    def __init__(self, theta:int|float, phi:int|float):
        self.__theta = theta
        self.__validate_theta()

        self.__phi = phi
        self.__validate_phi()
    
    def __validate_theta(self) -> None:
        if type(self.__theta) not in (int, float):
            msg = "Rotation3D.__theta must be an int or float."
            raise TypeError(msg)
        
        return
    
    def __validate_phi(self) -> None:
        if type(self.__phi) not in (int, float):
            msg = "Rotation3D.__phi must be an int or float."
            raise TypeError(msg)
        return

    def get_theta(self) -> int|float:
        return self.__theta
    def get_phi(self) -> int|float:
        return self.__phi
    
    def set_theta(self, theta:int|float) -> None:
        self.__theta = theta
        self.__validate_theta()
        return
    
    def set_phi(self, phi:int|float) -> None:
        self.__phi = phi
        self.__validate_phi()
        return
    
    def rot_theta(self, delta_theta:int|float) -> None:
        if type(delta_theta) not in (int, float):
            msg = "Rotation3D.rot_theta argument 'delta_theta' must be an int or float."
            raise TypeError(msg)
        self.__theta += delta_theta
        return
    
    def rot_phi(self, delta_phi:int|float) -> None:
        if type(delta_phi) not in (int, float):
            msg = "Rotation3D.rot_phi argument 'delta_phi' must be an int or float."
            raise TypeError(msg)
        self.__phi += delta_phi
        return
    
    def __neg__(self):
        # returns a Rotation3D object
        return self.__class__(-self.get_theta(), -self.get_phi())

    def __add__(self, other):
        # returns a Rotation3D object
        if type(other) is not self.__class__:
            msg = f"Cannot add object of type {type(other)} from object of type {type(self)}."
            raise TypeError(msg)
        return self.__class__(self.get_theta() + other.get_theta(), self.get_phi() + other.get_phi())

    def __sub__(self, other):
        # returns a Rotation3D object
        if type(other) is not self.__class__:
            msg = f"Cannot subtract object of type {type(other)} from object of type {type(self)}."
            raise TypeError(msg)
        return self + -other
