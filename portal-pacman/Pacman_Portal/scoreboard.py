import pygame
from pygame.sprite import Group
from pacman import PacMan


class Scoreboard:
    """A class to report score, lives, and level"""

    def __init__(self, screen, settings, game_state, ghosts, maze):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.game_state = game_state
        self.ghosts = ghosts
        self.maze = maze

        # Font(s)
        self.font = pygame.font.SysFont(None, 30)

        # Text Color(s)
        self.text_color = (255, 255, 255)   # White

        # Score
        self.score_image = self.font.render("0", True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        # Level
        self.level_image = self.font.render(str(self.game_state.level), True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        # Lives
        self.pacman_lives = Group()
        self.update()

    def draw(self):
        """Prepare next frame to draw"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Using sprite.draw from inheritance, draw pacman sprite
        self.pacman_lives.draw(self.screen)

    def update(self):
        """Update pacman_lives group, score, and level"""
        # Prep number of lives through images of Pacman
        self.pacman_lives = Group()
        for lives in range(self.game_state.lives):
            pacman_life = PacMan(self.screen, self.settings, self.game_state, self.ghosts, self.maze)
            pacman_life.image = pygame.transform.scale(pacman_life.image, (30, 30))
            pacman_life.rect.width = 30
            pacman_life.rect.height = 30
            pacman_life.rect.left = self.screen_rect.left + lives * pacman_life.rect.width
            pacman_life.rect.bottom = self.screen_rect.bottom
            self.pacman_lives.add(pacman_life)

        # Prep score
        score_str = "Score: {:,}".format(self.game_state.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.bottom = self.screen_rect.bottom

        # Prep level
        self.level_image = self.font.render(str(self.game_state.level), True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.bottom = self.screen_rect.bottom
