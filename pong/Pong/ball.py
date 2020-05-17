import pygame
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, settings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.image = pygame.image.load('images/Ball.png')
        self.rect = self.image.get_rect()
        self.left_right_direction = 1      # (-) = left, (+) = right
        self.up_down_direction = 0          # (-) = up, 0 = neutral, (+) = down
        self.reset = False

        #   Set starting location: center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw ball to screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Change ball's position"""
        self.x += self.left_right_direction
        self.y += self.up_down_direction

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def center_ball(self):
        self.x = self.screen_rect.centerx
        self.y = self.screen_rect.centery
        self.up_down_direction = 0
        self.left_right_direction = 1
