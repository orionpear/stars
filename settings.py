"""This module contains the class Settings."""

class Settings():
    """This class manages the settings of the game."""

    def __init__(self):
        """Initialize the settings of the game."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = 230, 230, 230

        # Star settings
        self.star_filename = 'images/star.bmp'