from point import Point
import pygame


def connect_points(screen, background, i: int, j: int, points: list[int, int]) -> None:
    '''
    draw line between two points
    '''
    pygame.draw.line(screen, background, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
