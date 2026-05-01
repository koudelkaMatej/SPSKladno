import pygame
from settings import *
import random
class Pipe(pygame.sprite.Sprite):
    def __init__(self, smer):
        super().__init__()
        PIPE_HEIGHT = random.randint(50, 200)
        self.image = pygame.image.load(PIPE_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.pipe_passed = False  # flag to check if pipe has been passed

        if smer == "up":
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH, 0))
            self.rect.y = 0
            self.rect.x = SCREEN_WIDTH
        elif smer == "down":
            self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH, SCREEN_HEIGHT - PIPE_HEIGHT))
            self.rect.y = SCREEN_HEIGHT - 150 - PIPE_HEIGHT
            self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= 4
        if self.rect.x < -self.rect.width:
            self.kill()

if __name__ == "__main__":
    import main
