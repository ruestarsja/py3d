from twodim.point2d     import Point2D
from twodim.triangle2d  import Triangle2D

from threedim.point3d       import Point3D
from threedim.rotation3d    import Rotation3D
from threedim.object        import Object
from threedim.triangle3d    import Triangle3D

from math import sqrt, degrees, radians, sin, cos, tan, atan
import pygame as pg



class Camera():

    """
    A camera object in 3-dimensional space.

    pos (Point3D|tuple(int|float, int|float, int|float)): the 3-dimensional
        coordinates of the camera.
    rot (Rotation3D|tuple(int|float, int|float)): (theta, phi) where theta
        is rotation in the x-z plane in degrees +x -> +z and phi is
        rotation orthogonal to the x-z plane in degrees theta -> +y.
    up (Rotation3D|tuple(int|float, int|float)): (theta, phi) of the "up"
        direction of the camera. this should always be 90 degrees from rot.
    fov (int|float): the horizontal field of view in degrees.
    mov_vel (int|float): the movement velocity in units/sec.
    """

    def __init__(
        self,
        pos:Point3D|tuple[int|float, int|float, int|float],
        rot:Rotation3D|tuple[int|float, int|float],
        # up:Rotation3D|tuple[int|float, int|float],
        fov:int|float,
        mov_vel:int|float=1.0,
        rot_vel:int|float=0.2
    ):
        self.__pos = pos
        self.__validate_pos()

        self.__rot = rot
        self.__validate_rot()

        # self.__up = up
        # self.__validate_up()

        self.__fov = fov
        self.__validate_fov()

        self.__mov_vel = mov_vel
        self.__validate_mov_vel()

        self.__rot_vel = rot_vel
        self.__validate_rot_vel()
    

    def __validate_pos(self) -> None:
        if type(self.__pos) is not Point3D:
            msg = "Camera.__pos must be a Point3D object or a 3-tuple of ints or floats."
            if type(self.__pos) is not tuple:
                raise TypeError(msg)
            elif len(self.__pos) != 3:
                raise ValueError(msg)
            else:
                try:
                    self.__pos = Point3D(*self.__pos)
                except ValueError:
                    raise ValueError(msg)
        return


    def __validate_rot(self) -> None:
        if type(self.__rot) is not Rotation3D:
            msg = "Camera.__rot must be a Rotation3D object or a 2-tuple of ints or floats."
            if type(self.__rot) is not tuple:
                raise TypeError(msg)
            elif len(self.__rot) != 2:
                raise ValueError(msg)
            else:
                try:
                    self.__rot = Rotation3D(*self.__rot)
                except ValueError:
                    raise ValueError(msg)
        return


    def __validate_up(self) -> None:
        if type(self.__uo) is not Rotation3D:
            msg = "Camera.__up must be a Rotation3D object or a 2-tuple of ints or floats."
            if type(self.__up) is not tuple:
                raise TypeError(msg)
            elif len(self.__up) != 2:
                raise ValueError(msg)
            else:
                try:
                    self.__up = Rotation3D(*self.__up)
                except ValueError:
                    raise ValueError(msg)
        return


    def __validate_fov(self) -> None:
        if type(self.__fov) not in (int, float):
            msg = "Camera.__fov must be an int or float."
            raise TypeError(msg)
        return
    

    def __validate_mov_vel(self) -> None:
        if type(self.__mov_vel) not in (int, float):
            msg = "Camera.__mov_vel must be an int or float."
            raise TypeError(msg)
        return


    def __validate_rot_vel(self) -> None:
        if type(self.__rot_vel) not in (int, float):
            msg = "Camera.__rot_vel must be an int or float."
            raise TypeError(msg)
        return


    def get_pos(self) -> Point3D:
        return self.__pos
    def get_x(self) -> int|float:
        return self.__pos.get_x()
    def get_y(self) -> int|float:
        return self.__pos.get_y()
    def get_z(self) -> int|float:
        return self.__pos.get_z()
    def get_rot(self) -> Rotation3D:
        return self.__rot
    def get_theta(self) -> int|float:
        return self.__rot.get_theta()
    def get_phi(self) -> int|float:
        return self.__rot.get_phi()
    def get_up(self) -> Rotation3D:
        return self.__up
    
    def get_fov(self) -> int|float:
        return self.__fov
    def get_mov_vel(self) -> int|float:
        return self.__mov_vel


    def set_pos(self, pos:Point3D|tuple[int|float, int|float, int|float]) -> None:
        self.__pos = pos
        self.__validate_pos()
        return


    def set_x(self, x:int|float) -> None:
        self.__pos.set_x(x)
        return


    def set_y(self, y:int|float) -> None:
        self.__pos.set_y(y)
        return


    def set_z(self, z:int|float) -> None:
        self.__pos.set_z(z)
        return
    

    def set_rot(self, rot:tuple[int|float, int|float]) -> None:
        self.__rot = rot
        self.__validate_rot()
        return


    def set_theta(self, theta:int|float) -> None:
        self.__rot.set_theta(theta)
        return
    

    def set_phi(self, phi:int|float) -> None:
        self.__rot.set_phi(phi)
        return


    def set_fov(self, fov:int|float) -> None:
        self.__fov = fov
        self.__validate_fov()
        return
    

    def set_mov_vel(self, mov_vel:int|float) -> None:
        self.__mov_vel = mov_vel
        self.__validate_mov_vel()
        return


    def __move_x(self, delta_x:int|float) -> None:
        self.__pos.move_x(delta_x)
        return
    

    def __move_y(self, delta_y:int|float) -> None:
        self.__pos.move_y(delta_y)
        return


    def __move_z(self, delta_z:int|float) -> None:
        self.__pos.move_z(delta_z)
        return


    def __rot_theta(self, delta_theta:int|float) -> None:
        self.__rot.rot_theta(delta_theta)
        return


    def __rot_phi(self, delta_phi:int|float) -> None:
        self.__rot.rot_phi(delta_phi)
        return


    def move_forward(self, delta_time:int|float) -> None:
        if type(delta_time) not in (int, float):
            msg = "Camera.move_forward argument 'delta_time' must be an int or float."
            raise TypeError(msg)

        theta = self.__rot.get_theta()
        delta_x = self.__mov_vel * delta_time * cos(radians(theta))
        delta_z = self.__mov_vel * delta_time * sin(radians(theta))
        self.__move_x(delta_x)
        self.__move_z(delta_z)
        return


    def move_backward(self, delta_time:int|float) -> None:
        if type(delta_time) not in (int, float):
            msg = "Camera.move_backward argument 'delta_time' must be an int or float."
            raise TypeError(msg)

        theta = self.__rot.get_theta()
        delta_x = -1 * self.__mov_vel * delta_time * cos(radians(theta))
        delta_z = -1 * self.__mov_vel * delta_time * sin(radians(theta))
        self.__move_x(delta_x)
        self.__move_z(delta_z)
        return


    def move_left(self, delta_time:int|float) -> None:
        if type(delta_time) not in (int, float):
            msg = "Camera.move_left argument 'delta_time' must be an int or float."
            raise TypeError(msg)

        theta = self.__rot.get_theta()
        delta_x = self.__mov_vel * delta_time * sin(radians(theta))
        delta_z = -1 * self.__mov_vel * delta_time * cos(radians(theta))
        self.__move_x(delta_x)
        self.__move_z(delta_z)
        return


    def move_right(self, delta_time:int|float) -> None:
        if type(delta_time) not in (int, float):
            msg = "Camera.move_right argument 'delta_time' must be an int or float."
            raise TypeError(msg)

        theta = self.__rot.get_theta()
        delta_x = -1 * self.__mov_vel * delta_time * sin(radians(theta))
        delta_z = self.__mov_vel * delta_time * cos(radians(theta))
        self.__move_x(delta_x)
        self.__move_z(delta_z)
        return


    def move_up(self, delta_time:int|float) -> None:
        if type(delta_time) not in (int, float):
            msg = "Camera.move_up argument 'delta_time' must be an int or float."
            raise TypeError(msg)

        delta_y = self.__mov_vel * delta_time
        self.__move_y(delta_y)
        return
    

    def move_down(self, delta_time:int|float) -> None:
        if type(delta_time) not in (int, float):
            msg = "Camera.move_down argument 'delta_time' must be an int or float."
            raise TypeError(msg)

        delta_y = -1 * self.__mov_vel * delta_time
        self.__move_y(delta_y)
        return
    

    def look_horizontal(self, mouse_delta_x:int|float) -> None:
        if type(mouse_delta_x) not in (int, float):
            msg = "Camera.look_horizontal argument 'mouse_delta_x' must be an int or float."
            raise TypeError(msg)
        
        delta_theta = mouse_delta_x * self.__rot_vel
        self.__rot_theta(delta_theta)


    def look_vertical(self, mouse_delta_y:int|float) -> None:
        if type(mouse_delta_y) not in (int, float):
            msg = "Camera.look_vertical argument 'mouse_delta_y' must be an int or float."
            raise TypeError(msg)
        
        # multiple by -1 because pygame treats down as positive
        delta_phi = -1 * mouse_delta_y * self.__rot_vel
        self.__rot_phi(delta_phi)


    def project_all(self, objs:list[Object], window:pg.surface.Surface) -> tuple[Triangle2D]:
        msg = "Camera.project_all argument 'objs' must be a list of Object objects."
        if type(objs) is not list:
            raise TypeError(msg)
        else:
            for obj in objs:
                if type(obj) is not Object:
                    raise ValueError(msg)
        if type(window) is not pg.surface.Surface:
            msg = "Camera.project_all argument 'window' must be a pygame.surface.Surface object."
            raise TypeError(msg)
        del msg

        projected_faces = list()
        for obj in objs:
            projected_faces.extend(self.project_obj(obj, window))
        return tuple(projected_faces)


    def project_obj(self, obj:Object, window:pg.surface.Surface) -> tuple[Triangle2D]:
        if type(obj) is not Object:
            msg = "Camera.project_obj argument 'obj' must be an Object object."
            raise TypeError(msg)
        if type(window) is not pg.surface.Surface:
            msg = "Camera.project_obj argument 'window' must be a pygame.surface.Surface object."

        projected_faces = list()
        for face in obj.get_faces():
            projected_faces.append(self.project_face(Triangle3D(face), window))
        return tuple(projected_faces)
    

    def project_face(self, face:Triangle3D, window:pg.surface.Surface) -> Triangle2D:
        if type(face) is not Triangle3D:
            msg = "Camera.project_face argument 'face' must be a Triangle3D object."
            raise TypeError(msg)
        if type(window) is not pg.surface.Surface:
            msg = "Camera.project_face argument 'window' must be a pygame.surface.Surface object."
            raise TypeError(msg)

        points = face.get_vertices()
        cam_dist = window.get_width() / (2 * tan(radians(self.get_fov() / 2)))
        projected_points = list()
        for point in points:
            rel_rot = self.get_relative_rot(point)
            # add (window.get_width/height() / 2) to center the screen
            # multiply second part of projected_y by -1 because pygame treats down as positive
            projected_x = (window.get_width() / 2) + cam_dist * tan(radians(rel_rot.get_theta()))
            projected_y = (window.get_height() / 2) + -1 * cam_dist * tan(radians(rel_rot.get_phi()))
            projected_points.append(Point2D(projected_x, projected_y))
        return Triangle2D(tuple(projected_points))


    def get_relative_rot(self, point:Point3D) -> Rotation3D:
        if type(point) is not Point3D:
            msg = "Camera.get_relative_rot argument 'point' must be a Point3D object."
            raise TypeError(msg)

        # start by finding the rotation relative to rot(0, 0) if we take the camera as the origin
        delta_x = point.get_x() - self.get_x()
        delta_y = point.get_y() - self.get_y()
        delta_z = point.get_z() - self.get_z()
        abs_theta = degrees(atan(delta_z / delta_x))
        abs_phi = degrees(atan(delta_y / sqrt(delta_x**2 + delta_z**2)))
        abs_rot = Rotation3D(abs_theta, abs_phi)
        rel_rot = abs_rot - self.get_rot()
        return rel_rot
