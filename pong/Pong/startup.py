import pygame.font


class Menu:
    def __init__(self, screen, settings,  title, subtitle):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 300, 300
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.bg_color = settings.bg_color

        self.title_rect = pygame.Rect(0, 0, self.width, self.height)
        self.title_image = self.font.render(title, True, self.text_color, self.bg_color)
        self.title_image_rect = self.title_image.get_rect()

        self.subtitle_rect = pygame.Rect(0, 0, self.width, self.height)
        self.subtitle_image = self.font.render(subtitle, True, self.text_color, self.bg_color)
        self.subtitle_image_rect = self.title_image.get_rect()

        self.prep_title()
        self.prep_subtitle()

    def prep_title(self):
        """Place title at the top of the screen, centered"""
        self.title_image_rect.top = self.screen_rect.top
        self.title_image_rect.centerx = self.screen_rect.centerx

    def draw_title(self):
        self.screen.fill(self.bg_color, self.title_rect)
        self.screen.blit(self.title_image, self.title_image_rect)

    def prep_subtitle(self):
        """Place subtitle right below title"""
        self.subtitle_image_rect.top = self.title_image_rect.bottom
        self.subtitle_image_rect.centerx = self.screen_rect.centerx

    def draw_subtitle(self):
        self.screen.fill(self.bg_color, self.subtitle_rect)
        self.screen.blit(self.subtitle_image, self.subtitle_image_rect)
