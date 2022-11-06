import pygame
from pygame.locals import RESIZABLE

from constants import WINDOW_H, WINDOW_L


"""
Import from pygame library

Import different variables
"""

pygame.init()

# Opening the pygame and Title window
window = pygame.display.set_mode((WINDOW_L, WINDOW_H), RESIZABLE)

# Title
pygame.display.set_caption("Sauvez le monde")

# Screen refresh
pygame.display.flip()
pygame.key.set_repeat(400, 30)