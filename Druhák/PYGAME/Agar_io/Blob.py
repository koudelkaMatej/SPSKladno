import pygame
from settings import *
import random

class Blob(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None, radius=None, color=None):    
        super().__init__()  # Initialize the pygame.sprite.Sprite base class
        
        # Use provided parameters or generate random ones
        self.x = x if x is not None else random.randint(BLOB_START_SIZE, SCREEN_WIDTH - BLOB_START_SIZE)
        self.y = y if y is not None else random.randint(BLOB_START_SIZE, SCREEN_HEIGHT - BLOB_START_SIZE)
        self.radius = radius if radius is not None else BLOB_START_SIZE
        self.color = color if color is not None else LIGHT_GREEN
        
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.fill((0, 0, 0, 0))  # Clear the surface
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
