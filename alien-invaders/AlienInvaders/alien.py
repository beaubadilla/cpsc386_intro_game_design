import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen, type_alien):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.type = type_alien
        self.alien_images = []
        self.load_alien_images()
        self.index = 0
        self.image = self.alien_images[self.index]  # Default
        self.frame_counter = 0
        self.will_fire = False
        self.rect = self.alien_images[0].get_rect()

        #   Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #   Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.frame_counter += 1
        if self.frame_counter <= 120:
            self.index = 0
        elif self.frame_counter <= 240:
            self.index = 1
        else:
            self.frame_counter = 0
        #   Change picture for animation
        if self.type != 4:
            self.image = self.alien_images[self.index]
            self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        else:
            self.x += self.ai_settings.ufo_speed_factor
        self.rect.x = self.x

    def load_alien_images(self):
        if self.type == 1:
            self.alien_images.append(pygame.image.load('images/Alien1.1.bmp'))
            self.alien_images.append(pygame.image.load('images/Alien1.2.bmp'))
        elif self.type == 2:
            self.alien_images.append(pygame.image.load('images/Alien2.1.bmp'))
            self.alien_images.append(pygame.image.load('images/Alien2.2.bmp'))
        elif self.type == 3:
            self.alien_images.append(pygame.image.load('images/Alien3.1.bmp'))
            self.alien_images.append(pygame.image.load('images/Alien3.2.bmp'))
        elif self.type == 4:
            self.alien_images.append(pygame.image.load('images/Alien4.bmp'))
