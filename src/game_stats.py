class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.rocket_ships_left = self.ai_settings.rocket_ship_limit
        self.score = 0
        self.level = 1
