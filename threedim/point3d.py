from math import sqrt


class Point3D():

    """
    A point in 3-dimensional space.
    """
    
    def __init__(self, x:int|float, y:int|float, z:int|float):
        self.__x = x
        self.__validate_x()

        self.__y = y
        self.__validate_y()

        self.__z = z
        self.__validate_z()
    
    def __repr__(self) -> str:
        return f"threedim.point3d.Point3d({self.__x}, {self.__y}, {self.__z})"

    def __validate_x(self) -> None:
        if type(self.__x) not in (int, float):
            msg = "Point3D.__x must be an int or float."
            raise TypeError(msg)
        return

    def __validate_y(self) -> None:
        if type(self.__y) not in (int, float):
            msg = "Point3D.__y must be an int or float."
            raise TypeError(msg)
        return
    
    def __validate_z(self) -> None:
        if type(self.__z) not in (int, float):
            msg = "Point3D.__z must be an int or float."
            raise TypeError(msg)
        return

    def get_pos(self) -> tuple[int|float, int|float, int|float]:
        return (self.__x, self.__y, self.__z)

    def dist(self, other) -> int|float:
        if type(other) is not self.__class__:
            msg = "Point3D.dist argument 'other' must be a Point3D object."
            raise TypeError(msg)
        return sqrt(
                   (self.get_x() - other.get_x())**2
                 + (self.get_y() - other.get_y())**2
                 + (self.get_z() - other.get_z())**2
               )
    
    def get_x(self) -> int|float:
        return self.__x
    def get_y(self) -> int|float:
        return self.__y
    def get_z(self) -> int|float:
        return self.__z
    
    def set_x(self, x:int|float) -> None:
        self.__x = x
        self.__validate_x()
        return
    def set_y(self, y:int|float) -> None:
        self.__y = y
        self.__validate_y()
        return
    def set_z(self, z:int|float) -> None:
        self.__z = z
        self.__validate_z()
        return
    
    def move_x(self, delta_x:int|float) -> None:
        if type(delta_x) not in (int, float):
            msg = "Point3D.move_x argument 'delta_x' must be an int or float."
            raise TypeError(msg)
        self.__x += delta_x
        return
    
    def move_y(self, delta_y:int|float) -> None:
        if type(delta_y) not in (int, float):
            msg = "Point3D.move_y argument 'delta_y' must be an int or float."
            raise TypeError(msg)
        self.__y += delta_y
        return

    def move_z(self, delta_z:int|float) -> None:
        if type(delta_z) not in (int, float):
            msg = "Point3D.move_z argument 'delta_z' must be an int or float."
            raise TypeError(msg)
        self.__z += delta_z
        return

    def __eq__(self, other) -> bool:
        if type(other) is not self.__class__:
            return False
        if self.get_pos() == other.get_pos():
            return True
        return False

    def __neg__(self):
        # returns Point3D
        return self.__class__(
            -self.get_x(),
            -self.get_y(),
            -self.get_z()
        )
    
    def __add__(self, other):
        # returns Point3D
        if type(other) is not self.__class__:
            msg = f"Cannot add object of type {type(self)} and object of type {type(other)}."
            raise TypeError(msg)
        return self.__class__(
            self.get_x() + other.get_x(),
            self.get_y() + other.get_y(),
            self.get_z() + other.get_z()
        )
    
    def __sub__(self, other):
        # returns Point3D
        if type(other) is not self.__class__:
            msg = f"Cannot add object of type {type(self)} and object of type{type(other)}."
            raise TypeError(msg)
        return self + -other

    def __mul__(self, other):
        # returns Point3D
        if type(other) not in (int, float):
            raise TypeError(
                f"Cannot multiply object of type {type(self)} and object of type {type(other)}."
            )
        return self.__class__(
            self.get_x() * other,
            self.get_y() * other,
            self.get_z() * other
        )
