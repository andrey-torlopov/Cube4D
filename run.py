from math import *
from operator import matmul

import pygame
from point import Point

# Init block
WHITE = (255, 255, 255)
RED = (255, 100, 0, 100)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 640
ROTATE_SPEED = 0.02
clock = pygame.time.Clock()
pygame.display.set_caption("4D cube")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

circle_pos = [WIDTH / 2, HEIGHT / 2]  # x, y
SCALE = 50
ANGLE_X = ANGLE_Y = ANGLE_Z = 0

# Check angle!
ANGLE_X = 10
points = []

# all the cube vertices
points.append(Point(-1, -1, 1, 1))
points.append(Point(1, -1, 1, 1))
points.append(Point(1, 1, 1, 1))
points.append(Point(-1, 1, 1, 1))
points.append(Point(-1, -1, -1, 1))
points.append(Point(1, -1, -1, 1))
points.append(Point(1, 1, -1, 1))
points.append(Point(-1, 1, -1, 1))

points.append(Point(-1, -1, 1, -1))
points.append(Point(1, -1, 1, -1))
points.append(Point(1, 1, 1, -1))
points.append(Point(-1, 1, 1, -1))
points.append(Point(-1, -1, -1, -1))
points.append(Point(1, -1, -1, -1))
points.append(Point(1, 1, -1, -1))
points.append(Point(-1, 1, -1, -1))


projected_points = [[n, n] for n in range(len(points))]


def connect_points(i: int, j: int, points: list[int, int]) -> None:
    '''
    draw line between two points
    '''
    pygame.draw.line(screen, WHITE, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


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


while True:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    ANGLE_Y += ROTATE_SPEED

    ANGLE_Y += ROTATE_SPEED
    ANGLE_Z += ROTATE_SPEED

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        ANGLE_Y = ANGLE_X = ANGLE_Z = 0
    if keys[pygame.K_a]:
        ANGLE_Y += ROTATE_SPEED
    if keys[pygame.K_d]:
        ANGLE_Y -= ROTATE_SPEED
    if keys[pygame.K_w]:
        ANGLE_X += ROTATE_SPEED
    if keys[pygame.K_s]:
        ANGLE_X -= ROTATE_SPEED
    if keys[pygame.K_q]:
        ANGLE_Z -= ROTATE_SPEED
    if keys[pygame.K_e]:
        ANGLE_Z += ROTATE_SPEED

    # Update

    rotation_x = [[1, 0, 0, 0],
                  [0, cos(ANGLE_X), -sin(ANGLE_X), 0],
                  [0, sin(ANGLE_X), cos(ANGLE_X), 0],
                  [0, 0, 0, 1]
                  ]

    rotation_y = [[cos(ANGLE_Y), 0, sin(ANGLE_Y), 0],
                  [0, 1, 0, 0],
                  [-sin(ANGLE_Y), 0, cos(ANGLE_Y), 0],
                  [0, 0, 0, 1]
                  ]

    rotation_z = [[cos(ANGLE_Z), -sin(ANGLE_Z), 0, 0],
                  [sin(ANGLE_Z), cos(ANGLE_Z), 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]
                  ]

    # Drawining
    i = 0
    for point in points:
        rotate_x = matmul_point(rotation_x, point)
        rotate_y = matmul_point(rotation_y, rotate_x)
        rotate_z = matmul_point(rotation_z, rotate_y)

        distance = 2
        z = 1 / (distance - rotate_z.w)

        projection_matrix = [
            [1/z, 0, 0, 0],
            [0, 1/z, 0, 0],
            [0, 0, 1/z, 0],
        ]

        point_2d = matmul_point(projection_matrix, rotate_z)  # type: ignore

        x = (point_2d.x * SCALE) + circle_pos[0]
        y = (point_2d.y * SCALE) + circle_pos[1]

        projected_points[i] = (x, y)
        i += 1
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    for p in range(4):
        connect_points(p, (p+1) % 4, projected_points)
        connect_points(p+4, ((p+1) % 4) + 4, projected_points)
        connect_points(p, (p+4), projected_points)

    pygame.display.update()
