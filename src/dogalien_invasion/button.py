import pygame
from pygame.sprite import Sprite


class Button(Sprite):
    def __init__(self, ai_settings, screen):
        super(Button, self).__init__()
        """Initialize button attributes."""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.mouse_over = False

        # Load button image
        image = pygame.image.load("images/button1.png")
        highlighted_image = pygame.transform.scale(image,
                                                   (self.ai_settings.button_width, self.ai_settings.button_height))

        # create the image that shows when mouse is over the element
        image = pygame.transform.scale(image,
                                       (int(self.ai_settings.button_width * 0.8),
                                        int(self.ai_settings.button_height * 0.8)))

        # add both images and their rects to lists
        self.images = [image, highlighted_image]
        self.rects = [image.get_rect(center=self.screen_rect.center),
                      highlighted_image.get_rect(center=self.screen_rect.center)]

        # properties that vary the image and its rect when the mouse is over the element

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update_button(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw_button(self):
        self.screen.blit(self.image, self.rect)
