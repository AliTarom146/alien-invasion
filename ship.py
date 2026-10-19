
"""Manage the player's ship."""

import pygame


class Ship:
    """Manage the player's ship and its movement."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
        "Assets/images/ship2(no bg).png"
        ).convert_alpha()

        self.image = pygame.transform.scale(self.image, (41, 60))

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Move the ship while keeping it inside the screen."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def draw(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Ask the game's arsenal to fire a bullet."""
        return self.game.arsenal.fire_bullet()
