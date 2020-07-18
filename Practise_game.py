import pygame
from pygame.locals import (
                            K_UP,
                            K_DOWN,
                            K_LEFT,
                            K_RIGHT,
                            K_ESCAPE,
                            K_DOWN,
                            QUIT,
                            KEYDOWN,
                            )

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

is_game_running = True

while is_game_running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                is_game_running = False
        elif event.type == QUIT:
            is_game_running = False

screen.fill((255, 255, 255))

surf = pygame.Surface((50, 50))

surf.fill((0, 0, 0))

rect = surf.get_rect()

screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()
