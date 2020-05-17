# TODO(Bug): If a crash occurs, 'pacmanportalmaze.txt' might become empty. Must c/p from 'maze_template.txt'

# TODO: Adding sounds(Pacman death, blue/white ghost, Ghost death, Pacman eating)
# TODO: Ghost AI
# TODO: Pacman chase ghost animation in start screen
# TODO: Pacman death animation
# TODO: Ghost death animation (to eyes)
# TODO: Refine Pacman and ghost movement
# TODO: Ghost animations based on velocity
# TODO: Ghost returning to pen after death
# TODO: Random fruit
# TODO: Pacman interacts with fruit
# TODO: Refine aesthetics
# TODO: Ghost personalities
# TODO: Multiple levels
# TODO: Make portals temporary
import pygame
import game_functions as g_f
from maze import Maze
from settings import Settings
from start_screen import StartScreen
from game_state import GameState
from high_score_screen import HighScoreScreen
from scoreboard import Scoreboard
from pacman import PacMan
from ghost import Ghost
from pygame.sprite import Group

HS_FILE = "text/highscores.txt"
MAZE_FILE = "text/pacmanportalmaze.txt"


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )
    pygame.display.set_caption("Portal Pacman")

    maze = Maze(screen, MAZE_FILE, "shield", "portal", "portal", "Pill", "Power_Pill")
    game_state = GameState()
    start_screen = StartScreen(screen, settings, game_state, maze)
    high_score_screen = HighScoreScreen(screen, game_state)

    g_f.load_high_scores(HS_FILE, game_state)
    g_f.load_maze_array(MAZE_FILE, game_state)
    high_score_screen.load_high_scores_images(game_state)
    ghosts = Group()
    scoreboard = Scoreboard(screen, settings, game_state, ghosts, maze)
    red_ghost = Ghost(screen, 'red', game_state)
    pink_ghost = Ghost(screen, 'pink', game_state)
    orange_ghost = Ghost(screen, 'orange', game_state)
    teal_ghost = Ghost(screen, 'teal', game_state)
    ghosts = Group()
    ghosts.add(red_ghost)
    ghosts.add(pink_ghost)
    ghosts.add(orange_ghost)
    ghosts.add(teal_ghost)
    pacman = PacMan(screen, settings, game_state, ghosts, maze)

    ghost_sound = pygame.mixer.Sound('sounds/Ghost2.wav')
    ghost_sound.set_volume(0.01)

    while True:
        screen.fill(settings.bg_color)
        g_f.check_events(start_screen, settings, game_state, high_score_screen, pacman, maze)
        if game_state.game_active:
            ghost_sound.play(-1)
            g_f.update_game(scoreboard, pacman, maze, ghosts, game_state)
            g_f.draw_game(screen, maze, scoreboard, pacman, ghosts)
        else:
            if game_state.start_screen and not game_state.high_score_screen:
                g_f.update_start_screen(start_screen)
                start_screen.draw()
            elif game_state.high_score_screen and not game_state.start_screen:
                high_score_screen.draw()

        pygame.display.flip()


run_game()
