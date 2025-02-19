"""This module contains functions of the game."""

import sys
import pygame

def check_events(event):
    """Respond to keypresses and releases."""
    if event.type == pygame.QUIT:
        sys.exit()