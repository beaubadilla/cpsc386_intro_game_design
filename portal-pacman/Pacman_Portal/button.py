import pygame.font


class Button:
    def __init__(self, screen, msg, centerx, centery, width, height):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Button sizes
        self.width, self.height = width, height                  # 200, 50

        # Button colors
        self.button_color = (255, 255, 255)

        # Text Colors
        self.text_color = (0, 0, 0)

        # Font and font size
        self.font = pygame.font.SysFont(None, 48)

        # Create Rect object for rendering the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Render image of button(both the message and button outline)
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        # Make Rect attributes of the new rendered image accessible
        self.msg_image_rect = self.msg_image.get_rect()

        # Positioning
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.msg_image_rect.centerx = centerx
        self.msg_image_rect.centery = centery

    def draw_button(self):
        #   Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
