import pygame


def load_image(name):
    image = pygame.image.load(name)
    return image


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings:
        self.display_width = 1300
        self.display_height = 750
        self.background = pygame.image.load("images/galaxy.jpg")
        self.start_screen = pygame.image.load("images/galaxy.jpg")

        # Rocket ship settings
        self.rocket_ship_width = 80
        self.rocket_ship_height = 166
        self.rocket_ship_limit = 3

        # Bullet settings
        self.bullet_width = 20
        self.bullet_height = 20
        self.bullets_allowed = 4

        # Alien settings
        self.alien_width = 88
        self.alien_height = 65
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_drop_speed = 8

        # Empty ship settings
        self.empty_ship_width = 20
        self.empty_ship_height = 30

        # Button settings
        self.button_width = 204
        self.button_height = 194
        self.button_center = (400, 400)

        # How quickly the game speeds up
        self.speedup_scale = 1.15
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.rocket_ship_speed_factor = 0.8
        self.bullet_speed_factor = 1.0
        self.alien_speed_factor = 0.17

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