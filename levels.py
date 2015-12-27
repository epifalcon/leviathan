import pygame

import constants
import platforms

class Level():
    """
    Generic super-class for levels.
    Create a child class for each level with level-specific info
    """
    platform_list = None
    enemy_list = None
    background = None

    # How far this wold has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """
        Player needed for when moving platforms collide with Player
        """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player


    def update(self):
        self.platform_list.update()
        self.enemy_list.update()


    def draw(self, screen):
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


    def shift_world(self, shift_x):
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


class Start_Menu(Level):
    """
    TODO
    """

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load('Levels/start_menu.png').convert()
        self.level_limit = -1000


class Level_01(Level):
    """
    Level 1
    """

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load('Levels/background_01.png').convert()
        self.background.set_colorkey(constants.PINK)
        self.level_limit = -2500

        level = [[platforms.GRASS_LEFT, 500, 500],
                 [platforms.GRASS_MIDDLE, 570, 500],
                 [platforms.GRASS_RIGHT, 640, 500]]

        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

