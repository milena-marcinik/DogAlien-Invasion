import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, rocket_ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load and resize bullet images
        def resize(image):
            image = pygame.transform.scale(image, (ai_settings.bullet_width, ai_settings.bullet_height))
            return image

        self.images = []
        self.images.extend(
            [resize(pygame.image.load("images/bullet_001.png")), resize(pygame.image.load(
                "images/bullet_002.png")),
             resize(pygame.image.load("images/bullet_003.png")), resize(pygame.image.load(
                "images/bullet_004.png")),
             resize(pygame.image.load("images/bullet_005.png")), resize(pygame.image.load(
                "images/bullet_006.png")),
             resize(pygame.image.load("images/bullet_007.png"))])

        self.index = 0
        self.bullet_image = self.images[self.index]

        # Get rect bullet images
        self.rect = pygame.Rect((0, 0, ai_settings.bullet_width, ai_settings.bullet_height))
        self.rect.centerx = rocket_ship.rect.centerx
        self.rect.top = rocket_ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

        # Animation
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.bullet_image = self.images[self.index]

    def draw_bullet(self, surface):
        """Draw the bullet to the screen."""
        surface.blit(self.bullet_image, self.rect)
