import sys              # for checking events
import pygame
# from time import sleep


def check_events(paddle_right_mid, paddle_right_top, paddle_right_bottom, play_button, stats, sb):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle_right_mid, paddle_right_top, paddle_right_bottom)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle_right_mid, paddle_right_top, paddle_right_bottom)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, sb, play_button, mouse_x, mouse_y)


def check_keydown_events(event, paddle_right_mid, paddle_right_top, paddle_right_bottom):
    if event.key == pygame.K_UP:
        paddle_right_mid.up_flag = True
    elif event.key == pygame.K_DOWN:
        paddle_right_mid.down_flag = True
    elif event.key == pygame.K_LEFT:
        paddle_right_top.left_flag = True
        paddle_right_bottom.left_flag = True
    elif event.key == pygame.K_RIGHT:
        paddle_right_top.right_flag = True
        paddle_right_bottom.right_flag = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, paddle_right_mid, paddle_right_top, paddle_right_bottom):
    if event.key == pygame.K_UP:
        paddle_right_mid.up_flag = False
    elif event.key == pygame.K_DOWN:
        paddle_right_mid.down_flag = False
    elif event.key == pygame.K_LEFT:
        paddle_right_top.left_flag = False
        paddle_right_bottom.left_flag = False
    elif event.key == pygame.K_RIGHT:
        paddle_right_top.right_flag = False
        paddle_right_bottom.right_flag = False


def prep_screen(settings, screen,
                paddle_left_mid, paddle_left_top, paddle_left_bottom,
                paddle_right_mid, paddle_right_top, paddle_right_bottom, ball, play_button, stats, sb, menu
                ):
    """Draws each object after they have been updated"""
    screen.fill(settings.bg_color)
    #   All 'blitme'/'draw'
    if not stats.game_active:
        play_button.draw_button()
        # menu.prep_title()
        # menu.prep_subtitle()
        menu.draw_title()
        menu.draw_subtitle()
    else:
        pygame.draw.rect(screen, (255, 255, 255), [600, 0, 1, 800], 1)  # Half line
        paddle_left_mid.blitme()
        paddle_left_top.blitme()
        paddle_left_bottom.blitme()
        paddle_right_mid.blitme()
        paddle_right_top.blitme()
        paddle_right_bottom.blitme()
        ball.blitme()
        sb.prep_score()
        sb.show_score()


def update_paddles(paddle_left_mid, paddle_left_top, paddle_left_bottom,
                   paddle_right_mid, paddle_right_top, paddle_right_bottom):
    """Refactoring purposes. To make only one call to update all paddles in main"""
    paddle_left_mid.update()
    paddle_left_top.update()
    paddle_left_bottom.update()
    paddle_right_mid.update()
    paddle_right_top.update()
    paddle_right_bottom.update()


def check_dead_ball(screen, ball, stats):
    """Checks if the ball has gone out the screen. If so, reset the ball to the middle"""
    screen_rect = screen.get_rect()

    #   If ball passes left side of screen
    if ball.rect.right < screen_rect.left:
        ball.center_ball()
        ball.reset = True
        stats.user_score += 1
    #   If ball passes top side of screen
    elif ball.rect.bottom < screen_rect.top:
        ball.center_ball()
        ball.reset = True
        if ball.rect.centerx < screen_rect.centerx:
            stats.user_score += 1
        else:
            stats.ai_score += 1
    #   If ball passes right side of screen
    elif ball.rect.left > screen_rect.right:
        ball.center_ball()
        ball.reset = True
        stats.ai_score += 1
    #   If ball passes bottom side of screen
    elif ball.rect.top > screen_rect.bottom:
        ball.center_ball()
        ball.reset = True
        if ball.rect.centerx < screen_rect.centerx:
            stats.user_score += 1
        else:
            stats.ai_score += 1


def check_ball_collision(ball, sound_effect, paddle_left_mid, paddle_left_top, paddle_left_bottom,
                         paddle_right_mid, paddle_right_top, paddle_right_bottom):
    """Check if ball has collided. If so, call another function to check which paddle, and then where on the paddle"""
    if ball.rect.colliderect(paddle_left_mid):
        change_ball_direction(ball, paddle_left_mid)
        sound_effect.play()
    elif ball.rect.colliderect(paddle_left_bottom):
        change_ball_direction(ball, paddle_left_bottom)
        sound_effect.play()
    elif ball.rect.colliderect(paddle_left_top):
        change_ball_direction(ball, paddle_left_top)
        sound_effect.play()
    elif ball.rect.colliderect(paddle_right_mid):
        change_ball_direction(ball, paddle_right_mid)
        sound_effect.play()
    elif ball.rect.colliderect(paddle_right_bottom):
        change_ball_direction(ball, paddle_right_bottom)
        sound_effect.play()
    elif ball.rect.colliderect(paddle_right_top):
        change_ball_direction(ball, paddle_right_top)
        sound_effect.play()


def change_ball_direction(ball, paddle):
    #   Dividing left and right (LR) paddles into 3 sections

    # Range of top portion: 0 - 1/3 of paddle height
    top_of_paddle_lr = paddle.rect.height/3
    # Range of middle portion: 1/3 of paddle height - 2/3 of paddle height
    middle_of_paddle_lr = (paddle.rect.height/3)*2
    # Range of bottom portion: 2/3 of paddle height - paddle height    #TODO:Check if necessary
    # bottom_of_paddle_LR = paddle.rect.height

    #   Dividing top and bot (TB) paddles into 3 sections
    left_of_paddle_tb = paddle.rect.width/3
    middle_of_paddle_tb = (paddle.rect.width/3)*2

    if paddle.position == 'right-middle':
        #   If the ball hit the top portion of the right-middle paddle
        if paddle.rect.top <= ball.rect.centery <= (paddle.rect.top + top_of_paddle_lr):
            ball.left_right_direction = -1
            ball.up_down_direction = -1
        #    If the ball hit the middle potion of the right-middle paddle
        elif (paddle.rect.top + top_of_paddle_lr) <= ball.rect.centery <= (paddle.rect.top + middle_of_paddle_lr):
            ball.left_right_direction = -1
            ball.up_down_direction = 0
        else:
            ball.left_right_direction = -1
            ball.up_down_direction = 1
    elif paddle.position == 'left-middle':
        #   If the ball hit the top portion of the left-middle paddle
        if paddle.rect.top <= ball.rect.centery <= (paddle.rect.top + top_of_paddle_lr):
            ball.left_right_direction = 1
            ball.up_down_direction = -1
        #    If the ball hit the middle potion of the left-middle paddle
        elif (paddle.rect.top + top_of_paddle_lr) <= ball.rect.centery <= (paddle.rect.top + middle_of_paddle_lr):
            ball.left_right_direction = 1
            ball.up_down_direction = 0
        else:
            ball.left_right_direction = 1
            ball.up_down_direction = 1
    elif paddle.position == 'right-top':
        #   If the ball hit the left portion of the right-top paddle
        if paddle.rect.left <= ball.rect.centerx <= (paddle.rect.left + left_of_paddle_tb):
            ball.left_right_direction = -2
            ball.up_down_direction = 1
        #    If the ball hit the middle potion of the right-top paddle
        elif (paddle.rect.top + top_of_paddle_lr) <= ball.rect.centerx <= (paddle.rect.top + middle_of_paddle_tb):
            ball.left_right_direction = -1
            ball.up_down_direction = 1
        else:
            ball.left_right_direction = -0.5
            ball.up_down_direction = 1
    elif paddle.position == 'left-top':
        #   If the ball hit the left portion of the left-top paddle
        if paddle.rect.left <= ball.rect.centerx <= (paddle.rect.left + left_of_paddle_tb):
            ball.left_right_direction = 0.5
            ball.up_down_direction = 1
        #    If the ball hit the middle potion of the left-top paddle
        elif (paddle.rect.top + top_of_paddle_lr) <= ball.rect.centerx <= (paddle.rect.top + middle_of_paddle_tb):
            ball.left_right_direction = 1
            ball.up_down_direction = 1
        else:
            ball.left_right_direction = 2
            ball.up_down_direction = 1
    elif paddle.position == 'right-bottom':
        #   If the ball hit the left portion of the right-top paddle
        if paddle.rect.left <= ball.rect.centerx <= (paddle.rect.left + left_of_paddle_tb):
            ball.left_right_direction = -2
            ball.up_down_direction = -1
        #    If the ball hit the middle potion of the right top paddle
        elif (paddle.rect.top + top_of_paddle_lr) <= ball.rect.centerx <= (paddle.rect.top + middle_of_paddle_tb):
            ball.left_right_direction = -1
            ball.up_down_direction = -1
        else:
            ball.left_right_direction = -0.5
            ball.up_down_direction = -1
    elif paddle.position == 'left-bottom':
        #   If the ball hit the left portion of the left-bottom paddle
        if paddle.rect.left <= ball.rect.centerx <= (paddle.rect.left + left_of_paddle_tb):
            ball.left_right_direction = 0.5
            ball.up_down_direction = -1
        #    If the ball hit the middle potion of the left-bottom paddle
        elif (paddle.rect.top + top_of_paddle_lr) <= ball.rect.centerx <= (paddle.rect.top + middle_of_paddle_tb):
            ball.left_right_direction = 1
            ball.up_down_direction = -1
        else:
            ball.left_right_direction = 2
            ball.up_down_direction = -1


def check_play_button(stats, sb, play_button, mouse_x, mouse_y):
    """Start a new game when a player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #   Reset the game settings.

        #   Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            #   Reset the game statistics.
            stats.game_active = True

            #   Reset the scoreboard images.
            sb.prep_score()


def announce_winner(screen, winner):
    screen_rect = screen.get_rect()
    text_color = (30, 30, 30)
    rect = pygame.Rect(0, 0, 500, 500)
    rect_color = (0, 255, 0)
    font = pygame.font.SysFont(None, 48)

    winner_image = font.render(winner, True, text_color, rect_color)
    winner_image_rect = winner_image.get_rect()
    winner_image_rect.center = screen_rect.center
    screen.fill(rect_color, rect)
    screen.blit(winner_image, winner_image_rect)
