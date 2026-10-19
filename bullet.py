"""Manage bullets fired by the player's ship."""

import pygame


class Bullet(pygame.sprite.Sprite):
    """Represent a bullet fired by the ship."""

    def __init__(self, game):
        """Create a bullet at the ship's current position."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            self.settings.laser_image
        ).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet upward."""
        self.y -= self.settings.laser_speed
        self.rect.y = self.y
