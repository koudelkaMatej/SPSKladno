import pygame
import settings
import random as rand
from EnemyBullet import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH.format(rand.randint(1, 5))).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.ENEMY_SCALE, self.image.get_height()*settings.ENEMY_SCALE))
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0
        self.direction = "Left"
    def update(self):
        if self.counter % 50 == 0:
            self.rect.y += settings.ENEMY_DROP
            if self.direction == "Right":
                self.direction = "Left"
            else:
                self.direction = "Right"
        else:
            if self.direction == "Right":
                self.rect.x += settings.ENEMY_SPEED
            else:
                self.rect.x -= settings.ENEMY_SPEED
        self.counter += 1
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = "Right"
        if self.rect.right > settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
            self.direction = "Left"
        self.shoot()
    def shoot(self):
        if rand.random() < 0.25:  # 25% šance na střelbu každý update
           bullet_group.add(EnemyBullet(self.rect.centerx, self.rect.bottom))
            

if __name__ == "__main__":
    import main