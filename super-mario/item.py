import pygame
from pygame.sprite import Sprite


class Item(Sprite):
    """A class to represent a single enemy"""

    def __init__(self, screen, images, item_type):
        """Initialize the enemy, and set its starting position."""
        super(Item, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.images = images
        self.type = item_type

        self.animation_px_ctr = 0

        # load the enemy image and set the starting position for each enemy
        # powerup mushroom
        if self.type == 1:
            self.image = pygame.transform.scale(images[0], (32, 32))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screen_rect.left + 200
            self.rect.bottom = self.screen_rect.bottom - 50
        # fire flower
        elif self.type == 2:
            self.image = pygame.transform.scale(images[0], (32, 32))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screen_rect.left + 300
            self.rect.bottom = self.screen_rect.bottom - 50
        # star
        elif self.type == 3:
            self.image = pygame.transform.scale(images[0], (32, 32))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screen_rect.left + 400
            self.rect.bottom = self.screen_rect.bottom - 50
        elif self.type == 4:
            self.image = pygame.transform.scale(images[0], (32, 32))
            self.rect = self.image.get_rect()

        self.frame = 0

    def blitme(self):
        """Draw the enemy at its current location."""
        # frame timer
        self.frame += 1
        if self.frame >= 40:
            self.frame = 0

        # changes the enemy image depending on the timer (animation)
        if self.type == 2 or self.type == 3:
            self.image = pygame.transform.scale(self.images[int(self.frame / 10)], (32, 32))

        self.screen.blit(self.image, self.rect)

    def __str__(self):
        return "This is a " + str(self.type) + "\t Current Position(center): " + str(self.rect.center)

    def transform_images(self):
        ctr = 0
        for image in self.images:
            img = pygame.transform.scale(image, (30, 30))
            self.images[ctr] = img
            ctr += 1
