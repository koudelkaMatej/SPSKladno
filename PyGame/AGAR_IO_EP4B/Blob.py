import pygame
from settings import *
import random

class Blob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(5, SCREEN_WIDTH-5)
        self.y = random.randint(5, SCREEN_HEIGHT-5)
        self.radius = FOOD_START_SIZE
        self.color = LIGHT_GREEN
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=(self.x, self.y))