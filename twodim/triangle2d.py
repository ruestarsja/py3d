from twodim.point2d import Point2D

import pygame as pg


class Triangle2D():

    """
    A triangle in 2-dimensional space.
    """

    def __init__(
        self,
        vertices:tuple[
            Point2D|tuple[int, int],
            Point2D|tuple[int, int],
            Point2D|tuple[int, int]
        ]
    ):
        self.__vertices = vertices
        self.__validate_vertices()
    
    def __validate_vertices(self):
        vertices = list()
        msg = (
            "Triangle2D.__vertices must be a tuple of Point2D objects or 2-tuples of ints or "
            "floats."
        )
        for pos in self.__vertices:
            if type(pos) is not Point2D:
                try:
                    pos = Point2D(*pos)
                except TypeError:
                    raise TypeError(msg)
            vertices.append(pos)
        self.__vertices = tuple(vertices)


    def get_vertices(self):
        return self.__vertices
    
    def draw_frame(self, surface, color='black'):
        pg.draw.lines(surface, color, True, [point.get_pos() for point in self.get_vertices()])

    def draw_full(self, surface, color='black'):
        pg.draw.polygon(surface, color, [point.get_pos() for point in self.get_vertices()])

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
