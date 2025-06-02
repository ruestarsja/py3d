from twodim.triangle2d  import Triangle2D
from twodim.point2d     import Point2D

from threedim.threedimspace import ThreeDimSpace
from threedim.camera        import Camera
from threedim.object        import Object

import pygame as pg
import sys
import time
from queue import Queue


class Py3D():

    """
    The pygame application py3d.
    """

    def __init__(
        self,
        dims:tuple[int, int],
        name:str="py3d app",
        max_fps:int|None=None
    ):
        self.__dims = dims
        self.__validate_dims()

        self.__name = name
        self.__validate_name()

        self.__max_fps = max_fps
        self.__validate_max_fps()
        
    def __validate_dims(self) -> None:
        if type(self.__dims) is not tuple:
            raise TypeError(
                "Application.__init__ argument 'dims' must be a 2-tuple."
            )
        else:
            for x in self.__dims:
                if type(x) not in (int, float):
                    raise ValueError(
                        "Application.__init__ argument 'dims' must be a 2-tuple consisting of only"
                        " ints or tuples."
                    )
        return
    
    def __validate_name(self) -> None:
        if type(self.__name) is not str:
            raise TypeError(
                "Application.__init__ argument 'name' must be a str."
            )
        return
    
    def __validate_max_fps(self) -> None:
        if self.__max_fps is not None:
            if type(self.__max_fps) is not int:
                raise TypeError(
                    "Application.__init__ argument 'max_fps' must be a positive int or None."
                )
            elif self.__max_fps <= 0:
                raise ValueError(
                    "Application.__init__ argument 'max_fps' must be a positive int or None."
                )
        return

    def run(self) -> None:
        pg.init()

        self.__make_window()
        self.__mouse_freed = True

        self.__space = ThreeDimSpace()
        self.__faces_to_draw:Queue[Triangle2D] = Queue(maxsize=0)

        self.__camera = Camera((0, 0, 0), (0, 0), 90)
        self.__space.add_camera(self.__camera)
        
        self.__space.add_object(Object("threedim/objects/platonic_octohedron.txt", 1, (5, 0, 0)))

        self.__delta_time = 0
        start_time = time.time()

        for face in self.__camera.project_all(self.__space.get_objects(), self.__window):
            self.__faces_to_draw.put(face)

        self.__running = True
        while self.__running:
            end_time = time.time()
            self.__delta_time = end_time - start_time
            if self.__max_fps:
                time.sleep((1/self.__max_fps) - self.__delta_time)
                self.__delta_time = 1/self.__max_fps
            start_time = time.time()
            self.__update_display()
            self.__handle_events()
            self.__handle_movement()
            if not self.__mouse_freed:
                self.__handle_rotation()
            for face in self.__camera.project_all(self.__space.get_objects(), self.__window):
                self.__faces_to_draw.put(face)

        pg.quit()
        return

    def __make_window(self) -> None:
        self.__window = pg.display.set_mode(self.__dims)
        pg.display.set_caption(self.__name)
        return

    def __update_display(self) -> None:
        self.__window.fill("white")
        while not self.__faces_to_draw.empty():
            self.__faces_to_draw.get().draw_frame(self.__window)
        pg.display.update()
        return

    def __handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.__mouse_freed = not self.__mouse_freed
                    pg.mouse.set_pos(
                        (self.__window.get_width() / 2, self.__window.get_height() / 2)
                    )
                    pg.mouse.set_visible(self.__mouse_freed)
        return

    def __handle_movement(self) -> None:
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.__camera.move_forward(self.__delta_time)
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.__camera.move_backward(self.__delta_time)
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.__camera.move_left(self.__delta_time)
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.__camera.move_right(self.__delta_time)
        if keys[pg.K_SPACE]:
            self.__camera.move_up(self.__delta_time)
        if keys[pg.K_LCTRL]:
            self.__camera.move_down(self.__delta_time)
        if keys[pg.K_j]:
            self.__camera.look_horizontal(-0.1)
        if keys[pg.K_l]:
            self.__camera.look_horizontal(0.1)
        if keys[pg.K_i]:
            self.__camera.look_vertical(-0.1)
        if keys[pg.K_k]:
            self.__camera.look_vertical(0.1)
        return
    
    def __handle_rotation(self) -> None:
        center = Point2D(self.__window.get_width() / 2, self.__window.get_height() / 2)
        mouse_pos = Point2D(*pg.mouse.get_pos())
        delta_pos = mouse_pos - center
        self.__camera.look_horizontal(delta_pos.get_x())
        self.__camera.look_vertical(delta_pos.get_y())
        pg.mouse.set_pos(center.get_pos())


if __name__ == "__main__":
    app = Py3D((1200, 700), "Py3D")
    app.run()
    sys.exit()
