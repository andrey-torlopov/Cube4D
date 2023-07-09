from operator import matmul
import pygame
import numpy as np
from math import *
from dataclasses import dataclass


# Init block
WHITE = (255, 255, 255)
RED = (255, 100, 0, 100)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 640
ROTATE_SPEED = 0.02
clock = pygame.time.Clock()
pygame.display.set_caption("3D cube projection")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
circle_pos = [WIDTH / 2, HEIGHT / 2]  # x, y
SCALE = 100
ANGLE_X = ANGLE_Y = ANGLE_Z = 0

#Check angle!
ANGLE_X = 10

# Model

@dataclass
class Point:
    x: float
    y: float
    z: float

    @property
    def matrix(self) -> np.matrix[float]:
        '''Return matrix'''
        return np.matrix([self.x, self.y, self.z])

points = []

# all the cube vertices
points.append(Point(-1, -1, 1))
points.append(Point(1, -1, 1))
points.append(Point(1, 1, 1))
points.append(Point(-1, 1, 1))
points.append(Point(-1, -1, -1))
points.append(Point(1, -1, -1))
points.append(Point(1, 1, -1))
points.append(Point(-1, 1, -1))

projection_matrix = [Point(1,0,0), Point(0, 1, 0)]

projected_points = [[n, n] for n in range(len(points))]

def connect_points(i, j, points: list[Point]) -> None:
    '''
    Draw line!
    '''
    pygame.draw.line(
        screen, WHITE, (points[i].x, points[i].y), (points[j].x, points[j].y))

def matmul_m(a, b):
    ''' Matrix multiplication. Analog matmul function'''
    a_rows = len(a)
    a_cols = len(a[0])

    b_rows = len(b)
    b_cols = len(b[0])
    # Dot product matrix dimentions = a_rows x b_cols
    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    if a_cols != b_rows:
        print("INCOMPATIBLE MATRIX SIZES")
        return product

    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(b_rows):
                product[i][j] += a[i][k] * b[k][j]

    return product

while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    ANGLE_Y += ROTATE_SPEED

    # ANGLE_Y += ROTATE_SPEED
    # ANGLE_Z += ROTATE_SPEED

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_r]:
        #     ANGLE_Y = ANGLE_X = ANGLE_Z = 0
        # if keys[pygame.K_a]:
        #     ANGLE_Y += ROTATE_SPEED
        # if keys[pygame.K_d]:
        #     ANGLE_Y -= ROTATE_SPEED
        # if keys[pygame.K_w]:
        #     ANGLE_X += ROTATE_SPEED
        # if keys[pygame.K_s]:
        #     ANGLE_X -= ROTATE_SPEED
        # if keys[pygame.K_q]:
        #     ANGLE_Z -= ROTATE_SPEED
        # if keys[pygame.K_e]:
        #     ANGLE_Z += ROTATE_SPEED

    # update stuff

    rotation_x = [[1, 0, 0],
                    [0, cos(ANGLE_X), -sin(ANGLE_X)],
                    [0, sin(ANGLE_X), cos(ANGLE_X)]]

    rotation_y = [[cos(ANGLE_Y), 0, sin(ANGLE_Y)],
                    [0, 1, 0],
                    [-sin(ANGLE_Y), 0, cos(ANGLE_Y)]]

    rotation_z = [[cos(ANGLE_Z), -sin(ANGLE_Z), 0],
                    [sin(ANGLE_Z), cos(ANGLE_Z), 0],
                    [0, 0, 1]]


    # drawining stuff

    i = 0
    for point in points:
        rotated2d = np.dot(rotation_y, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_z, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * SCALE) + circle_pos[0]
        y = int(projected2d[1][0] * SCALE) + circle_pos[1]

        projected_points[i] = [x, y]

        pygame.draw.circle(screen, WHITE, (x, y), 5)
        i += 1

    for p in range(4):
        connect_points(p, (p+1) % 4, projected_points)
        connect_points(p+4, ((p+1) % 4) + 4, projected_points)
        connect_points(p, (p+4), projected_points)

    pygame.display.update()