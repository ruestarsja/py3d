from twodim.point2d import Point2D


class Line2D():

    """
    A line in 2-dimensional space.
    """

    def __init__(
        self,
        start:Point2D|tuple[int, int],
        end:Point2D|tuple[int, int]
    ):
        self.__start = start
        self.__validate_start()
        
        self.__end = end
        self.__validate_end()

    def __validate_start(self) -> None:
        if type(self.__start) is not Point2D:
            msg = "Line2D.__start must be a Point2D object or a 2-tuple of ints or floats."
            if type(self.__start) is not tuple:
                raise TypeError(msg)
            elif len(self.__start) != 2:
                raise ValueError(msg)
            else:
                try:
                    self.__start = Point2D(*self.__start)
                except ValueError:
                    raise ValueError(msg)
        return
    
    def __validate_end(self) -> None:
        if type(self.__end) is not Point2D:
            msg = "Line2D.__end must be a Point2D object or a 2-tuple of ints or floats."
            if type(self.__end) is not tuple:
                raise TypeError(msg)
            elif len(self.__end) != 2:
                raise ValueError(msg)
            else:
                try:
                    self.__end = Point2D(*self.__end)
                except ValueError:
                    raise ValueError(msg)
        return

    def get_ends(self):
        return (self.__start, self.__end)
    def get_start(self):
        return self.__start
    def get_end(self):
        return self.__end

    def get_len(self):
        return self.get_start().dist(self.get_end())

    def __eq__(self, other):
        if type(other) is not self.__class__:
            return False
        if (self.get_ends() == other.get_ends()) or \
           (self.get_ends() == (other.get_end(), other.get_start())):
            return True
        return False
