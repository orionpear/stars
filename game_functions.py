"""This module contains functions of the game."""

import sys
import pygame

from star import Star

def check_events(event):
    """Respond to keypresses and releases."""
    if event.type == pygame.QUIT:
        sys.exit()


def update_screen(settings, screen, stars):
    """Update the screen."""
    screen.fill(settings.screen_bg_color)
    draw_stars(stars)
    pygame.display.flip()


def create_row_stars(
        settings, screen, stars, star_width,
        star_height, row_number, number_stars):
    """Create a row of stars."""
    for star_number in range(number_stars):
        star = Star(settings, screen)
        star.rect.x = 2 * star_number * star_width
        star.rect.y = 2 * row_number * star_height
        stars.add(star)


def create_grid_stars(
        settings, screen, stars, star_width,
        star_height, number_rows, number_stars):
    """Create a grid of stars."""
    for row_number in range(number_rows):
        create_row_stars(
            settings, screen, stars,
            star_width, star_height,
            row_number, number_stars)
        

def draw_stars(stars):
    for star in stars.sprites():
        star.blitme()


def get_number_stars(settings, star_width):
    """Calculate and return the number of stars possible in row."""
    available_space_x = settings.screen_width
    return int(available_space_x / (2 * star_width))


def get_number_rows(settings, star_height):
    """Calculate and return the number of rows possible on the screen."""
    available_space_y = settings.screen_height
    return int(available_space_y / (2 * star_height))