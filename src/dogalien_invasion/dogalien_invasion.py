"""Main module."""
import pygame
import src.dogalien_invasion.game_functions as game_functions
from pygame.sprite import Group
from src.dogalien_invasion.settings import Settings
from src.dogalien_invasion.game_stats import GameStats
from src.dogalien_invasion.button import Button
from src.dogalien_invasion.rocket_ship import RocketShip
from src.dogalien_invasion.scoreboard import Scoreboard
from src.dogalien_invasion.empty_ship import EmptyShip


def run_game():
    """The function opens the game and creates a screen"""
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.display_width, ai_settings.display_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a rocket ship
    rocket_ship = RocketShip(screen, ai_settings)

    # Make a group to store bullets in.
    bullets = Group()

    # Make a group of Aliens and the fleet.
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, rocket_ship, aliens)

    # Create an instance to store game statistics.# Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    empty_ship = EmptyShip(ai_settings, screen)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Play button.
    play_button = Button(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        game_functions.check_events(ai_settings, screen, stats, sb, play_button, rocket_ship, aliens, bullets)

        if stats.game_active:
            rocket_ship.update()
            game_functions.update_bullets(ai_settings, screen, stats, sb, rocket_ship, aliens, bullets)
            game_functions.update_aliens(ai_settings, stats, sb, screen, rocket_ship, aliens, bullets)

        game_functions.update_screen(ai_settings, screen, stats, sb, rocket_ship, aliens, bullets, play_button,
                                     empty_ship)


run_game()
