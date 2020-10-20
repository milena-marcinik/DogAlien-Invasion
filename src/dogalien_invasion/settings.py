import pygame


def load_image(name):
    image = pygame.image.load(name)
    return image


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings:
        self.display_width = 1800
        self.display_height = 1000
        self.background = pygame.image.load("images/galaxy.jpg")
        self.start_screen = pygame.image.load("images/galaxy.jpg")

        # Rocket ship settings
        self.rocket_ship_width = 100
        self.rocket_ship_height = 208
        self.rocket_ship_limit = 3

        # Bullet settings
        self.bullet_width = 25
        self.bullet_height = 25
        self.bullets_allowed = 4

        # Alien settings
        self.alien_width = 110
        self.alien_height = 75
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_drop_speed = 20

        # Empty ship settings
        self.empty_ship_width = 40
        self.empty_ship_height = 60

        # Button settings
        self.button_width = 240
        self.button_height = 228
        self.button_center = (400, 400)

        # How quickly the game speeds up
        self.speedup_scale = 1.3
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.rocket_ship_speed_factor = 12.0
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 2

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 10

    def increase_speed(self):
        """Increase speed settings and alien points values."""
        self.rocket_ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
