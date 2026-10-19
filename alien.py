
"""Manage an alien in the game."""

import pygame


class Alien(pygame.sprite.Sprite):
    """Represent a single alien."""

    def __init__(self, game):
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            "Assets/images/enemy_4.png"
        ).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def draw(self):
        """Draw the alien at its current position."""
        self.screen.blit(self.image, self.rect)
