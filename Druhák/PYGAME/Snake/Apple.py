import pygame
from settings import *
import random

class Apple(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        if image_path == RED_APPLE_IMAGE_PATH:
            self.type = "red"
        else:
            self.type = "green"
        x = random.randint(CELL_SIZE//2, SCREEN_WIDTH - CELL_SIZE//2)
        x -= x % 20
        y = random.randint(CELL_SIZE//2, SCREEN_HEIGTH - CELL_SIZE//2)
        y -= y % 20
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))

