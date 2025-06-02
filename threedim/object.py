from threedim.point3d import Point3D


class Object():

    """
    An object with vertices, edges, and faces in 3-dimensional space.
    """

    def __init__(
        self,
        fname:str,
        scale:int|float,
        center:Point3D|tuple[int|float, int|float, int|float]
    ):

        self.__fname = fname
        self.__validate_fname()

        self.__scale = scale
        self.__validate_scale()
        
        self.__center = center
        self.__validate_center()

        # Calling self.__load() will define:
        #     self.__vertices
        #     self.__edges
        #     self.__faces
        self.__load()
    
    def __validate_fname(self) -> None:
        msg = "Object.__fname must be a str of a path to a text file."
        if type(self.__fname) is not str:
            raise TypeError(msg)
        else:
            try:
                with open(self.__fname, 'r') as fin:
                    pass
            except FileNotFoundError:
                raise ValueError(msg)
        return
    
    def __validate_scale(self) -> None:
        if type(self.__scale) not in (int, float):
            msg = "Object.__scale must be an int or float."
            raise TypeError(msg)
        return
    
    def __validate_center(self) -> None:
        if type(self.__center) is not Point3D:
            msg = "Object.__center must be a Point3D object or a 3-tuple of ints or floats."
            if type(self.__center) is not tuple:
                raise TypeError(msg)
            elif len(self.__center) != 3:
                raise ValueError(msg)
            else:
                try:
                    self.__center = Point3D(*self.__center)
                except ValueError:
                    raise ValueError(msg)
        return
    
    def get_fname(self) -> str:
        return self.__fname
    def get_scale(self) -> int|float:
        return self.__scale
    def get_center(self) -> Point3D:
        return self.__center
    def get_vertices(self) -> set:
        return self.__vertices
    def get_edges(self) -> set:
        return self.__edges
    def get_faces(self) -> set:
        return self.__faces

    def __load(self) -> None:
        self.__vertices = list()
        self.__edges = list()
        self.__faces = list()

        reading_edges = True
        
        with open(self.__fname, 'r') as file:
            try:
                for line in file:
                    line = line.strip()
                    if line == '':
                        reading_edges = False
                    elif reading_edges:
                        x,y,z = line.split(',')
                        point = Point3D(float(x), float(y), float(z))*self.__scale + self.__center
                        if point not in self.__vertices:
                            self.__vertices.append(point)
                    else:
                        i1, i2, i3 = line.split(',')
                        i1, i2, i3 = int(i1), int(i2), int(i3)
                        self.__edges.append(
                            (self.__vertices[i1], self.__vertices[i2])
                        )
                        self.__edges.append(
                            (self.__vertices[i1], self.__vertices[i3])
                        )
                        self.__edges.append(
                            (self.__vertices[i2], self.__vertices[i3])
                        )
                        self.__faces.append(
                            (self.__vertices[i1], self.__vertices[i2], self.__vertices[i3])
                        )
            except:
                msg = (
                    "Object.__fname must be a str of a path to a properly formatted text file, but"
                    " the file was formatted improperly."
                )
                raise IOError(msg)
        return
