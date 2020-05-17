# Create hi-score by instantiating a button class
# Refactoring Idea: Try using only one self.Text_image and self.Text_image_rect like
# Line 42: self.alien_rect
import pygame.font


class StartScreen:
    def __init__(self, screen, ai_settings, title1, title2):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.alien_frame_ctr = 0

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Title~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
        # Title settings
        self.text_color1 = (255, 255, 255)    # White
        self.text_color2 = (0, 255, 0)  # Green
        self.bg_color = ai_settings.bg_color
        self.width, self.height = 300, 300
        self.font = pygame.font.SysFont(None, 150)

        # Create a Rect object for each title
        self.title1_rect = pygame.Rect(0, 0, self.width, self.height)
        self.title2_rect = pygame.Rect(0, 0, self.width, self.height)

        # Create the image (to blit())
        # .render(text, antialiasing, textColor, backgroundColor)
        self.title1_image = self.font.render(title1, True, self.text_color1, self.bg_color)
        self.title2_image = self.font.render(title2, True, self.text_color2, self.bg_color)

        # Make the Rect attributes accessible
        self.title1_image_rect = self.title1_image.get_rect()
        self.title2_image_rect = self.title2_image.get_rect()

        # Position the titles
        self.title1_image_rect.centerx = self.screen_rect.centerx
        self.title1_image_rect.top = self.screen_rect.top
        self.title2_image_rect.centerx = self.screen_rect.centerx
        self.title2_image_rect.top = self.title1_image_rect.bottom

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Aliens~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
        # Create the image to blit()
        self.alien1_1_image = pygame.image.load('images/Alien1.1.bmp')
        self.alien1_2_image = pygame.image.load('images/Alien1.2.bmp')
        self.alien2_1_image = pygame.image.load('images/Alien2.1.bmp')
        self.alien2_2_image = pygame.image.load('images/Alien2.2.bmp')
        self.alien3_1_image = pygame.image.load('images/Alien3.1.bmp')
        self.alien3_2_image = pygame.image.load('images/Alien3.2.bmp')
        self.alien4_image = pygame.image.load('images/Alien4.bmp')

        # Make the Rect attributes accessible
        self.alien1_1_image_rect = self.alien1_1_image.get_rect()
        self.alien1_2_image_rect = self.alien1_1_image.get_rect()
        self.alien2_1_image_rect = self.alien1_1_image.get_rect()
        self.alien2_2_image_rect = self.alien1_1_image.get_rect()
        self.alien3_1_image_rect = self.alien1_1_image.get_rect()
        self.alien3_2_image_rect = self.alien1_1_image.get_rect()
        self.alien4_image_rect = self.alien1_1_image.get_rect()

        # Position aliens
        # X
        self.alien1_1_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien1_2_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien2_1_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien2_2_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien3_1_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien3_2_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien4_image_rect.centerx = self.screen_rect.centerx - 100
        # Y
        self.alien1_1_image_rect.centery = self.screen_rect.centery
        self.alien1_2_image_rect.centery = self.screen_rect.centery
        self.alien2_1_image_rect.centery = self.screen_rect.centery + 90
        self.alien2_2_image_rect.centery = self.screen_rect.centery + 90
        self.alien3_1_image_rect.centery = self.screen_rect.centery + 180
        self.alien3_2_image_rect.centery = self.screen_rect.centery + 180
        self.alien4_image_rect.centery = self.screen_rect.centery + 270

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Alien Values~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
        self.text_color_alien_values = (255, 255, 255)
        self.width_alien_values, self.height_alien_values = 60, 60
        self.font = pygame.font.SysFont(None, 40)

        self.av1_rect = pygame.Rect(0, 0, self.width_alien_values, self.height_alien_values)
        self.av1_image = self.font.render("= 20", True, self.text_color_alien_values, self.bg_color)
        self.av1_image_rect = self.av1_image.get_rect()
        self.av1_image_rect.centerx = self.alien1_1_image_rect.centerx + 60
        self.av1_image_rect.centery = self.alien1_1_image_rect.centery

        self.av2_rect = pygame.Rect(0, 0, self.width_alien_values, self.height_alien_values)
        self.av2_image = self.font.render("= 40", True, self.text_color_alien_values, self.bg_color)
        self.av2_image_rect = self.av2_image.get_rect()
        self.av2_image_rect.centerx = self.alien2_1_image_rect.centerx + 60
        self.av2_image_rect.centery = self.alien2_1_image_rect.centery

        self.av3_rect = pygame.Rect(0, 0, self.width_alien_values, self.height_alien_values)
        self.av3_image = self.font.render("= 60", True, self.text_color_alien_values, self.bg_color)
        self.av3_image_rect = self.av3_image.get_rect()
        self.av3_image_rect.centerx = self.alien3_1_image_rect.centerx + 60
        self.av3_image_rect.centery = self.alien3_1_image_rect.centery

        self.av4_rect = pygame.Rect(0, 0, self.width_alien_values, self.height_alien_values)
        self.av4_image = self.font.render("= ?", True, self.text_color_alien_values, self.bg_color)
        self.av4_image_rect = self.av1_image.get_rect()
        self.av4_image_rect.centerx = self.alien4_image_rect.centerx + 180
        self.av4_image_rect.centery = self.alien4_image_rect.centery

    def draw_start_screen(self):
        # Draw Titles
        self.screen.fill(self.bg_color, self.title1_rect)
        self.screen.blit(self.title1_image, self.title1_image_rect)
        self.screen.fill(self.bg_color, self.title2_rect)
        self.screen.blit(self.title2_image, self.title2_image_rect)

        # Draw alien (score) values
        self.screen.fill(self.bg_color, self.title1_rect)
        self.screen.blit(self.alien4_image, self.alien4_image_rect)
        self.screen.fill(self.bg_color, self.title1_rect)
        self.screen.blit(self.av1_image, self.av1_image_rect)
        self.screen.fill(self.bg_color, self.title1_rect)
        self.screen.blit(self.av2_image, self.av2_image_rect)
        self.screen.fill(self.bg_color, self.title1_rect)
        self.screen.blit(self.av3_image, self.av3_image_rect)
        self.screen.fill(self.bg_color, self.title1_rect)
        self.screen.blit(self.av4_image, self.av4_image_rect)

        # Draw and animate aliens
        self.alien_frame_ctr += 1
        if self.alien_frame_ctr <= 60:
            # Draw first frame of each alien
            self.screen.blit(self.alien1_1_image, self.alien1_1_image_rect)
            self.screen.blit(self.alien2_1_image, self.alien2_1_image_rect)
            self.screen.blit(self.alien3_1_image, self.alien3_1_image_rect)
        elif 60 < self.alien_frame_ctr <= 120:
            # Draw second frame of each alien
            self.screen.blit(self.alien1_2_image, self.alien1_2_image_rect)
            self.screen.blit(self.alien2_2_image, self.alien2_2_image_rect)
            self.screen.blit(self.alien3_2_image, self.alien3_2_image_rect)
        else:
            self.alien_frame_ctr = 0
