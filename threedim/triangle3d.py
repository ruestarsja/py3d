from threedim.point3d import Point3D

import pygame as pg


class Triangle3D():

    """
    A triangle in 3-dimensional space.
    """
    
    def __init__(
        self,
        vertices:tuple[
            Point3D|tuple[int|float, int|float, int|float],
            Point3D|tuple[int|float, int|float, int|float],
            Point3D|tuple[int|float, int|float, int|float]
        ]
    ):
        self.__vertices = vertices
        self.__validate_vertices()
    
    def __validate_vertices(self) -> None:
        vertices = list()
        msg = "Triangle3D.__vertices must be a 3-tuple of Point3D objects or 3-tuples of ints or floats."
        if type(self.__vertices) is not tuple:
            raise TypeError(msg)
        for pos in self.__vertices:
            if type(pos) is not Point3D:
                if type(pos) is not tuple:
                    raise ValueError(msg)
                elif len(pos) != 3:
                    raise ValueError(msg)
                else:
                    try:
                        pos = Point3D(*pos)
                    except TypeError:
                        raise ValueError(msg)
            vertices.append(pos)
        self.__vertices = vertices
        return


    def get_vertices(self):
        return self.__vertices

    def __eq__(self, other):
        if type(other) is not self.__class__:
            return False
        self_vertices, other_vertices = self.get_vertices(), other.get_vertices()
        other_used = []
        for vertex in self_vertices:
            if other_vertices.count(vertex) > other_used.count(vertex):
                other_used.append(vertex)
            else:
                return False
        return True
