import pygame.font
from pygame.sprite import Group

from src.dogalien_invasion.empty_ship import EmptyShip


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (152, 251, 152)
        self.font = pygame.font.Font("font/space age.ttf", 45)
        self.font_hs = pygame.font.Font("font/space age.ttf", 30)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_empty_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.background)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 5
        self.score_rect.top = 5

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        self.empty_ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = f"HIGH SCORE: {high_score:,}"
        self.high_score_image = self.font_hs.render(high_score_str, True, self.text_color, self.ai_settings.background)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = f"LEVEL: {self.stats.level}"
        self.level_image = self.font_hs.render(level_str, True, self.text_color, self.ai_settings.background)

        # Center the high score at the top of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.bottom = self.score_rect.bottom + 20

    def prep_empty_ships(self):
        """Show how many ships are left."""
        self.empty_ships = Group()
        for rocket_ship_number in range(self.stats.rocket_ships_left):
            empty_ship = EmptyShip(self.ai_settings, self.screen)
            empty_ship.rect.x = 10 + rocket_ship_number * empty_ship.rect.width
            empty_ship.rect.y = 10
            self.empty_ships.add(empty_ship)
