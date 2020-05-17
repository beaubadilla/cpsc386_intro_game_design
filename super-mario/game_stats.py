class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self):
        """Initialize statistics."""
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False

        self.lives_left = 1
        self.score = 0
        self.level = 1
        self.coins = 0
        self.high_scores = []

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.score = 0
        self.level = 1
        self.coins = 0
