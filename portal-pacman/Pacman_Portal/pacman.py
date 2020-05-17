import pygame
from pygame.sprite import Sprite
import game_functions as g_f

IMAGE_SIZE = 15
MAZE_FILE = "text/pacmanportalmaze.txt"


class PacMan(Sprite):

    def __init__(self, screen, settings, game_state, ghosts, maze):
        super(PacMan, self).__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_state = game_state
        self.ghosts = ghosts
        self.maze = maze

        # Load PacMan image
        self.rect = pygame.Rect(self.screen_rect.centerx, self.screen_rect.centery, 45, 45)
        self.images = []
        self.load_images()
        self.frame_index = 0
        self.direction = 0
        self.image = pygame.image.load('images/Pacman_2.bmp')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()

        # Positioning (default 48th row)
        # y-axis = pixels 705-720
        # x-axis = centerx
        self.rect.y = 705
        self.rect.centerx = self.screen_rect.centerx

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_none = False

        # 'Next' movement flag: represents whether Pacman can move to the next expected location
        self.right = True
        self.left = True
        self.up = True
        self.down = True
        self.none = False

        # Variables to calculate Pacman's current position as a 2D array index
        self.x = self.rect.centerx
        self.y = self.rect.centery

        # Variables that hold the 2D index corresponding to PacMan's current position
        self.current_row = int(self.y/IMAGE_SIZE)
        self.current_col = int(self.x/IMAGE_SIZE)

        # Variables will hold the next 2D index dependent on current orientation of Pacman
        self.next_row = 0
        self.next_col = 0

        # Portal bullet
        self.bullet_color = (255, 255, 255)
        self.portal_bullet = pygame.Rect(0, 0, 10, 10)
        self.portal_bullet_moving = False
        self.bullet_direction = 0
        self.portal_timer = 0

    def draw(self):
        self.screen.blit(self.images[self.direction][self.frame_index], self.rect)
        if self.portal_bullet_moving:
            pygame.draw.rect(self.screen, self.bullet_color, self.portal_bullet)

    def calc_next(self):
        """Dependent on Pacman's velocity,
        this will calculate the position (as a 2D index representation) Pacman will move next"""
        if self.moving_right:
            # If Pacman is oriented right, next index will be next column, same row
            self.next_col = self.current_col + 1
            self.next_row = self.current_row
        elif self.moving_left:
            # If Pacman is oriented left, next index will be previous column, same row
            self.next_col = self.current_col - 1
            self.next_row = self.current_row
        elif self.moving_up:
            # If Pacman is oriented up, next index will be same column, previous row
            self.next_col = self.current_col
            self.next_row = self.current_row - 1
        elif self.moving_down:
            # If Pacman is oriented down, next index will be same column, next row
            self.next_col = self.current_col
            self.next_row = self.current_row + 1
        elif self.moving_none:
            self.next_col = self.next_col
            self.next_row = self.next_row

    def check_next(self):
        """Checks if the next 'step' Pacman will encounter is a pill, powerpill, portal, or terrain"""
        self.current_col = int(self.rect.centerx/IMAGE_SIZE)
        self.current_row = int(self.rect.centery/IMAGE_SIZE)

        self.calc_next()
        with open(MAZE_FILE, "r") as file:
            data = file.readlines()

        with open(MAZE_FILE, "w") as file:
            if self.game_state.maze_array[self.next_row][self.next_col] == 'X' or \
                    self.game_state.maze_array[self.next_row][self.next_col] == 'h':
                if self.moving_right:
                    self.right = False
                elif self.moving_left:
                    self.left = False
                elif self.moving_down:
                    self.down = False
                elif self.moving_up:
                    self.up = False
                else:
                    self.right = False
                    self.left = False
                    self.up = False
                    self.down = False
            elif self.game_state.maze_array[self.current_row][self.current_col] == 'p' or \
                    self.game_state.maze_array[self.current_row][self.current_col] == 'P':
                """If current position is a pill or powerpill(pseudo-collision)"""
                if self.game_state.maze_array[self.current_row][self.current_col] == 'p':
                    self.game_state.score += self.game_state.pill_point_value
                if self.game_state.maze_array[self.current_row][self.current_col] == 'P':
                    g_f.activate_power_pill(self.ghosts)

                # Update current position's 'p' to '.' in text file (writes to file on line 121 (this line + 19)
                this_lines_str = data[self.current_row]
                this_lines_str_as_list = list(this_lines_str)
                this_lines_str_as_list[self.current_col] = '.'
                change_line = ''.join(this_lines_str_as_list)
                data[self.current_row] = change_line

                # Need to update maze_array so Pacman object doesn't constantly recognize current position as 'p' still
                self.game_state.maze_array[self.current_row] = change_line
            elif self.game_state.maze_array[self.current_row][self.current_col] == 'v':
                if self.maze.portal_counter % 2 == 0:
                    self.rect.centerx = self.maze.portals[0][1] * 15
                    self.rect.centery = self.maze.portals[0][0] * 15
                else:
                    self.rect.centerx = self.maze.portals[1][1] * 15
                    self.rect.centery = self.maze.portals[1][0] * 15
            else:
                # If it's just an empty space, Pacman can move
                if self.moving_right:
                    self.right = True
                elif self.moving_left:
                    self.left = True
                elif self.moving_down:
                    self.down = True
                elif self.moving_up:
                    self.up = True

            file.writelines(data)

    def update(self):
        self.check_next()
        if self.moving_right and self.right:
            self.rect.centerx += self.settings.pacman_speed
            self.direction = 0
        elif self.moving_left and self.left:
            self.rect.centerx -= self.settings.pacman_speed
            self.direction = 1
        elif self.moving_down and self.down:
            self.rect.centery += self.settings.pacman_speed
            self.direction = 2
        elif self.moving_up and self.up:
            self.rect.centery -= self.settings.pacman_speed
            self.direction = 3
        else:
            self.rect.centerx += 0
            self.rect.centery += 0
        time_seconds = int(pygame.time.get_ticks() / 1000)
        if time_seconds % 2 == 0:
            self.frame_index = 0
        elif time_seconds % 1 == 0:
            self.frame_index = 1

        # Portal movement
        if self.portal_bullet_moving:
            if self.bullet_direction == 0:
                self.portal_bullet.centerx += 10
            elif self.bullet_direction == 1:
                self.portal_bullet.centerx -= 10
            elif self.bullet_direction == 2:
                self.portal_bullet.centery += 10
            elif self.bullet_direction == 3:
                self.portal_bullet.centery -= 10
            self.check_portal_bullet()
        # self.portal_timer_ends()

    def reset_flags(self):
        self.right = False
        self.left = False
        self.down = False
        self.up = False

    def load_images(self):
        pacman_right = list((pygame.image.load("images/Pacman_Right_1.bmp"),
                             pygame.image.load("images/Pacman_Right_2.bmp")))
        pacman_left = list((pygame.image.load("images/Pacman_Left_1.bmp"),
                            pygame.image.load("images/Pacman_Left_2.bmp")))
        pacman_up = list((pygame.image.load("images/Pacman_Up_1.bmp"),
                          pygame.image.load("images/Pacman_Up_2.bmp")))
        pacman_down = list((pygame.image.load("images/Pacman_Down_1.bmp"),
                            pygame.image.load("images/Pacman_Down_2.bmp")))
        pacman_death = list((pygame.image.load("images/Pacman_Death_2.bmp"),
                             pygame.image.load("images/Pacman_Death_3.bmp"),
                             pygame.image.load("images/Pacman_Death_4.bmp"),
                             pygame.image.load("images/Pacman_Death_5.bmp"),
                             pygame.image.load("images/Pacman_Death_6.bmp"),
                             pygame.image.load("images/Pacman_Death_7.bmp"),
                            pygame.image.load("images/Pacman_Death_8.bmp"),
                             pygame.image.load("images/Pacman_Death_9.bmp"),
                             pygame.image.load("images/Pacman_Death_10.bmp"),
                             pygame.image.load("images/Pacman_Death_11.bmp")))
        self.images.append(pacman_right)
        self.images.append(pacman_left)
        self.images.append(pacman_down)
        self.images.append(pacman_up)
        self.images.append(pacman_death)

        for image in self.images:
            for x in range(2):      # num of animation images
                image[x] = pygame.transform.scale(image[x], (45, 45))

    def shoot_portal(self):
        self.portal_bullet.centerx = self.rect.centerx
        self.portal_bullet.centery = self.rect.centery
        self.portal_bullet_moving = True
        self.bullet_direction = self.direction
        self.portal_timer = pygame.time.get_ticks() + 8000

    def check_portal_bullet(self):
        current_bullet_col = int(self.portal_bullet.centerx / IMAGE_SIZE)
        current_bullet_row = int(self.portal_bullet.centery / IMAGE_SIZE)

        # self.calc_next()
        with open(MAZE_FILE, "r") as file:
            data = file.readlines()

        with open(MAZE_FILE, "w") as file:
            if self.game_state.maze_array[current_bullet_row][current_bullet_col] == 'X' or \
                    self.game_state.maze_array[current_bullet_row][current_bullet_col] == 'h':
                self.maze.portal_counter += 1
                # Change 'X' to 'v' in the maze file to draw the portal image instead of brick
                this_lines_str = data[current_bullet_row]
                this_lines_str_as_list = list(this_lines_str)   # Change str into list to be able to change value
                if self.maze.portal_counter % 2 == 0:
                    this_lines_str_as_list[current_bullet_col] = 'v'
                else:
                    this_lines_str_as_list[current_bullet_col] = 'h'
                change_line = ''.join(this_lines_str_as_list)
                data[current_bullet_row] = change_line

                # Need to update maze_array so Pacman object doesn't constantly recognize current position as 'p'
                self.game_state.maze_array[current_bullet_row] = change_line

                self.portal_bullet_moving = False

                if self.maze.portal_counter == 1:
                    self.maze.portals.append(list((current_bullet_row, current_bullet_col)))
                elif self.maze.portal_counter == 2:
                    self.maze.portals.append(list((current_bullet_row, current_bullet_col)))
                elif self.maze.portal_counter > 2:
                    # Change "oldest" portal made back into a brick
                    portal_to_brick_str = data[self.maze.portals[0][0]]
                    portal_to_brick_str_as_list = list(portal_to_brick_str)
                    portal_to_brick_str_as_list[self.maze.portals[0][1]] = 'X'
                    new_line = ''.join(portal_to_brick_str_as_list)
                    data[self.maze.portals[0][0]] = new_line

                    # Make list act as a queue by "pushing" out oldest portal and pushing each index
                    self.maze.portals[0][0] = self.maze.portals[1][0]
                    self.maze.portals[0][1] = self.maze.portals[1][1]
                    self.maze.portals[1][0] = current_bullet_row
                    self.maze.portals[1][1] = current_bullet_col
            file.writelines(data)

    def center(self):
        self.rect.y = 705
        self.rect.centerx = self.screen_rect.centerx

    def reset_movement_flags(self):
        self.moving_left = False
        self.moving_right = False
        self.moving_down = False
        self.moving_up = False

    # Attempt to make portals temporary. portal_counter causing issues with maze.portals[][]
    # def portal_timer_ends(self):
    #     if len(self.maze.portals) > 0:
    #         now = pygame.time.get_ticks()
    #         with open(MAZE_FILE, "r") as file:
    #             data = file.readlines()
    #         with open(MAZE_FILE, "w") as file:
    #             if now >= self.portal_timer:
    #                 portal_to_brick_str = data[self.maze.portals[0][0]]
    #                 portal_to_brick_str_as_list = list(portal_to_brick_str)
    #                 portal_to_brick_str_as_list[self.maze.portals[0][1]] = 'X'
    #                 new_line = ''.join(portal_to_brick_str_as_list)
    #                 data[self.maze.portals[0][0]] = new_line
    #                 self.maze.portals.pop()
    #             file.writelines(data)
