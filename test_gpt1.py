import pygame
import sys
from pygame.locals import *
from math import sin, cos, radians

# Инициализация Pygame
pygame.init()

# Размер окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Инициализация цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Инициализация 4D куба
cube_vertices = [
    (-1, -1, -1, -1),
    (-1, -1, -1, 1),
    (-1, -1, 1, -1),
    (-1, -1, 1, 1),
    (-1, 1, -1, -1),
    (-1, 1, -1, 1),
    (-1, 1, 1, -1),
    (-1, 1, 1, 1),
    (1, -1, -1, -1),
    (1, -1, -1, 1),
    (1, -1, 1, -1),
    (1, -1, 1, 1),
    (1, 1, -1, -1),
    (1, 1, -1, 1),
    (1, 1, 1, -1),
    (1, 1, 1, 1)
]

cube_edges = [
    (0, 1), (0, 2), (0, 4), (0, 8),
    (1, 3), (1, 5), (1, 9),
    (2, 3), (2, 6), (2, 10),
    (3, 7), (3, 11),
    (4, 5), (4, 6), (4, 12),
    (5, 7), (5, 13),
    (6, 7), (6, 14),
    (7, 15),
    (8, 9), (8, 10), (8, 12),
    (9, 11), (9, 13),
    (10, 11), (10, 14),
    (11, 15),
    (12, 13), (12, 14),
    (13, 15),
    (14, 15)
]

# Инициализация угла поворота
angle = 0

# Создание окна
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Вращающийся 4D куб')

clock = pygame.time.Clock()

# # Проецирование 4D координат на 3D координаты


# def project_to_3D(x, y, z, w):
#     scale = 200  # Масштабирование
#     fov = 256  # Глубина обзора
#     screen_x = x * fov / (w + fov) + WINDOW_WIDTH / 2
#     screen_y = y * fov / (w + fov) + WINDOW_HEIGHT / 2
#     return screen_x * scale, screen_y * scale

# Проецирование 4D координат на 2D плоскость


def project_to_2D(x, y, z, w):
    scale = min(WINDOW_WIDTH, WINDOW_HEIGHT) / 2  # Масштабирование
    screen_x = x * scale / (w + 6) + WINDOW_WIDTH / 2
    screen_y = y * scale / (w + 6) + WINDOW_HEIGHT / 2
    return screen_x, screen_y


# Главный цикл программы
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    window_surface.fill(BLACK)

    # Поворот 4D куба
    angle += 1

    # Преобразование вершин 4D куба в 2D координаты
    rotated_vertices = []
    for vertex in cube_vertices:
        x, y, z, w = vertex
        # Применение матрицы поворота вокруг оси Y
        x, z = x * cos(radians(angle)) - z * sin(radians(angle)), x * sin(radians(angle)) + z * cos(radians(angle))
        # Применение матрицы поворота вокруг оси X
        y, z = y * cos(radians(angle)) - z * sin(radians(angle)), y * sin(radians(angle)) + z * cos(radians(angle))
        # Применение матрицы поворота вокруг оси Z
        x, y = x * cos(radians(angle)) - y * sin(radians(angle)), x * sin(radians(angle)) + y * cos(radians(angle))
        # Проецирование 4D координат на 2D плоскость
        screen_x, screen_y = project_to_2D(x, y, z, w)
        rotated_vertices.append((screen_x, screen_y))

    # Рисование 4D куба
    for edge in cube_edges:
        x1, y1 = rotated_vertices[edge[0]]
        x2, y2 = rotated_vertices[edge[1]]
        pygame.draw.line(window_surface, WHITE, (x1, y1), (x2, y2), 1)

    # Обновление экрана
    pygame.display.update()
    clock.tick(60)
