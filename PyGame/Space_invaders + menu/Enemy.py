import pygame
import settings
import random as rand
from EnemyBullet import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.enemy_type = rand.randint(1, 5)
        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH.format(self.enemy_type)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.ENEMY_SCALE, self.image.get_height()*settings.ENEMY_SCALE))
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0
        self.direction = "Left"
        self.bullet_group = pygame.sprite.Group()
        self.shoot_timer = 0
        self.shoot_interval = rand.randint(50, 150)  # random shoot interval for each enemy
        self.drop_speed = settings.ENEMY_DROP
        self.speed = settings.ENEMY_SPEED


        if self.enemy_type == 1:
            pass
        elif self.enemy_type == 2:  
            pass
        elif self.enemy_type == 3:
            pass
        elif self.enemy_type == 4:
            self.drop_speed = settings.ENEMY_DROP * 1.5
        elif self.enemy_type == 5:
            self.speed = settings.ENEMY_SPEED * 1.5


            
    def update(self):
        if self.counter % 50 == 0:
            self.rect.y += self.drop_speed
            if self.direction == "Right":
                self.direction = "Left"
            else:
                self.direction = "Right"
        else:
            if self.direction == "Right":
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed
        self.counter += 1
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = "Right"
        if self.rect.right > settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
            self.direction = "Left"
        if self.shoot_timer == self.shoot_interval:
            self.shoot()
            self.shoot_timer = 0
        else:
            self.shoot_timer += 1    
        if self.rect.top > settings.SCREEN_HEIGHT:
            self.kill()
    def shoot(self):
        if rand.randint(0, 100) < settings.ENEMY_SHOOT_CHANCE:
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            self.bullet_group.add(bullet)

            

if __name__ == "__main__":
    import main