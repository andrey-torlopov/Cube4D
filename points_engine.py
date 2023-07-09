from math import cos, sin
from point import Point


def matrix_to_point(m: list[float, float]) -> Point:
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


def matmul_point(a: list[float, float], p: Point) -> Point:
    return matrix_to_point(matmul_m(a, p.matrix))


def matmul_m(a: list[float, float], b: list[float]) -> list[float]:
    ''' Matrix multiplication. Analog matmul function'''
    a_rows = len(a)
    a_cols = len(a[0])

    b_rows = len(b)
    b_cols = len(b[0])

    # Dot product matrix dimentions = a_rows x b_cols
    product: list[float, float] = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    if a_cols != b_rows:
        print("INCOMPATIBLE MATRIX SIZES")
        print(f'a_rows {a_rows} a_cols {a_cols} b_rows {b_rows} b_cols {b_cols}')
        exit()
        return product

    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(b_rows):
                product[i][j] += a[i][k] * b[k][j]

    return product


def make_rotation_x(angle: float) -> list[float, float]:
    return [
        [1, 0, 0, 0],
        [0, cos(angle), -sin(angle), 0],
        [0, sin(angle), cos(angle), 0],
        [0, 0, 0, 1]
    ]


def make_rotation_y(angle: float) -> list[float, float]:
    return [
        [cos(angle), 0, sin(angle), 0],
        [0, 1, 0, 0],
        [-sin(angle), 0, cos(angle), 0],
        [0, 0, 0, 1]
    ]


def make_rotation_z(angle: float) -> list[float, float]:
    return [
        [cos(angle), -sin(angle), 0, 0],
        [sin(angle), cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]


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

    rotate_x = matmul_point(rotation_x, point)
    rotate_y = matmul_point(rotation_y, rotate_x)
    rotate_z = matmul_point(rotation_z, rotate_y)

    z = 1 / (distance - rotate_z.w)

    projection_matrix = [
        [1 / z, 0, 0, 0],
        [0, 1 / z, 0, 0],
        [0, 0, 1 / z, 0],
    ]

    point_2d = matmul_point(projection_matrix, rotate_z)  # type: ignore

    x = (point_2d.x * scale) + circle_pos[0]
    y = (point_2d.y * scale) + circle_pos[1]

    return (x, y)
