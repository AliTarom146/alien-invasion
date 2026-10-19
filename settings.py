
"""Store settings for the Alien Invasion game."""


class Settings:
    """Manage the game's settings and asset locations."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.caption = "Alien Invasion"
        self.bg_color = (230, 230, 230)
        self.fps = 60

        # Ship settings
        self.ship_speed = 5
        self.ship_image = "Assets/images/ship.png"

        # Laser settings
        self.laser_speed = 8
        self.laser_limit = 5
        self.laser_image = "Assets/images/laserBlast.png"
        self.laser_sound = "Assets/sound/laser.mp3"

        # Background image
        self.background_image = "Assets/images/Starbasesnow.png"
