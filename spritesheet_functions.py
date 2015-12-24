import pygame

import constants

class SpriteSheet(object):
    sprite_sheet = None


    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        """
        Grab a single image out of a larger spritesheet.
        """
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Set (0,0) of the image as transparent color
        image.set_colorkey(constants.PINK)

        return image
