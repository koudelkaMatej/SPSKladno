import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()  # Initialize the pygame.sprite.Sprite base class
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.fill((0, 0, 0, 0))  # Clear the surface
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def update(self,mouse_x, mouse_y):
        # Move towards the mouse position
        direction_x = mouse_x - self.x
        direction_y = mouse_y - self.y
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if distance >= 3.6:
            direction_x /= distance
            direction_y /= distance
            speed = 5
            self.x += direction_x * speed
            self.y += direction_y * speed
        self.rect.center = (self.x, self.y)

if __name__ == "__main__":
    import main