import pygame
from settings import *
import random

class Blob(pygame.sprite.Sprite):
    def __init__(self):    
        super().__init__()  # Initialize the pygame.sprite.Sprite base class
        self.x = random.randint(BLOB_START_SIZE, SCREEN_WIDTH - BLOB_START_SIZE)
        self.y = random.randint(BLOB_START_SIZE, SCREEN_HEIGHT - BLOB_START_SIZE)
        self.radius = BLOB_START_SIZE
        self.color = LIGHT_GREEN
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.fill((0, 0, 0, 0))  # Clear the surface
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
