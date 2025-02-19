import sys
import pygame

from settings import Settings

def run_game():
    """Initialize the game objects and run the game."""
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Stars")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((230, 230, 230))
        pygame.display.flip()

run_game()
