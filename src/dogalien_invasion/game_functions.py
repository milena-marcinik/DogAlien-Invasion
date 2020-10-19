import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, rocket_ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        rocket_ship.moving_right = True
        # Move the ship to the left
    elif event.key == pygame.K_LEFT:
        rocket_ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        fire_bullet(ai_settings, screen, rocket_ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, rocket_ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        rocket_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket_ship.moving_left = False


def check_events(ai_settings, screen, stats, play_button, rocket_ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, rocket_ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket_ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, rocket_ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, rocket_ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        # Reset game statistic
        stats.reset_stats()
        stats.game_active = True

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, rocket_ship, aliens)
        rocket_ship.center_rocket_ship()


def update_screen(ai_settings, screen, stats, sb, rocket_ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.blit(ai_settings.background, (0, 0))
    rocket_ship.blitme()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets:
        bullet.draw_bullet(screen)

    # Draw aliens
    for alien in aliens:
        alien.blitme()

    # Draw the score information
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        screen.blit(ai_settings.start_screen, (0, 0))
        play_button.update_button(pygame.mouse.get_pos())
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def fire_bullet(ai_settings, screen, rocket_ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, rocket_ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, stats, sb, rocket_ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_settings, screen, stats, sb, rocket_ship, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, stats, sb, rocket_ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        stats.score += ai_settings.alien_points
        # * len(aliens)
        sb.prep_score()

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, rocket_ship, aliens)


def ship_hit(ai_settings, stats, screen, rocket_ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.rocket_ships_left > 0:
        # Decrement ships_left.
        stats.rocket_ships_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, rocket_ship, aliens)
        rocket_ship.center_rocket_ship()

        # Pause
        sleep(1)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, rocket_ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, rocket_ship, aliens, bullets)


def update_aliens(ai_settings, stats, screen, rocket_ship, aliens, bullets):
    """
     Check if the fleet is at an edge,
     and then update the postions of all aliens in the fleet.
     """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(rocket_ship, aliens):
        ship_hit(ai_settings, stats, screen, rocket_ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, rocket_ship, aliens, bullets)


def get_number_aliens(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.display_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, rocket_ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.display_height - 3 * alien_height - rocket_ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, rocket_ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, rocket_ship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
