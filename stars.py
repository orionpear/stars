import sys
import pygame


def run_game():
    """Initialize the game objects and run the game."""
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Stars")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((230, 230, 230))
        pygame.display.flip()

run_game()
