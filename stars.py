import pygame
from pygame.sprite import Group

from settings import Settings
from star import Star
import game_functions as gf

def run_game():
    """Initialize the game objects and run the game."""
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Stars")

    star = Star(settings, screen)
    star_width, star_height = star.rect.width, star.rect.height
    stars = Group()
    number_stars = gf.get_number_stars(settings, star_width)
    number_rows = gf.get_number_rows(settings, star_height)
    gf.create_grid_stars(
        settings, screen, stars,
        star_width, star_height,
        number_rows, number_stars)

    while True:
        for event in pygame.event.get():
            gf.check_events(event)
            
            gf.update_screen(settings, screen, stars)

run_game()
