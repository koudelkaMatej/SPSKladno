import pygame
import settings
import random as rand
from Bullet import *

clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.PLAYER_IMAGE_PATH).convert_alpha()
        self.width, self.height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.width*settings.PLAYER_SCALE, self.height*settings.PLAYER_SCALE))
        self.rect = self.image.get_rect(bottom=settings.SCREEN_HEIGHT, centerx=settings.SCREEN_WIDTH // 2) # center = (x,y)¨
        self.speed = settings.PLAYER_SPEED  # rychlost v pixelech za sekundu
        self.shoot_cooldown = 500  # cooldown mezi střelami v milisekundách
        self.last_shot_time = 0  # čas poslední střely v milisek

        self.bullet_group = pygame.sprite.Group()
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed   
        if keys[pygame.K_RIGHT] and self.rect.right < settings.SCREEN_WIDTH:
            self.rect.x += self.speed
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullet_group.add(bullet)
            self.last_shot_time = current_time

if __name__ == "__main__":
    import main