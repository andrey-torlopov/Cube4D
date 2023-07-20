from math import cos, sin
from point import Point, Point3D
import numpy as np


def matrix_to_point(m: np.ndarray) -> Point:
    result = Point(
        m[0][0],
        m[1][0],
        0,
        0
    )
    if len(m) > 2:
        result.z = m[2][0]

    return result


def matmul_point(matrix: np.ndarray, p: Point) -> Point:
    return matrix_to_point(np.dot(matrix, p.matrix))


def matmul_point3D(matrix: np.ndarray, p: Point3D) -> Point3D:
    coordinates3D = np.dot(matrix, p.matrix)
    return Point3D(coordinates3D[0][0], coordinates3D[1][0], coordinates3D[2][0],)


def make_rotation_x(angle: float) -> np.ndarray:
    return np.array([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ])


def make_rotation_y(angle: float) -> np.ndarray:
    return np.array([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ])


def make_rotation_z(angle: float) -> np.ndarray:
    return np.array([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])


def process_points(point: Point,
                   angles: tuple[float, float, float],
                   scale: float,
                   circle_pos: tuple[int, int],
                   distance: int) -> tuple[int, int]:
    '''
    Rotate point by angles, scale and move to center
    and return X, Y coordinates
    and converting 4D to 3D coodinates
    '''

    rotation_x = make_rotation_x(angles[0])
    rotation_y = make_rotation_y(angles[1])
    rotation_z = make_rotation_z(angles[2])

    k = 1 / (distance - point.w)

    projection_matrix_3D = np.array([
        [k, 0, 0, 0],
        [0, k, 0, 0],
        [0, 0, k, 0]
    ])

    point = matmul_point(projection_matrix_3D, point)
    point3D = Point3D(point.x, point.y, point.z)

    rotate_x_point = matmul_point3D(rotation_x, point3D)
    rotate_y_point = matmul_point3D(rotation_y, rotate_x_point)
    rotate_z_point = matmul_point3D(rotation_z, rotate_y_point)

    projecion_matrix_2D = np.array([
        [1, 0, 0],
        [0, 1, 0]
    ])

    point_coordinates = np.array([
        [rotate_z_point.x],
        [rotate_z_point.y],
        [rotate_z_point.z]
    ])

    coordinate_2D = np.dot(projecion_matrix_2D, point_coordinates)

    x = (coordinate_2D[0][0] * scale) + circle_pos[0]
    y = (coordinate_2D[1][0] * scale) + circle_pos[1]

    return (x, y)


def process_points2d(point: Point,
                     angles: tuple[float, float, float],
                     scale: float,
                     circle_pos: tuple[int, int],
                     distance: int) -> tuple[int, int]:
    '''
    Rotate point by angles, scale and move to center
    and return X, Y coordinates
    '''
    rotation_x = make_rotation_x(angles[0])
    rotation_y = make_rotation_y(angles[1])
    rotation_z = make_rotation_z(angles[2])

    rotate_x_point = matmul_point3D(rotation_x, point)
    rotate_y_point = matmul_point3D(rotation_y, rotate_x_point)
    rotate_z_point = matmul_point3D(rotation_z, rotate_y_point)

    k = 1 / (distance - rotate_z_point.z)

    projection_matrix = np.array([
        [k, 0, 0],
        [0, k, 0]
    ])

    point_2d = matmul_point(projection_matrix, rotate_z_point)

    x = (point_2d.x * scale) + circle_pos[0]
    y = (point_2d.y * scale) + circle_pos[1]

    return (x, y)
