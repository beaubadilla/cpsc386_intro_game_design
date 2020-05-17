import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf
from startup import StartScreen


def run_game():
    #   Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Instantiate objects
    play_button = Button(screen, "Play")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()
    bunkers = Group()
    gf.add_bunkers(screen, ai_settings, bunkers, ship)
    gf.create_fleet(ai_settings, screen, aliens)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    sc = StartScreen(screen, ai_settings, "ALIEN", "INVADERS")
    music = pygame.mixer.Sound('sounds/background_music.wav')
    music.set_volume(0.01)

    alien_fire_event = pygame.USEREVENT + 1                 # USEREVENT is a default attribute starting at 24
    ufo_event = pygame.USEREVENT + 2
    # Sets a timer that "makes" an alien_fire_event, just as
    # arrow key makes an event, every 3 seconds (3000 ms)
    pygame.time.set_timer(alien_fire_event, ai_settings.alien_bullets_frequency)
    pygame.time.set_timer(ufo_event, ai_settings.ufo_frequency)

    #   Start the main loop for the game.
    while True:
        #   Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, alien_bullets)

        if stats.game_active:
            music.play(-1)
            ship.update()
            bullets.update()
            alien_bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb,  ship, aliens, bullets, alien_bullets, bunkers)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers)
            bunkers.update()
        #   Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, sc, alien_bullets, bunkers)

        #   Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
