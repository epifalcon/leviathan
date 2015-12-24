import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    """
    """
    change_x = 0
    change_y = 0

    walking_frames_l = []
    walking_frames_r = []

    # Facing direction
    direction = 'R'

    # Sprites
    level = None

    def __init__(self):
        """
        Constructor
        """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet('p1_walk.png')
        image = sprite_sheet.get_image(0, 0, 30, 55)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(30, 0, 60, 55)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(60, 0, 90, 55)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(90, 0, 120, 55)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(120, 0, 150, 55)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(150, 0, 180, 55)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(0, 0, 30, 55)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(30, 0, 60, 55)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(60, 0, 90, 55)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(90, 0, 120, 55)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(120, 0, 150, 55)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(150, 0, 180, 55)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Initial image
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()


    def update(self):
        """
        Move the Player
        """
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction = 'R':
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # Collision detection horizontal
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If moving right
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Collsion detection vertical
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset position based on the top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x


    def calc_grav(self):
        """
        Calculate gravity
        """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height


    def jump(self):
        # See if there is a platform below Player
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # Jump if we can
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10


    def go_left(self):
        self.change_x = -3
        self.direction = "L"

    def go_right(self):
        self.change_x = 3
        self.direction = "R"

    def stop(self):
        self.change_x = 0


