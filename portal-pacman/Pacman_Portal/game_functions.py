import pygame
import sys


#     _______
# ___/GENERAL\__________________________________________________________________________________________________________
def check_events(start_screen, settings, game_state, high_score_screen, pacman, maze):
    """Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            maze.reset_maze_file()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pacman, maze)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pacman)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, start_screen, settings, game_state)
            check_high_score_button(mouse_x, mouse_y, start_screen, game_state)
            check_back_button(mouse_x, mouse_y, high_score_screen, game_state)
        # elif event.type == pygame.USEREVENT + 1:
        #     # call fruit function


def check_keydown_events(event, pacman, maze):
    if event.key == pygame.K_RIGHT:
        pacman.reset_movement_flags()
        pacman.moving_right = True
    elif event.key == pygame.K_LEFT:
        pacman.reset_movement_flags()
        pacman.moving_left = True
    elif event.key == pygame.K_UP:
        pacman.reset_movement_flags()
        pacman.moving_up = True
    elif event.key == pygame.K_DOWN:
        pacman.reset_movement_flags()
        pacman.moving_down = True
    else:
        pacman.reset_movement_flags()
    if event.key == pygame.K_SPACE:
        pacman.shoot_portal()
    if event.key == pygame.K_q:
        maze.reset_maze_file()
        sys.exit()


def check_keyup_events(event, pacman):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        pacman.moving_right = False
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = False
    elif event.key == pygame.K_UP:
        pacman.moving_up = False
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = False


def update_game(scoreboard, pacman, maze, ghosts, game_state):
    scoreboard.update()
    pacman.update()
    maze.update()
    ghosts.update()
    check_game_over(game_state)
    check_ghost_pacman_collision(ghosts, pacman, game_state)


def update_start_screen(start_screen):
    start_screen.update()


def draw_game(screen, maze, scoreboard, pacman, ghosts):
    maze.blitme()
    scoreboard.draw()
    pacman.draw()
    ghosts.draw(screen)


def check_game_over(game_state):
    hs_file = 'text/highscores.txt'
    if game_state.lives == 0:
        update_high_scores(game_state)
        update_high_scores_file(hs_file, game_state)
        game_state.game_active = False
        game_state.start_screen = True
        game_state.reset_stats()
        pygame.mouse.set_visible(True)


#     ___________
# ___/HIGH SCORES\______________________________________________________________________________________________________
def load_high_scores(hs_file, game_state):
    # with open(hs_file, 'rb') as f:
    #     game_state.high_scores = pickle.load(f)
    #     f.close()
    with open(hs_file) as f:
        game_state.high_scores = f.read().splitlines()
        f.close()


def update_high_scores_file(hs_file, game_state):
    # ASSUMING high_scores in game_state is updated
    with open(hs_file, 'w') as f:
        for num_scores in range(len(game_state.high_scores)):
            f.write("{}\n".format(str(game_state.high_scores[num_scores])))
        f.close()


def update_high_scores(game_state):
    for num_score in range(len(game_state.high_scores)):
        if game_state.score >= int(game_state.high_scores[num_score]):
            game_state.high_scores[num_score] = game_state.score
            break


#     _______
# ___/Buttons\__________________________________________________________________________________________________________
def check_play_button(mouse_x, mouse_y, start_screen, settings, game_state):
    """Start a new game when a player clicks Play."""
    button_clicked = start_screen.play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_state.game_active and not game_state.high_score_screen:
        #   Reset the game settings.

        #   Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        if start_screen.play_button.rect.collidepoint(mouse_x, mouse_y):
            # Do the following when a new GAME starts
            #   Reset the game statistics.
            game_state.reset_stats()
            game_state.game_active = True
            settings.reset_settings()

            # Just in case, turn these flags off
            game_state.start_screen = False
            game_state.high_score_screen = False


def check_high_score_button(mouse_x, mouse_y, start_screen, game_state):
    """Display high score screen"""
    button_clicked = start_screen.high_scores_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_state.game_active:
        game_state.high_score_screen = True
        game_state.start_screen = False


def check_back_button(mouse_x, mouse_y, high_score_screen, game_state):
    """Display start screen"""
    button_clicked = high_score_screen.back_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and game_state.high_score_screen and not game_state.game_active:
        game_state.high_score_screen = False
        game_state.start_screen = True


#     ___
# ___/MAP\______________________________________________________________________________________________________________
def load_maze_array(maze_file, game_state):
    with open(maze_file) as f:
        game_state.maze_array = f.read().splitlines()


#     _______
# ___/GHOSTS\___________________________________________________________________________________________________________
def activate_power_pill(ghosts):
    print("Ghosts:", ghosts)
    for ghost in ghosts:
        ghost.vulnerable = True
        ghost.timer_start = True
        ghost.timer_beg = pygame.time.get_ticks()
        ghost.timer_stop = pygame.time.get_ticks() + 10000


def check_ghost_pacman_collision(ghosts, pacman, game_state):
    for ghost in ghosts.copy():
        if pacman.current_row == ghost.row and pacman.current_col == ghost.col:
            if ghost.vulnerable:
                ghosts.remove(ghost)
            else:
                game_state.lives -= 1
                pacman.center()
                pygame.time.wait(2000)
