# Need back button
import pygame
from button import Button


class HighScoreScreen:
    def __init__(self, screen, game_state):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Title
        self.text_color = (255, 255, 255)       # White
        self.bg_color = (0, 0, 0)               # Black
        self.title_width, self.title_height = 300, 300
        self.title_font = pygame.font.SysFont(None, 150)
        self.title_rect = pygame.Rect(0, 0, self.title_width, self.title_height)
        self.title_image = self.title_font.render("High Scores", True, self.text_color, self.bg_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.top = self.screen_rect.top + 30

        # High Scores
        self.high_scores_font = pygame.font.SysFont(None, 100)
        self.high_scores = game_state.high_scores
        self.high_scores_images = []
        self.high_scores_deltay = 75

        # Buttons
        # Back (to start screen)
        # Position top left
        self.back_button = Button(screen, "Back", 0, 0, 100, 40)
        self.back_button.msg_image_rect.top = self.screen_rect.top
        self.back_button.msg_image_rect.left = self.screen_rect.left
        self.back_button.rect.top = self.screen_rect.top
        self.back_button.rect.left = self.screen_rect.left

    def draw(self):
        high_scores_rect_centery = self.screen_rect.centery - 150
        self.screen.blit(self.title_image, self.title_image_rect)
        self.back_button.draw_button()
        for image in self.high_scores_images:
            high_scores_image_rect = image.get_rect()
            # high_scores_image_rect.centery = self.screen_rect.centery
            high_scores_image_rect.centerx = self.screen_rect.centerx
            high_scores_rect_centery += self.high_scores_deltay
            high_scores_image_rect.centery = high_scores_rect_centery
            self.screen.blit(image, high_scores_image_rect)

    def load_high_scores_images(self, game_state):
        """Create / Update list of high_scores_images"""
        self.high_scores_images.clear()
        self.high_scores = game_state.high_scores
        for x in range(len(self.high_scores)):
            image = self.high_scores_font.render(str(self.high_scores[x]), True, self.text_color, self.bg_color)
            self.high_scores_images.append(image)
