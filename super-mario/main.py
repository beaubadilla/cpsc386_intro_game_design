import pygame
from pygame.sprite import Group

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from mario import Mario
from enemy import Enemy
from block import Block
from item import Item
from background import Background
import game_functions as gf
from bricks_placement import Placement
from game_over import GameOver


# import bricks_placement as bp


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode((1200, 450))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Super Mario")
    clock = pygame.time.Clock()

    # Make the Play button.
    play_button = Button(screen, "Play")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats()
    sb = Scoreboard(screen, stats)
    go_screen = GameOver(screen, stats)
    gf.load_high_scores("text/high_scores.txt", stats)

    # Set the background color.
    # bg_color = (230, 230, 230)

    # load all sprite images
    large_regular_mario_images, small_regular_mario_images, \
    large_fire_mario_images, small_fire_mario_images, \
    large_star_mario_images, small_star_mario_images, \
    goomba_images, turtle_images, \
    mushroom_images, pipe_image, mushroom_image, flower_images, \
    question_block_images, star_images, static_coin_images, dynamic_coin_images, \
    overworld_brick_images, overworld_floor_image, overworld_stair_image, \
    underworld_brick_image, underworld_floor_image, \
    vertical_pipe_images, horizontal_pipe_images = gf.get_sprites()

    # Make a mario, a group of blocks, and a group of enemies.
    background = Background(screen)
    mario = Mario(screen, small_regular_mario_images, large_regular_mario_images,
                  small_fire_mario_images, large_fire_mario_images,
                  small_star_mario_images, large_star_mario_images)
    goomba1 = Enemy(screen, goomba_images, 1, 0, 900, 716)
    goomba2 = Enemy(screen, goomba_images, 1, 1276, 1476, 1300)
    goomba3 = Enemy(screen, goomba_images, 1, 1531, 1827, 1600)
    goomba4 = Enemy(screen, goomba_images, 1, 1531, 1827, 1700)
    goomba5 = Enemy(screen, goomba_images, 1, 3000, 4200, 3135)
    goomba6 = Enemy(screen, goomba_images, 1, 3000, 4200, 3190)
    goomba7 = Enemy(screen, goomba_images, 1, 3000, 4200, 3740)
    goomba8 = Enemy(screen, goomba_images, 1, 3000, 4200, 3780)
    goomba9 = Enemy(screen, goomba_images, 1, 3000, 4200, 3960)
    goomba10 = Enemy(screen, goomba_images, 1, 3000, 4200, 4000)
    goomba11 = Enemy(screen, goomba_images, 1, 3000, 4200, 4040)
    goomba12 = Enemy(screen, goomba_images, 1, 3000, 4200, 4080)
    goomba13 = Enemy(screen, goomba_images, 1, 5275, 5733, 5540)
    goomba14 = Enemy(screen, goomba_images, 1, 5275, 5733, 5580)

    turtle = Enemy(screen, turtle_images, 2, 3000, 4200, 3500)
    enemies = Group(turtle, goomba1, goomba2, goomba3, goomba4, goomba5, goomba6,
                    goomba7, goomba8, goomba9, goomba10, goomba11, goomba12, goomba13, goomba14)
    # block = Block(screen, '?', question_block_images)
    # block.rect.bottom = screen_rect.bottom - 100
    blocks = Group()
    coins = []
    coins2 = []
    # mushroom = Item(screen, mushroom_image, 1)
    # flower = Item(screen, flower_images, 2)
    # star = Item(screen, star_images, 3)
    # items = Group(mushroom, flower, star)
    items = Group()
    fireballs = Group()
    bp = Placement()
    bp.place_bricks(screen, question_block_images, overworld_brick_images,
                    overworld_stair_image, pipe_image, blocks,
                    static_coin_images, mushroom_image, flower_images, star_images, coins, coins2, items)

    # block = Block(screen, '?', question_block_images, mushroom)
    # block.rect.bottom = screen_rect.bottom - 100
    # block.rect.centerx = screen_rect.left + 100

    # pygame.mixer.music.load("sounds/overworld_theme.mp3")
    # pygame.mixer.music.play(-1)

    # Start the main loop for the game.
    while True:
        gf.check_events(screen, stats, sb, play_button, mario, enemies, fireballs, bp, background, blocks)

        if stats.game_active:
            gf.check_block_collision(screen, mario, blocks, fireballs)
            gf.check_item_collision(screen, mario, items)
            gf.check_fireball_enemy_collision(fireballs, enemies)
            mario.update()
            enemies.update()
            fireballs.update()
            # block.blitme()

            if not mario.dead:
                gf.check_mario_hit(screen, stats, sb, mario, enemies)
            else:
                pygame.mixer.music.stop()
                if mario.death_timer > 100:
                    gf.reset(background, stats, mario, enemies)
            # print(len(enemies.sprites()))
        if stats.lives_left != 0:
            gf.update_screen(screen_rect, stats, sb, background, mario, enemies, play_button, blocks, items, fireballs)
        else:
            screen.fill((0, 0, 0))
            gf.check_game_over(stats)
            go_screen.draw()
            pygame.display.flip()
        clock.tick(60)
        # print(str(clock.get_fps())))


run_game()
