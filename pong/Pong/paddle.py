import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    def __init__(self, settings, screen, position):
        super(Paddle, self).__init__()

        #   Declare self attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.position = position
        self.up_flag = False
        self.down_flag = False
        self.left_flag = False
        self.right_flag = False

        # Default definition to create variable inside __init__ (avoid Pycharm error)
        self.image = pygame.image.load('images/left_right_Paddle.png')

        self.load_image()

        # Code placed here because it has to be after self.image is initialized, but before placing starting location
        self.rect = self.image.get_rect()

        self.set_starting_position()

    def blitme(self):
        """Draw paddle at location based off rect attributes"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Change paddle's position"""
        if self.up_flag and self.rect.top > 0:
            self.rect.centery -= self.settings.paddle_speed_factor
        if self.down_flag and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.paddle_speed_factor
        if self.left_flag and self.rect.left > 0:
            if (self.position == 'right-top' or self.position == 'right-bottom') and self.rect.left <= 600:
                self.rect.centerx -= 0
            else:
                self.rect.centerx -= self.settings.paddle_speed_factor
        if self.right_flag and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.paddle_speed_factor

    def load_image(self):
        """Refactoring purposes. Relieves _init__ of this block"""
        if self.position == 'left-middle':
            self.image = pygame.image.load('images/left_right_Paddle.png')
        elif self.position == 'left-top':
            self.image = pygame.image.load('images/top_bot_Paddle.png')
        elif self.position == 'left-bottom':
            self.image = pygame.image.load('images/top_bot_Paddle.png')
        elif self.position == 'right-middle':
            self.image = pygame.image.load('images/left_right_Paddle.png')
        elif self.position == 'right-top':
            self.image = pygame.image.load('images/top_bot_Paddle.png')
        elif self.position == 'right-bottom':
            self.image = pygame.image.load('images/top_bot_Paddle.png')

    def set_starting_position(self):
        """Refactoring purposes. Relieves _init__ of this block"""
        if self.position == 'left-middle':
            self.rect.left = self.screen_rect.left
            self.rect.y = self.screen_rect.centery
        elif self.position == 'left-top':
            # One-fourth of the screen width towards the left
            self.rect.center = ((self.settings.screen_width/4), 0)
        elif self.position == 'left-bottom':
            self.rect.center = ((self.settings.screen_width/4), self.settings.screen_height)
        elif self.position == 'right-middle':
            self.rect.right = self.screen_rect.right
            self.rect.y = self.screen_rect.centery
        elif self.position == 'right-top':
            # Three-fourths of the screen width toward the right
            self.rect.center = (((self.settings.screen_width * 3) / 4), 0)
        elif self.position == 'right-bottom':
            self.rect.center = (((self.settings.screen_width * 3) / 4), self.settings.screen_height)
