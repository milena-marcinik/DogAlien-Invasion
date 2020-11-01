import pygame

from pygame.sprite import Sprite


class EmptyShip(Sprite):
    def __init__(self, ai_settings, screen):
        super(EmptyShip, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/empty_ship.png")

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.top = 5
        self.rect.left = self.screen_rect.left + 5

    def draw_empty_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
