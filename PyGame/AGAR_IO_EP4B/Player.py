import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = PLAYER_START_SIZE
        self.color = color
        self.speed = PLAYER_SPEED
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, mouse_x, mouse_y):
        direction_x = mouse_x - self.x
        direction_y = mouse_y - self.y
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if distance >= 3.6: # 7.02
            direction_x /= distance
            direction_y /= distance

            self.x += direction_x * self.speed
            self.y += direction_y * self.speed
        else:
            self.x = direction_x + self.x
            self.y = direction_y + self.y
            self.rect.center = (self.x, self.y)
        self.rect.center = (self.x, self.y)
        

if __name__ == "__main__":
    import main