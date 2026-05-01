import pygame
from settings import *
from Fireboy import Fireboy
import os
class WaterGirl(Fireboy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.idle_path = WATERGIRL_IDLE_IMAGE_PATH
        self.right_path = WATERGIRL_RIGHT_IMAGE_PATH
        self.scale = WATERGIRL_SCALE
        self.load_animation_frames()
        self.water = True  # watergirl can pass through lava but not water
        self.lava = False  # watergirl cannot pass
        self.on_water = False  # track if watergirl is currently in water
        self.on_lava = False  # track if watergirl is currently in lava
    
    def _movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.current_animation = 'left'
            self.rect.x -= 5
        elif keys[pygame.K_d]:
            self.current_animation = 'right'
            self.rect.x += 5
        else:
            self.current_animation = 'idle'
        if keys[pygame.K_w]:
            if not self.jumping:
                self.jumping = True
                self.on_ground = False
                self.jump_velocity = self.jump_force