import pygame
from pygame.sprite import Sprite
import random

IMAGE_SIZE = 15


class Ghost(Sprite):
    def __init__(self, screen, ghost_type, game_state):
        super(Ghost, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ghost_type = ghost_type
        self.rect = pygame.Rect(self.screen_rect.centerx, self.screen_rect.centery, 45, 45)
        self.images = []
        self.frame = 0
        self.direction = 0
        self.game_state = game_state

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        self.moving_none = False

        self.right = True
        self.left = True
        self.down = True
        self.up = True

        # Attributes for power pill
        self.vulnerable = False
        self.timer_start = False
        self.timer_beg = 0
        self.timer_stop = 0

        self.load_images()
        self.image = self.images[0][0]

        # Tracking position
        self.row = 0
        self.col = 0

        self.next_row = 0
        self.next_col = 0

    def __str__(self):
        return "Direction: " + str(self.direction) + "\nCurrent Row:"

    def update(self):
        # 1st index reference as self.direction: 0 = right, 1 = left, 2 = down, 3 = up
        # 2nd index referenced as self.frame: animation frames
        self.ai_movement()
        self.check_next()
        if not self.vulnerable:
            # print("Moving left:" + str(self.moving_left))
            # print("Moving right:" + str(self.moving_right))
            # print("Moving up:" + str(self.moving_up))
            # print("Moving down:" + str(self.moving_down) + "\n")
            # print("left:" + str(self.left))
            # print("right:" + str(self.right))
            # print("up:" + str(self.up))
            # print("down:" + str(self.down) + "\n")
            if self.right and self.moving_right:
                self.direction = 0
                self.rect.centerx += 3
            elif self.left and self.moving_left:
                self.direction = 1
                self.rect.centerx += 3
            elif self.down and self.moving_down:
                self.direction = 2
                self.rect.centery += 3
            elif self.up and self.moving_up:
                self.direction = 3
                self.rect.centery -= 3
        elif self.vulnerable:
            self.direction = 4
            time_seconds = int(pygame.time.get_ticks() / 1000)
            if time_seconds % 2 == 0:
                self.direction = 4
            elif time_seconds % 1 == 0:
                self.direction = 5
            if self.right and self.moving_right:
                self.rect.centerx += 3
            elif self.left and self.moving_left:
                self.rect.centerx += 3
            elif self.down and self.moving_down:
                self.rect.centery += 3
            elif self.up and self.moving_up:
                self.rect.centery -= 3
        time_seconds = int(pygame.time.get_ticks() / 1000)
        if time_seconds % 2 == 0:
            self.frame = 0
        elif time_seconds % 1 == 0:
            self.frame = 1
        self.image = self.images[self.direction][self.frame]

        self.row = int(self.rect.centery / 15)       # 15 = image size
        self.col = int(self.rect.centerx / 15)

        # For blue/ghost timer
        if self.timer_start:
            self.timer_beg = pygame.time.get_ticks()
            if self.timer_beg > self.timer_stop:
                self.vulnerable = False

    def draw(self):
        self.screen.blit(self.images[self.direction][self.frame], self.rect)

    def load_images(self):
        if self.ghost_type == 'red':
            self.rect.bottom = 300
            self.rect.left = 322
            red_right = list(
                (pygame.image.load("images/Ghost_Red_Right_1.bmp"),
                 pygame.image.load("images/Ghost_Red_Right_2.bmp")))
            red_left = list(
                (pygame.image.load("images/Ghost_Red_Left_1.bmp"),
                 pygame.image.load("images/Ghost_Red_Left_2.bmp")))
            red_down = list(
                (pygame.image.load("images/Ghost_Red_Down_1.bmp"),
                 pygame.image.load("images/Ghost_Red_Down_2.bmp")))
            red_up = list(
                (pygame.image.load("images/Ghost_Red_Up_1.bmp"),
                 pygame.image.load("images/Ghost_Red_Up_2.bmp")))
            self.images.append(red_right)
            self.images.append(red_left)
            self.images.append(red_down)
            self.images.append(red_up)
        elif self.ghost_type == 'pink':
            self.rect.bottom = 390              # Pen row # * brick size(15)
            self.rect.left = 270
            pink_right = list(
                (pygame.image.load("images/Ghost_Pink_Right_1.bmp"),
                 pygame.image.load("images/Ghost_Pink_Right_2.bmp")))
            pink_left = list(
                (pygame.image.load("images/Ghost_Pink_Left_1.bmp"),
                 pygame.image.load("images/Ghost_Pink_Left_2.bmp")))
            pink_down = list(
                (pygame.image.load("images/Ghost_Pink_Down_1.bmp"),
                 pygame.image.load("images/Ghost_Pink_Down_2.bmp")))
            pink_up = list(
                (pygame.image.load("images/Ghost_Pink_Up_1.bmp"),
                 pygame.image.load("images/Ghost_Pink_Up_2.bmp")))
            self.images.append(pink_right)
            self.images.append(pink_left)
            self.images.append(pink_down)
            self.images.append(pink_up)
        elif self.ghost_type == 'orange':
            self.rect.bottom = 390
            self.rect.left = 322
            orange_right = list(
                (pygame.image.load("images/Ghost_Orange_Right_1.bmp"),
                 pygame.image.load("images/Ghost_Orange_Right_2.bmp")))
            orange_left = list(
                (pygame.image.load("images/Ghost_Orange_Left_1.bmp"),
                 pygame.image.load("images/Ghost_Orange_Left_2.bmp")))
            orange_down = list(
                (pygame.image.load("images/Ghost_Orange_Down_1.bmp"),
                 pygame.image.load("images/Ghost_Orange_Down_2.bmp")))
            orange_up = list(
                (pygame.image.load("images/Ghost_Orange_Up_1.bmp"),
                 pygame.image.load("images/Ghost_Orange_Up_2.bmp")))
            self.images.append(orange_right)
            self.images.append(orange_left)
            self.images.append(orange_down)
            self.images.append(orange_up)
        elif self.ghost_type == 'teal':
            self.rect.bottom = 390
            self.rect.left = 374
            teal_right = list(
                (pygame.image.load("images/Ghost_Teal_Right_1.bmp"),
                 pygame.image.load("images/Ghost_Teal_Right_2.bmp")))
            teal_left = list(
                (pygame.image.load("images/Ghost_Teal_Left_1.bmp"),
                 pygame.image.load("images/Ghost_Teal_Left_2.bmp")))
            teal_down = list(
                (pygame.image.load("images/Ghost_Teal_Down_1.bmp"),
                 pygame.image.load("images/Ghost_Teal_Down_2.bmp")))
            teal_up = list(
                (pygame.image.load("images/Ghost_Teal_Up_1.bmp"),
                 pygame.image.load("images/Ghost_Teal_Up_2.bmp")))
            self.images.append(teal_right)
            self.images.append(teal_left)
            self.images.append(teal_down)
            self.images.append(teal_up)

        # Blue and white animation frames
        blue = list(
            (pygame.image.load("images/Blue_Ghost_1.bmp"),
             pygame.image.load("images/Blue_Ghost_2.bmp")))
        white = list(
            (pygame.image.load("images/White_Ghost_1.bmp"),
             pygame.image.load("images/White_Ghost_2.bmp")))
        self.images.append(blue)
        self.images.append(white)

        # Scale images to 45x45
        for image in self.images:
            for x in range(2):      # 2 = num of animation images
                image[x] = pygame.transform.scale(image[x], (45, 45))

    def ai_movement(self):
        new_direction_timer = int(pygame.time.get_ticks() / 10)
        if new_direction_timer % 100 == 0:
            new_direction = random.randint(0, 3)
            if new_direction == 0:
                self.reset_movement_flags()
                self.moving_right = True
            elif new_direction == 1:
                self.reset_movement_flags()
                self.moving_left = True
            elif new_direction == 2:
                self.reset_movement_flags()
                self.moving_down = True
            elif new_direction == 3:
                self.reset_movement_flags()
                self.moving_up = True

    def reset_movement_flags(self):
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def calc_next(self):
        """Dependent on Ghost's velocity,
        this will calculate the position (as a 2D index representation) Ghost will move next"""
        # self.col = int(self.rect.centerx/IMAGE_SIZE)
        # self.row = int(self.rect.centery/IMAGE_SIZE)
        if self.moving_right:
            # If Ghost is oriented right, next index will be next column, same row
            self.next_col = self.col + 1
            self.next_row = self.row
        elif self.moving_left:
            # If Ghost is oriented left, next index will be previous column, same row
            self.next_col = self.col - 1
            self.next_row = self.row
        elif self.moving_up:
            # If Ghost is oriented up, next index will be same column, previous row
            self.next_col = self.col
            self.next_row = self.row - 1
        elif self.moving_down:
            # If Ghost is oriented down, next index will be same column, next row
            self.next_col = self.col
            self.next_row = self.row + 1
        # elif self.moving_none:
            # self.next_col = self.next_col
            # self.next_row = self.next_row

    def check_next(self):
        """Checks if the next 'step' Ghost will encounter is terrain"""
        # self.col = int(self.rect.centerx/IMAGE_SIZE)
        # self.row = int(self.rect.centery/IMAGE_SIZE)
        self.calc_next()
        if self.game_state.maze_array[self.next_row][self.next_col] == 'X':
            if self.moving_right:
                self.right = False
                self.left = True
                self.up = False
                self.down = False
            elif self.moving_left:
                self.right = False
                self.left = False
                self.up = False
                self.down = False
            elif self.moving_down:
                self.right = False
                self.left = False
                self.up = False
                self.down = False
            elif self.moving_up:
                self.right = False
                self.left = False
                self.up = False
                self.down = False
            else:
                self.right = False
                self.left = False
                self.up = False
                self.down = False
        else:
            # If it's just an empty space, Ghost can move
            if self.moving_right:
                self.right = True
            elif self.moving_left:
                self.left = True
            elif self.moving_down:
                self.down = True
            elif self.moving_up:
                self.up = True
