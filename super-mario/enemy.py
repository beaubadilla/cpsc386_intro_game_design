import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """A class to represent a single enemy"""

    def __init__(self, screen, images, enemy_type, left_limit, right_limit, start_position):
        """Initialize the enemy, and set its starting position."""
        super(Enemy, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.images = images
        self.type = enemy_type
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.start_position = start_position

        # load the enemy image and set the starting position for each enemy
        if self.type == 1:
            self.image = pygame.transform.scale(images[0], (32, 32))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.start_position
            self.rect.bottom = self.screen_rect.bottom - 50
        elif self.type == 2:
            self.image = pygame.transform.scale(images[0], (32, 48))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.start_position
            self.rect.bottom = self.screen_rect.bottom - 49

        self.x_velocity = -1
        self.frame = 0
        self.dead_frames = 0
        self.dead = False
        
    def reset(self):
        """Return True if enemy is at edge of screen."""
        if self.type == 1:
            self.rect.centerx = self.start_position
            self.rect.bottom = self.screen_rect.bottom - 50
        elif self.type == 2:
            self.rect.centerx = self.start_position
            self.rect.bottom = self.screen_rect.bottom - 49
        
    def update(self):
        """Move the enemy right or left."""
        if not self.dead:
            if self.rect.left <= self.left_limit:
                self.x_velocity = 1
            elif self.rect.right > self.right_limit:
                self.x_velocity = -1
            self.rect.centerx += self.x_velocity

    def blitme(self):
        """Draw the enemy at its current location."""
        # checks if enemy is dead and display's dead enemy image if available
        if self.dead and self.type == 1:
            self.dead_frames += 1
            self.image = pygame.transform.scale(self.images[2], (32, 16))
            self.rect.bottom = self.screen_rect.bottom - 34
            if self.dead_frames > 20:
                self.kill()

        elif self.dead and self.type == 2:
            self.image = pygame.transform.scale(self.images[9], (28, 24))
            x = self.rect.centerx
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.bottom = self.screen_rect.bottom - 50

        else:
            # frame timer
            self.frame += 1
            if self.frame >= 20:
                self.frame = 0

            # changes the enemy image depending on the timer (animation)
            if self.type == 1:
                self.image = pygame.transform.scale(self.images[int(self.frame / 10)], (32, 32))
            elif self.type == 2:
                # checks if enemy is walking to the left and sets its image to the left-looking image
                if self.x_velocity == -1:
                    self.image = pygame.transform.scale(self.images[int(self.frame / 10) + 2], (32, 48))
                else:
                    self.image = pygame.transform.scale(self.images[int(self.frame / 10) + 4], (32, 48))

        self.screen.blit(self.image, self.rect)

    def __str__(self):
        return "This is a " + self.type + "\t Current Position(center): " + str(self.rect.center)
