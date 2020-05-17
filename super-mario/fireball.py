# Need limit on num_fireballs (2); probably place in stats
from pygame.sprite import Sprite
import pygame


class Fireball(Sprite):
    def __init__(self, screen):
        super(Fireball, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect((0, 0), (10, 10))

        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        self.color = (255, 0, 0)

        self.x_velocity = 5
        self.y_velocity = 3

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += self.x_velocity
        elif self.moving_left:
            self.rect.centerx -= self.x_velocity

    def draw_fireball(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, 5)
        # pygame.draw.rect(self.screen, self.color, self.rect)
