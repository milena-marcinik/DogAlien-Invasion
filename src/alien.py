import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien images
        def resize(image):
            image = pygame.transform.scale(image, (ai_settings.alien_width, ai_settings.alien_height))
            return image

        self.images = []
        self.images.extend(
            [resize(pygame.image.load("images/alien_001.png")), resize(pygame.image.load("images/alien_002.png")),
             resize(pygame.image.load("images/alien_003.png")), resize(pygame.image.load("images/alien_004.png")),
             resize(pygame.image.load("images/alien_005.png")), resize(pygame.image.load("images/alien_006.png")),
             resize(pygame.image.load("images/alien_007.png")), resize(pygame.image.load("images/alien_008.png"))])

        self.index = 0
        self.alien_image = self.images[self.index]

        # Get rect alien images
        self.rect = self.alien_image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Make an animation."""
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.alien_image = self.images[self.index]

        # Move the alien right or left.
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.alien_image, self.rect)
