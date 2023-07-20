from point import Point
import pygame


def connect_points(screen, background, offset: int, i: int, j: int, points: list[int, int]) -> None:
    '''
    draw line between two points
    '''
    point_a = points[i + offset]
    point_b = points[j + offset]

    pygame.draw.line(screen, background, (point_a[0], point_a[1]), (point_b[0], point_b[1]))
