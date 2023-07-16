import numpy as np
import pygame
from math import sin, cos, pi

clock = pygame.time.Clock()
pygame.display.set_caption("2D Cube")
WIDTH = 800
HEIGHT = 640
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
circle_pos = (WIDTH // 2, HEIGHT // 2)

# Params

angle = 0
scale = 50


class Point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    @property
    def matrix(self) -> np.ndarray:
        return np.array([[self.x], [self.y], [self.z]])


points: list[Point] = []
points.append(Point(-1, -1, -1))
points.append(Point(1, -1, -1))
points.append(Point(1, 1, -1))
points.append(Point(-1, 1, -1))

points.append(Point(-1, -1, 1))
points.append(Point(1, -1, 1))
points.append(Point(1, 1, 1))
points.append(Point(-1, 1, 1))

projection = np.array([
    [1, 0, 0],
    [0, 1, 0]
])


# Make rotate matrix

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

#


while True:
    clock.tick(60)
    screen.fill(BLACK)
    angle += 0.01

    rotation_x = make_rotation_x(angle)
    rotation_y = make_rotation_y(angle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Proccess points and draw
    for point in points:
        point_matrix = point.matrix * scale
        processed_matrix = np.dot(rotation_x, point_matrix)
        processed_matrix = np.dot(rotation_y, processed_matrix)
        xy = (circle_pos[0] + processed_matrix[0][0], circle_pos[1] + processed_matrix[1][0])
        pygame.draw.circle(screen, WHITE, xy, 5)

    pygame.display.update()
