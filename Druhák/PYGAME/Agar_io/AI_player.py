import pygame
from settings import *
import random

class AI_player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()  # Initialize the pygame.sprite.Sprite base class
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.fill((0, 0, 0, 0))  # Clear the surface
        self.speed = 2
        self.counter = 0
        self.smerX = 0
        self.smerY = 0
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def update(self,mouse_x, mouse_y):
        # Move towards the mouse position
        self.ai2()
        self.rect.center = (self.x, self.y)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def ai1(self):
        self.x += random.choice([-1,1]) * self.speed
        self.y += random.choice([-1,1]) * self.speed
    
    def ai2(self):
        if self.counter % 30 == 0:
            self.smerX = random.choice([-1,1])
            self.smerY = random.choice([-1,1])
        self.x += self.smerX * self.speed
        self.y += self.smerY * self.speed
        self.counter += 1

if __name__ == "__main__":
    import main