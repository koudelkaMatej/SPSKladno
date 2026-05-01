import pygame
import settings

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(settings.ENEMY_BULLET_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = settings.ENEMY_BULLET_SPEED
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > settings.SCREEN_HEIGHT:
            self.kill()