import pygame
from pygame.sprite import Sprite


class Bunker(Sprite):
    def __init__(self, screen):
        super(Bunker, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bunker_images = []
        self.load_bunker_images()
        self.rect = pygame.Rect((0, 0), (80, 60))
        self.index = 0
        self.image = self.bunker_images[self.index]

    def update(self):
        self.image = self.bunker_images[self.index]

    def load_bunker_images(self):
        """Load images for bunker animation"""
        self.bunker_images.append(pygame.image.load('images/Bunker1.1.bmp'))
        self.bunker_images.append(pygame.image.load('images/Bunker1.2.bmp'))
        self.bunker_images.append(pygame.image.load('images/Bunker1.3.bmp'))
        self.bunker_images.append(pygame.image.load('images/Bunker1.4.bmp'))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
