import pygame.font


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        
        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_coins()
        self.prep_level()
        self.prep_time()
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_num = self.font.render(score_str, True, self.text_color, (107, 140, 255))
        self.score_image = self.font.render("SCORE", True, self.text_color, (107, 140, 255))
            
        # Display the score at the top left of the screen.
        self.score_num_rect = self.score_num.get_rect()
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.centerx = (self.screen_rect.right / 6)
        self.score_image_rect.top = 0
        self.score_num_rect.centerx = self.score_image_rect.centerx
        self.score_num_rect.top = self.score_image_rect.bottom
        
    def prep_coins(self):
        """Show how many coins are left"""
        coins = int(round(self.stats.coins, -1))
        coins_str = "{:,}".format(coins)
        self.coins_num = self.font.render(coins_str, True, self.text_color, (107, 140, 255))
        self.coins_image = self.font.render("COINS", True, self.text_color, (107, 140, 255))

        # Align the coins at the top of the screen.
        self.coins_num_rect = self.coins_num.get_rect()
        self.coins_image_rect = self.coins_image.get_rect()
        self.coins_image_rect.centerx = (self.screen_rect.right / 6) * 2
        self.coins_image_rect.top = 0
        self.coins_num_rect.centerx = self.coins_image_rect.centerx
        self.coins_num_rect.top = self.coins_image_rect.bottom
        
    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_num = self.font.render(str(self.stats.level), True,
                self.text_color, (107, 140, 255))
        self.level_image = self.font.render("WORLD", True, self.text_color, (107, 140, 255))

        # Align the level at the top of the screen.
        self.level_num_rect = self.level_num.get_rect()
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.centerx = (self.screen_rect.right / 6) * 3
        self.level_image_rect.top = 0
        self.level_num_rect.centerx = self.level_image_rect.centerx
        self.level_num_rect.top = self.level_image_rect.bottom

    def prep_time(self):
        """Turn the level into a rendered image."""
        self.time_num = self.font.render(str(int(pygame.time.get_ticks()/1000)), True,
                self.text_color, (107, 140, 255))
        self.time_image = self.font.render("TIME", True, self.text_color, (107, 140, 255))

        # Center the high score at the top of the screen.
        self.time_num_rect = self.time_num.get_rect()
        self.time_image_rect = self.time_image.get_rect()
        self.time_image_rect.centerx = (self.screen_rect.right / 6) * 4
        self.time_image_rect.top = 0
        self.time_num_rect.centerx = self.time_image_rect.centerx
        self.time_num_rect.top = self.time_image_rect.bottom

    def prep_lives(self):
        """Show how many lives are left."""
        self.lives_num = self.font.render(str(self.stats.lives_left), True,
                self.text_color, (107, 140, 255))
        self.lives_image = self.font.render("LIVES", True, self.text_color, (107, 140, 255))

        # Center the high score at the top of the screen.
        self.lives_num_rect = self.lives_num.get_rect()
        self.lives_image_rect = self.lives_image.get_rect()
        self.lives_image_rect.centerx = (self.screen_rect.right / 6) * 5
        self.lives_image_rect.top = 0
        self.lives_num_rect.centerx = self.lives_image_rect.centerx
        self.lives_num_rect.top = self.lives_image_rect.bottom

    def refresh_time(self):
        self.time_num = self.font.render(str(int(pygame.time.get_ticks()/1000)), True,
                self.text_color, (107, 140, 255))

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.score_num, self.score_num_rect)
        self.screen.blit(self.coins_image, self.coins_image_rect)
        self.screen.blit(self.coins_num, self.coins_num_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.screen.blit(self.level_num, self.level_num_rect)
        self.screen.blit(self.time_image, self.time_image_rect)
        self.screen.blit(self.time_num, self.time_num_rect)
        self.screen.blit(self.lives_image, self.lives_image_rect)
        self.screen.blit(self.lives_num, self.lives_num_rect)
