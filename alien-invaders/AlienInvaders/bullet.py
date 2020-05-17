import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship, alien, type_bullet):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.bullet_type = type_bullet         # 0 = from ship, 1 = from alien

        #   Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        if self.bullet_type == 0:
            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
        if self.bullet_type == 1:
            self.rect.centerx = alien.rect.centerx
            self.rect.top = alien.rect.bottom

        #   Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up/down the screen."""
        if self.bullet_type == 0:
            #   Update the decimal position of the bullet.
            self.y -= self.speed_factor
            #   Update the rect position
            self.rect.y = self.y
        if self.bullet_type == 1:
            self.y += self.speed_factor
            self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
