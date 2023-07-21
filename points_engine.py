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

    if len(m) > 3:
        result.w = m[3][0]

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


def make_rotation_XY(angle: float) -> np.ndarray:
    return np.array([
        [cos(angle), -sin(angle), 0, 0],
        [sin(angle), cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def make_rotation_XZ(angle: float) -> np.ndarray:
    return np.array([
        [cos(angle), 0, -sin(angle), 0],
        [0, 1, 0, 0],
        [sin(angle), 0, cos(angle), 0],
        [0, 0, 0, 1]
    ])


def make_rotation_XW(angle: float) -> np.ndarray:
    return np.array([
        [cos(angle), 0, 0, -sin(angle)],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [sin(angle), 0, 0, cos(angle)]
    ])


def make_rotation_ZW(angle: float) -> np.ndarray:
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, cos(angle), -sin(angle)],
        [0, 0, sin(angle), cos(angle)]
    ])


def process_points(point: Point,
                   angles: tuple[float, float, float, float],
                   scale: float,
                   circle_pos: tuple[int, int],
                   distance: int) -> tuple[int, int]:
    '''
    Rotate point by angles, scale and move to center
    and return X, Y coordinates
    and converting 4D to 3D coodinates
    '''

    rotarion_XY = make_rotation_XY(angles[0])
    rotarion_ZW = make_rotation_ZW(angles[1])
    rotarion_XW = make_rotation_XW(angles[2])

    rotated_point4D = matmul_point(rotarion_XY, point)
    rotated_point4D = matmul_point(rotarion_ZW, rotated_point4D)
    rotated_point4D = matmul_point(rotarion_XW, rotated_point4D)

    k = 1 / (distance - point.w)

    projection_matrix_3D = np.array([
        [k, 0, 0, 0],
        [0, k, 0, 0],
        [0, 0, k, 0]
    ])

    point = matmul_point(projection_matrix_3D, rotated_point4D)
    point.mult(scale)
    point3D = Point3D(point.x, point.y, point.z)

    projecion_matrix_2D = np.array([
        [1, 0, 0],
        [0, 1, 0]
    ])

    point_coordinates = np.array([
        [point3D.x],
        [point3D.y],
        [point3D.z]
    ])

    coordinate_2D = np.dot(projecion_matrix_2D, point_coordinates)

    x = (coordinate_2D[0][0]) + circle_pos[0]
    y = (coordinate_2D[1][0]) + circle_pos[1]

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
