import sys
import pygame

from bullet import Bullet
from alien import Alien
from bunker import Bunker
import random


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, alien_bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.USEREVENT + 1:
            fire_bullet_alien(ai_settings, screen, ship, aliens, alien_bullets)
        elif event.type == pygame.USEREVENT + 2:
            random_ufo(ai_settings, screen, aliens)


def check_keydown_events(event, ai_settings, screen, ship, bullets, aliens):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets, aliens)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets,  mouse_x, mouse_y):
    """Start a new game when a player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #   Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        #   Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            #   Reset the game statistics.
            stats.reset_stats()
            stats.game_active = True

            #   Reset the scoreboard images.
            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()

            #   Empty the list of aliens and bullets
            aliens.empty()
            bullets.empty()

            #   cCreate a new fleet and center the ship
            create_fleet(ai_settings, screen, aliens)
            ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, sc, alien_bullets, bunkers):
    """Update images on the screen and flip to the new screen."""
    #   Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #   Redraw all bullets behind ship and aliens

    #   Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
        sc.draw_start_screen()
    else:
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        for alien_bullet in alien_bullets.sprites():
            alien_bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        bunkers.draw(screen)

        #   Draw the score information.
        sb.show_score()

    #   Make the most recently drawn screen visible
    pygame.display.flip()


#     ________________
#   _/BULLET FUNCTIONS\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers):
    """Update the position of bullets and get rid of old bullets"""
    #   Update bullet positions
    #   Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.top >= 800:
            alien_bullets.remove(alien_bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, aliens, bullets)
    check_alien_laser_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers)
    check_bunker_collisions(aliens, bullets, alien_bullets, bunkers)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, aliens, bullets):
    """Respond to bullet-alien collisions."""
    #   Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        #   If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()

        #   Increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, aliens)


def fire_bullet(ai_settings, screen, ship, bullets, aliens):
    """Fire a bullet if limit not reached"""
    #   Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship, aliens, 0)
        bullets.add(new_bullet)


#     ________________
#   _/ALIEN FUNCTIONS\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers):
    """Check if the fleet is at an edge, and then update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #   Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers)

    #   Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number, type_alien):
    """Create an alien and place it in the row."""
    #   Create an alien and place it in the row.
    alien = Alien(ai_settings, screen, type_alien)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #   Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers)
            break


def fire_bullet_alien(ai_settings, screen, ship, aliens, alien_bullets):
    for alien in aliens:
        if random.randint(0, 11) % 10 == 0:
            alien.will_fire = True
        else:
            alien.will_fire = False
        if alien.will_fire:
            new_bullet = Bullet(ai_settings, screen, ship, alien, 1)
            alien_bullets.add(new_bullet)


def check_alien_laser_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers):
    if pygame.sprite.spritecollideany(ship, alien_bullets):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers)


def random_ufo(ai_settings, screen, aliens):
    ufo = Alien(ai_settings, screen, 4)
    ufo.rect.top = 45
    aliens.add(ufo)


#     ________________
#   _/FLEET FUNCTIONS\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    #   Create an alien and find the number of aliens in a row
    #   Spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen, 1)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    for row_number in range(4):
        for alien_number in range(number_aliens_x):
            if row_number < 2:
                create_alien(ai_settings, screen, aliens, alien_number, row_number, 1)
            elif row_number < 3:
                create_alien(ai_settings, screen, aliens, alien_number, row_number, 2)
            elif row_number == 3:
                create_alien(ai_settings, screen, aliens, alien_number, row_number, 3)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.type != 4:
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break
        else:
            if alien.rect.right <= 0 or alien.rect.left >= 1200:
                aliens.remove(alien)


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        if alien.type != 4:
            alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


#     ________________
#   _/SHIP FUNCTIONS\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, bunkers):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        #   Decrement ships_left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        #   Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        #   Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, aliens)
        ship.center_ship()

        #   Pause
        # sleep(0.5)
        pygame.time.delay(500)
    else:
        bunkers.empty()
        pygame.time.delay(1000)
        stats.game_active = False
        pygame.mouse.set_visible(True)


#     ________________
#   _/HIGH SCORE FUNCTIONS\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


#     ________________
#   _/BUNKER FUNCTIONS\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_bunkers(screen, ai_settings, bunkers, ship):
    width = ai_settings.screen_width
    pixels_between_bunkers = width / 5              # Divided by 5 to fit 4 bunkers with space left+right of each
    bunker_x = 0
    bunker_y = ship.rect.top - 15
    for i in range(4):
        new_bunker = Bunker(screen)
        bunker_x += pixels_between_bunkers
        new_bunker.rect.centerx = bunker_x
        new_bunker.rect.bottom = bunker_y
        bunkers.add(new_bunker)


def check_bunker_collisions(aliens, bullets, alien_bullets, bunkers):
    bunker_alien_bullets_collisions = pygame.sprite.groupcollide(bunkers, alien_bullets, False, True)
    bunker_ship_bullets_collisions = pygame.sprite.groupcollide(bunkers, bullets, False, True)

    if bunker_alien_bullets_collisions or bunker_ship_bullets_collisions:
        for bunker1 in bunker_ship_bullets_collisions.keys():
            bunker1.index += 1
            if bunker1.index == 4:
                bunkers.remove(bunker1)
        for bunker2 in bunker_alien_bullets_collisions.keys():
            bunker2.index += 1
            if bunker2.index == 4:
                bunkers.remove(bunker2)
    for bunker in bunkers:
        if pygame.sprite.spritecollideany(bunker, aliens):
            bunkers.remove(bunker)
