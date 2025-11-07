import pygame
from settings import *
import random

class Player_AI(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()  # Initialize the pygame.sprite.Sprite base class
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 3  #
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.fill((0, 0, 0, 0))  # Clear the surface
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def update(self,mouse_x, mouse_y):  #
        # Move towards the mouse position
        self.ai_move_1()
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def ai_move_1(self):
        self.x += random.choice([-1, 1]) * self.speed
        self.y += random.choice([-1, 1]) * self.speed

if __name__ == "__main__":
    import main