import pygame
import settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(settings.BULLET_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = settings.BULLET_SPEED
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()