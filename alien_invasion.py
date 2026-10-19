
"""Run the Alien Invasion game."""

import sys

import pygame

from settings import Settings
from ship import Ship
from arsenal import Arsenal


class AlienInvasion:
    """Manage the game and its main loop."""

    def __init__(self):
        """Initialize the game and create its resources."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.caption)

        self.clock = pygame.time.Clock()

        self.background = pygame.image.load(
            self.settings.background_image
        ).convert()
        self.background = pygame.transform.scale(
            self.background,
            (self.settings.screen_width, self.settings.screen_height),
        )

        self.ship = Ship(self)
        self.arsenal = Arsenal(self)

        self.laser_sound = pygame.mixer.Sound(
            self.settings.laser_sound
        )

    def run_game(self):
        """Run the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self.arsenal.update()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """Respond to keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    if self.ship.fire():
                        self.laser_sound.play()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Draw the game objects and update the display."""
        self.screen.blit(self.background, (0, 0))
        self.ship.draw()
        self.arsenal.draw()
        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
