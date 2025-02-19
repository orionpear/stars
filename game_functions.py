"""This module contains functions of the game."""

import sys
import pygame

def check_events(event):
    """Respond to keypresses and releases."""
    if event.type == pygame.QUIT:
        sys.exit()


def update_screen(settings, screen, star):
    """Update the screen."""
    screen.fill(settings.screen_bg_color)
    star.blitme()
    pygame.display.flip()