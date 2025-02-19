import sys
import pygame

from settings import Settings
from star import Star

def run_game():
    """Initialize the game objects and run the game."""
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Stars")

    star = Star(settings, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(settings.screen_bg_color)
        star.blitme()
        pygame.display.flip()

run_game()
