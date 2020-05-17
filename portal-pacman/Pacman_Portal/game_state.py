class GameState:
    def __init__(self):
        self.game_active = False
        self.high_score_screen = False
        self.start_screen = True

        self.score = 0
        self.lives = 3
        self.level = 1
        self.high_score = 0
        self.high_scores = []

        self.maze_array = []

        self.pill_point_value = 50

    def reset_stats(self):
        self.score = 0
        self.lives = 3
        self.level = 1
