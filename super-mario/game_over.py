import pygame


class GameOver:
    def __init__(self, screen, game_stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_color = (0, 0, 0)  # Black

        self.go_text_color = (255, 255, 255)
        self.go_title_font = pygame.font.SysFont(None, 200)
        self.go_title_rect = pygame.Rect(0, 0, 200, 50)
        self.go_title_image = self.go_title_font.render("GAME OVER", True, self.go_text_color, self.bg_color)
        self.go_title_image_rect = self.go_title_image.get_rect()
        self.go_title_image_rect.centerx = self.screen_rect.centerx
        self.go_title_rect.top = self.screen_rect.top + 30

        # Title
        self.text_color = (255, 255, 255)       # White
        self.title_width, self.title_height = 150, 150
        self.title_font = pygame.font.SysFont(None, 120)
        self.title_rect = pygame.Rect(0, 0, self.title_width, self.title_height)
        self.title_image = self.title_font.render("High Scores", True, self.text_color, self.bg_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.top = self.screen_rect.top + 125

        # High Scores
        self.high_scores_font = pygame.font.SysFont(None, 10)
        self.high_scores = game_stats.high_scores
        self.high_scores_images = []
        self.high_scores_deltay = 10

    def draw(self):
        high_scores_rect_centery = self.screen_rect.centery
        self.screen.blit(self.go_title_image, self.go_title_image_rect)
        self.screen.blit(self.title_image, self.title_image_rect)
        for image in self.high_scores_images:
            high_scores_image_rect = image.get_rect()
            # high_scores_image_rect.centery = self.screen_rect.centery
            high_scores_image_rect.centerx = self.screen_rect.centerx
            high_scores_rect_centery += self.high_scores_deltay
            high_scores_image_rect.centery = high_scores_rect_centery
            self.screen.blit(image, high_scores_image_rect)

    def load_high_scores_images(self, game_stats):
        """Create / Update list of high_scores_images"""
        self.high_scores_images.clear()
        self.high_scores = game_stats.high_scores
        for x in range(len(self.high_scores)):
            image = self.high_scores_font.render(str(self.high_scores[x]), True, self.text_color, self.bg_color)
            self.high_scores_images.append(image)
