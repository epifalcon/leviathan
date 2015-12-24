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


class Start_Menu(level):
    """
    TODO
    """


class Level_01(level)
    """
    Level 1
    """

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load('background_01.png').convert()
        self.background.set_colorkey(constants.PINK)
        self.level_limit = -2500

