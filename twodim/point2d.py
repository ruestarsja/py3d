from math import sqrt


class Point2D():

    """
    A point in 2-dimensional space.
    """
    
    def __init__(self, x:int|float, y:int|float):
        self.__x = x
        self.__validate_x()

        self.__y = y
        self.__validate_y()
    
    def __validate_x(self):
        if type(self.__x) not in (int, float):
            msg = "Point2D.__x must be an int or float."
            raise TypeError(msg)
        return
    
    def __validate_y(self):
        if type(self.__y) not in (int, float):
            msg = "Point2D.__y must be an int or float."
            raise TypeError(msg)
        return

    def get_pos(self):
        return (self.__x, self.__y)
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def dist(self, other):
        if type(other) is not self.__class__:
            msg = "Point2D.dist argument 'other' must be a Point2D object."
            raise TypeError(msg)
        return sqrt(
                   (self.get_x() - other.get_x())**2
                 + (self.get_y() - other.get_y())**2
               )
    
    def __eq__(self, other) -> bool:
        if type(other) is not self.__class__:
            return False
        if self.get_pos() == other.get_pos():
            return True
        return False

    def __neg__(self):
        # returns Point2D
        return self.__class__(
            -self.get_x(),
            -self.get_y()
        )
    
    def __add__(self, other):
        # returns Point2D
        if type(other) is not self.__class__:
            msg = f"Cannot add object of type {type(self)} and object of type {type(other)}."
            raise TypeError(msg)
        return self.__class__(
            self.get_x() + other.get_x(),
            self.get_y() + other.get_y()
        )
    
    def __sub__(self, other):
        # returns Point2D
        if type(other) is not self.__class__:
            msg = f"Cannot add object of type {type(self)} and object of type{type(other)}."
            raise TypeError(msg)
        return self + -other

    def __mul__(self, other):
        # returns Point2D
        if type(other) not in (int, float):
            raise TypeError(
                f"Cannot multiply object of type {type(self)} and object of type {type(other)}."
            )
        return self.__class__(
            self.get_x() * other,
            self.get_y() * other
        )
