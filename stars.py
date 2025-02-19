import pygame

from settings import Settings
from star import Star
import game_functions as gf

def run_game():
    """Initialize the game objects and run the game."""
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Stars")

    star = Star(settings, screen)

    while True:
        for event in pygame.event.get():
            gf.check_events(event)
            gf.update_screen(settings, screen, star)

run_game()
