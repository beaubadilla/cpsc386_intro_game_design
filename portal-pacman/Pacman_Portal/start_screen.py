# TODO: (Only if extra time) scalable
import pygame
from button import Button
from ghost import Ghost
from pygame.sprite import Group
from pacman import PacMan


class StartScreen:
    def __init__(self, screen, settings, game_state, maze):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.game_state = game_state
        self.maze = maze

        # Title
        self.text_color = (255, 255, 255)       # White
        self.bg_color = (0, 0, 0)               # Black
        self.title_width, self.title_height = 300, 300
        self.font = pygame.font.SysFont(None, 130)
        self.name_font = pygame.font.SysFont(None, 80)
        self.title_rect = pygame.Rect(0, 0, self.title_width, self.title_height)
        self.title_image = self.font.render("Portal Pacman", True, self.text_color, self.bg_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.top = self.screen_rect.top + 30

        # Buttons
        #   Play
        self.play_button = Button(screen, "Play", self.screen_rect.centerx, self.screen_rect.centery + 150, 200, 50)
        #   High Scores
        self.high_scores_button = Button(screen, "High Scores",
                                         self.screen_rect.centerx, self.screen_rect.centery + 250, 200, 50)

        # Animations
        #   Ghosts
        # self.time = pygame.time.get_ticks() # / 1000          # self.time = elapsed time in float(SECONDS)
        self.time_counter = 0
        self.red_ghost = Ghost(screen, 'red', game_state)
        self.pink_ghost = Ghost(screen, 'pink', game_state)
        self.orange_ghost = Ghost(screen, 'orange', game_state)
        self.teal_ghost = Ghost(screen, 'teal', game_state)
        self.ghosts = Group()
        self.ghosts.add(self.red_ghost)
        self.ghosts.add(self.pink_ghost)
        self.ghosts.add(self.orange_ghost)
        self.ghosts.add(self.teal_ghost)
        self.pacman = PacMan(screen, self.settings, self.game_state, self.ghosts, self.maze)

        #       Flags for unique animations
        self.present_red = False
        self.present_pink = False
        self.present_orange = False
        self.present_teal = False
        self.present_pacman = False

        #       Set positions
        self.red_ghost.rect.left = self.screen_rect.left
        self.pink_ghost.rect.left = self.screen_rect.left
        self.orange_ghost.rect.left = self.screen_rect.left
        self.teal_ghost.rect.left = self.screen_rect.left

        self.red_ghost.rect.centery = self.screen_rect.centery
        self.pink_ghost.rect.centery = self.screen_rect.centery
        self.orange_ghost.rect.centery = self.screen_rect.centery
        self.teal_ghost.rect.centery = self.screen_rect.centery
        self.pacman.rect.centery = self.screen_rect.centery

        #   Names
        self.red_name_image = self.name_font.render("Blinky", True, self.text_color, self.bg_color)
        self.red_name_image_rect = self.red_name_image.get_rect()
        self.red_name_image_rect.centerx = self.screen_rect.centerx
        self.red_name_image_rect.centery = self.screen_rect.centery - 100

        self.pink_name_image = self.name_font.render("Pinkey", True, self.text_color, self.bg_color)
        self.pink_name_image_rect = self.pink_name_image.get_rect()
        self.pink_name_image_rect.centerx = self.screen_rect.centerx
        self.pink_name_image_rect.centery = self.screen_rect.centery - 100

        self.orange_name_image = self.name_font.render("Clyde", True, self.text_color, self.bg_color)
        self.orange_name_image_rect = self.orange_name_image.get_rect()
        self.orange_name_image_rect.centerx = self.screen_rect.centerx
        self.orange_name_image_rect.centery = self.screen_rect.centery - 100

        self.teal_name_image = self.name_font.render("Inkey", True, self.text_color, self.bg_color)
        self.teal_name_image_rect = self.teal_name_image.get_rect()
        self.teal_name_image_rect.centerx = self.screen_rect.centerx
        self.teal_name_image_rect.centery = self.screen_rect.centery - 100

        self.red_name_active = False
        self.pink_name_active = False
        self.orange_name_active = False
        self.teal_name_active = False

    def update(self):
        half_screen = self.screen_rect.centerx
        self.time_counter += 1

        # Beginning of Ghost Introductions----------------------------------------
        if self.time_counter < 1000:
            # Present Blinky (until middle of screen)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            self.present_red = True
            self.red_name_active = True
            if self.red_ghost.rect.centerx <= half_screen:
                self.red_ghost.rect.centerx += 1
        elif 1000 < self.time_counter < 2000:
            # Move Blinky out of screen~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if self.red_ghost.rect.left < self.screen_rect.right:
                self.red_ghost.rect.centerx += 1
            else:
                self.present_red = False
                self.red_name_active = False
            # Present Pinky (until middle of screen)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            self.present_pink = True
            self.pink_name_active = True
            if self.pink_ghost.rect.centerx <= half_screen:
                self.pink_ghost.rect.centerx += 1
        elif 2000 < self.time_counter < 3000:
            # Move Pinky out of screen~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if self.pink_ghost.rect.left < self.screen_rect.right:
                self.pink_ghost.rect.centerx += 1
            else:
                self.present_pink = False
                self.pink_name_active = False
            # Present Clyde (until middle of screen)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            self.present_orange = True
            self.orange_name_active = True
            if self.orange_ghost.rect.centerx <= half_screen:
                self.orange_ghost.rect.centerx += 1
        elif 3000 < self.time_counter < 4000:
            # Move Clyde out of screen~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if self.orange_ghost.rect.left < self.screen_rect.right:
                self.orange_ghost.rect.centerx += 1
            else:
                self.present_orange = False
                self.orange_name_active = False
            # Present Inkey (until middle of screen)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            self.present_teal = True
            self.teal_name_active = True
            if self.teal_ghost.rect.centerx <= half_screen:
                self.teal_ghost.rect.centerx += 1
        elif 4000 < self.time_counter < 5500:
            # Move Inkey out of screen~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if self.teal_ghost.rect.left < self.screen_rect.right and self.present_teal:
                self.teal_ghost.rect.centerx += 1
            else:
                self.present_teal = False
                self.teal_name_active = False
        # End of Ghost Introductions-----------------------------------------------
        # Beginning of Ghosts chasing Pac-Man
                self.pacman.rect.right = self.screen_rect.left
                self.red_ghost.rect.right = self.pacman.rect.left - 50
                self.pink_ghost.rect.right = self.red_ghost.rect.left
                self.orange_ghost.rect.right = self.pink_ghost.rect.left
                self.teal_ghost.rect.right = self.orange_ghost.rect.left

                # self.powerpill.rect.right = self.screen_rect.right
        elif 5500 < self.time_counter < 6000:
            self.present_red = True
            self.present_pink = True
            self.present_orange = True
            self.present_teal = True
            self.present_pacman = True
            self.red_ghost.rect.centerx += 1
            self.pink_ghost.rect.centerx += 1
            self.orange_ghost.rect.centerx += 1
            self.teal_ghost.rect.centerx += 1
            self.pacman.rect.centerx += 1

    def draw(self):
        self.screen.blit(self.title_image, self.title_image_rect)
        self.play_button.draw_button()
        self.high_scores_button.draw_button()
        # self.ghosts.draw(self.screen)
        if self.present_red:
            self.red_ghost.draw()
            if self.red_name_active:
                self.screen.blit(self.red_name_image, self.red_name_image_rect)
        if self.present_pink:
            self.pink_ghost.draw()
            if self.pink_name_active:
                self.screen.blit(self.pink_name_image, self.pink_name_image_rect)
        if self.present_orange:
            self.orange_ghost.draw()
            if self.orange_name_active:
                self.screen.blit(self.orange_name_image, self.orange_name_image_rect)
        if self.present_teal:
            self.teal_ghost.draw()
            if self.teal_name_active:
                self.screen.blit(self.teal_name_image, self.teal_name_image_rect)
        if self.present_pacman:
            self.pacman.draw()
