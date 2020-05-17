import pygame
import game_functions as gf
from settings import Settings
from paddle import Paddle
from ball import Ball
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from startup import Menu
import random


def run_game():
    #   Initialize game and create a screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )

    #   Title the game window as "Pong"
    pygame.display.set_caption("Pong")

    #   Declare and initialize/instantiate objects
    paddle_left_mid = Paddle(settings, screen, 'left-middle')
    paddle_left_top = Paddle(settings, screen, 'left-top')
    paddle_left_bottom = Paddle(settings, screen, 'left-bottom')
    paddle_right_mid = Paddle(settings, screen, 'right-middle')
    paddle_right_top = Paddle(settings, screen, 'right-top')
    paddle_right_bottom = Paddle(settings, screen, 'right-bottom')
    ball = Ball(settings, screen)
    stats = GameStats()
    play_button = Button(screen, "Play")
    sb = Scoreboard(settings, screen, stats)
    menu = Menu(screen, settings, "PONG", "AI--NO WALLS")
    sound_effect = pygame.mixer.Sound('sounds/boom.wav')
    sound_effect.set_volume(0.1)

    #   Main loop for game
    while True:
        #   Check user input through events
        gf.check_events(paddle_right_mid, paddle_right_top, paddle_right_bottom, play_button, stats, sb)

        if stats.game_active:
            #   Update objects (change positions)
            gf.update_paddles(
                paddle_left_mid, paddle_left_top, paddle_left_bottom,
                paddle_right_mid, paddle_right_top, paddle_right_bottom
            )
            gf.check_ball_collision(
                ball, sound_effect,
                paddle_left_mid, paddle_left_top, paddle_left_bottom,
                paddle_right_mid, paddle_right_top, paddle_right_bottom
            )
            gf.check_dead_ball(screen, ball, stats)
            ball.update()

        #   Prep entire screen for next frame
        #   This function will call all 'blitme()' and 'draw'
        gf.prep_screen(
            settings, screen, paddle_left_mid, paddle_left_top, paddle_left_bottom, paddle_right_mid, paddle_right_top,
            paddle_right_bottom, ball, play_button, stats, sb, menu
        )

        #   Draw next frame
        pygame.display.flip()

        #   If ball gets reset, have a short pause
        if ball.reset:
            sleep(1)
            rand_num_ud = random.randint(-2, 2)
            rand_num_lr = random.randint(-2, 2)
            if rand_num_lr == 0:
                rand_num_lr += 1
            if rand_num_ud == 0:
                rand_num_ud += 1
            ball.up_down_direction = rand_num_ud
            ball.left_right_direction = rand_num_lr
            ball.reset = False

        if stats.ai_score == 15:
            gf.announce_winner(screen, "AI wins!")
            stats.game_active = False
            pygame.mouse.set_visible(True)
            stats.ai_score = 0
            sleep(0.5)
        elif stats.user_score == 15:
            stats.game_active = False
            pygame.mouse.set_visible(True)
            gf.announce_winner(screen, "User wins!")
            stats.user_score = 0
            sleep(0.5)


run_game()
