# Import the pygame module
import pygame

running = True

# Import pygame.locals
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN,
                           QUIT)

# Initials pygame

pygame.init()

# deine constants for the screen
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200

# craete the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
