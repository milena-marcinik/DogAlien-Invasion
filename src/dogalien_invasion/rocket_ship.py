import pygame


class RocketShip:
    def __init__(self, screen, ai_settings):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/rocket_ship.png")
        self.image = pygame.transform.scale(self.image,
                                            (self.ai_settings.rocket_ship_width, self.ai_settings.rocket_ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.rocket_ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.rocket_ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def center_rocket_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
