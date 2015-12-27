#!/usr/bin/python

import pygame

import constants
import levels
from player import Player


def main():
    """
    """
    pygame.init()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Leviathan')

    player = Player()

    level_list = []
    level_list.append(levels.Start_Menu(player))
    level_list.append(levels.Level_01(player))

    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = constants.PLAYER_START_X
    player.rect.y = constants.PLAYER_START_Y
    active_sprite_list.add(player)

    done = False
    clock = pygame.time.Clock()

    # Main Loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_SPACE:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()
        current_level.update()

        # Handle camera/background positioning
        if player.rect.x >= 400:
            diff = player.rect.x - 400
            player.rect.x = 400
            current_level.shift_world(-diff)

        if player.rect.x <= 100:
            diff = 100 - player.rect.x
            player.rect.x = 100
            current_level.shift_world(diff)

        # End of level logic
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 100
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # >>>>>> DRAW SECTION <<<<<<<<
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        # >>>> END DRAW SECTION <<<<<<<

        # 60 frames a second
        clock.tick(60)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

