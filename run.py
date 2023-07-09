import pygame
from point import Point
from point_initializers import initialize_points, initialize_projected_points
from screen_initializers import ScreenConfig
from points_draw import connect_points

from points_engine import (
    matrix_to_point,
    matmul_point,
    matmul_m,
    make_rotation_x,
    make_rotation_y,
    make_rotation_z,
    process_points
)

screen_config = ScreenConfig()
clock = pygame.time.Clock()
pygame.display.set_caption(screen_config.title)
screen = pygame.display.set_mode(screen_config.screen_size)
circle_pos = screen_config.center

# TODO: Temp code
screen_config.angle_x = 10

points = initialize_points()
projected_points = initialize_projected_points(points)

while True:
    clock.tick(screen_config.fps)
    screen.fill(screen_config.black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        screen_config.refresh()
    if keys[pygame.K_a]:
        screen_config.inc_angle_y()
    if keys[pygame.K_d]:
        screen_config.dec_angle_y()
    if keys[pygame.K_w]:
        screen_config.inc_angle_x()
    if keys[pygame.K_s]:
        screen_config.dec_angle_x()
    if keys[pygame.K_q]:
        screen_config.dec_angle_z()
    if keys[pygame.K_e]:
        screen_config.inc_angle_z()

    # Drawining
    i = 0
    for point in points:
        xy_points = process_points(
            point,
            screen_config.anglesXYZ,
            screen_config.scale,
            circle_pos,
            screen_config.distance
        )

        projected_points[i] = xy_points
        i += 1
        pygame.draw.circle(screen, screen_config.background, xy_points, 5)

    for p in range(4):
        connect_points(screen, screen_config.background, p, (p + 1) % 4, projected_points)
        connect_points(screen, screen_config.background, p + 4, ((p + 1) % 4) + 4, projected_points)
        connect_points(screen, screen_config.background, p, (p + 4), projected_points)

    pygame.display.update()
