class Settings:
    def __init__(self):
        self.screen_width = 690
        self.screen_height = 795
        self.bg_color = (0, 0, 0)

        # Pacman
        self.pacman_speed = 7

        # Red Ghost
        self.red_ghost_speed = 1
        self.red_ghost_speed_delta = 0.1    # Increases red ghost's speed

        # Blue, Orange, Teal Ghost
        self.bot_ghost_speed = 1            # bot = blue, orange, teal

        # Maze Meta-Data
        self.rows = 51
        self.columns = 47

    def reset_settings(self):
        self.red_ghost_speed = 1
