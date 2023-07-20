from point import Point
import pygame


def connect_points(screen, stroke_color, i: int, j: int, coordinates: list[int, int]) -> None:
    '''
    draw line between two points
    '''
    pygame.draw.line(screen, stroke_color, (coordinates[i][0], coordinates[i][1]), (coordinates[j][0], coordinates[j][1]))
