import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to manage stars"""

    def __init__(self, settings, screen):
        """Create a star object at the current location."""
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.default_image_size = 50, 50
        self.image = pygame.image.load(settings.star_filename)
        self.image = pygame.transform.scale(self.image, settings.star_default_image_size)
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y
    
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)