import pygame.font


class Scoreboard:
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        #   Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.ai_score = self.stats.ai_score
        self.ai_score_str = "{:,}".format(self.ai_score)
        self.ai_score_image = self.font.render(self.ai_score_str, True, self.text_color, self.settings.bg_color)
        self.ai_score_rect = self.ai_score_image.get_rect()

        self.user_score = self.stats.user_score
        self.user_score_str = "{:,}".format(self.user_score)
        self.user_score_image = self.font.render(self.user_score_str, True, self.text_color, self.settings.bg_color)
        self.user_score_rect = self.user_score_image.get_rect()

        score_win = self.stats.score_win
        score_win_str = "{:,}".format(score_win)
        self.score_win_image = self.font.render(score_win_str, True, self.text_color, self.settings.bg_color)
        self.score_win_rect = self.score_win_image.get_rect()

        #   Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Refactoring purposes."""
        #   AI's score
        self.ai_score = self.stats.ai_score
        self.ai_score_str = "{:,}".format(self.ai_score)
        self.ai_score_image = self.font.render(self.ai_score_str, True, self.text_color, self.settings.bg_color)
        self.ai_score_rect.top = self.screen_rect.top
        self.ai_score_rect.right = self.screen_rect.centerx - 20

        #   User' Score
        self.user_score = self.stats.user_score
        self.user_score_str = "{:,}".format(self.user_score)
        self.user_score_image = self.font.render(self.user_score_str, True, self.text_color, self.settings.bg_color)
        self.user_score_rect.top = self.screen_rect.top
        self.user_score_rect.left = self.screen_rect.centerx + 20

        #   Score to win
        self.score_win_rect.top = self.user_score_rect.bottom
        self.score_win_rect.centerx = self.screen_rect.centerx

    def show_score(self):
        self.screen.blit(self.ai_score_image, self.ai_score_rect)
        self.screen.blit(self.user_score_image, self.user_score_rect)
        self.screen.blit(self.score_win_image, self.score_win_rect)
