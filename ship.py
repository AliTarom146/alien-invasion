import pygame


class Ship:
    """Manage the player's ship."""

    def __init__(self, screen):
        """Initialize the ship and its starting position."""
        self.screen = screen
        self.image = pygame.image.load("Assets/images/ship.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.speed = 5
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Move the ship based on the keyboard input."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        self.rect.x = self.x

    def draw(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)
