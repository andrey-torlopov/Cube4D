from math import cos, sin
from point import Point
import numpy as np


def matrix_to_point(m: np.ndarray) -> Point:
    result = Point(
        m[0][0],
        m[1][0],
        0
    )
    if len(m) > 2:
        result.z = m[2][0]

    return result


def matmul_point(matrix: np.ndarray, p: Point) -> Point:
    return matrix_to_point(np.dot(matrix, p.matrix))


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
    '''
    rotation_x = make_rotation_x(angles[0])
    rotation_y = make_rotation_y(angles[1])
    rotation_z = make_rotation_z(angles[2])

    rotate_x_point = matmul_point(rotation_x, point)
    rotate_y_point = matmul_point(rotation_y, rotate_x_point)
    rotate_z_point = matmul_point(rotation_z, rotate_y_point)

    k = 1 / (distance - rotate_z_point.z)

    projection_matrix = np.array([
        [k, 0, 0],
        [0, k, 0]
    ])

    point_2d = matmul_point(projection_matrix, rotate_z_point)

    x = (point_2d.x * scale) + circle_pos[0]
    y = (point_2d.y * scale) + circle_pos[1]

    return (x, y)
