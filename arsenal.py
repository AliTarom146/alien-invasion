"""Manage the bullets fired during the game."""

import pygame

from bullet import Bullet


class Arsenal:
    """Manage the game's active bullets."""

    def __init__(self, game):
        """Initialize the bullet group."""
        self.game = game
        self.bullets = pygame.sprite.Group()
        self.bullet_limit = game.settings.laser_limit

    def fire_bullet(self):
        """Create a bullet if the bullet limit has not been reached."""
        if len(self.bullets) < self.bullet_limit:
            bullet = Bullet(self.game)
            self.bullets.add(bullet)
            return True

        return False

    def update(self):
        """Update bullets and remove those that leave the screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def draw(self):
        """Draw all active bullets."""
        self.bullets.draw(self.game.screen)
