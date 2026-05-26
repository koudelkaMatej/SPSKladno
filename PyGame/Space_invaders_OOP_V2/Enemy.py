import pygame
import settings
import random as rand
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        alien_type = rand.randint(1, 5)
        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH.format(alien_type)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.ENEMY_SCALE,self.image.get_height()*settings.ENEMY_SCALE))
        self.rect = self.image.get_rect(center = (x,y)) # center = (x,y)¨
        self.speed = settings.ENEMY_SPEED
        self.direction = 1
        self.counter_for_direction = -100
        self.shooted = False
        self.shooting_cooldown = rand.randint(1000,5000)
        self.last_shooting_time = pygame.time.get_ticks()
        self.shoot_timer = 0
        self.hp = 1
    def update(self):
        if self.direction == 1:
            self.rect.move_ip(self.speed,0)
            self.counter_for_direction += 1
        else:
            self.rect.move_ip(-self.speed,0)
            self.counter_for_direction -= 1
        if self.counter_for_direction % 100 == 0 and self.counter_for_direction != 0:
            self.direction *= -1
            self.rect.move_ip(0,settings.ENEMY_DROP_SPEED)
        self._check_borders()

        if self.shooted == False:
            self.shoot_timer = pygame.time.get_ticks()
            if self.shoot_timer - self.last_shooting_time >= self.shooting_cooldown:
                self.last_shooting_time = pygame.time.get_ticks()
                self.shooted = True

    def _reset_shoot_timer(self):
        self.shooted = False
        self.shooting_cooldown = rand.randint(1000,5000)


    def check_if_enemy_shoot(self):
        if self.shooted:
            self._reset_shoot_timer()
            return True
        return False

    def _check_borders(self):
        if self.rect.right > settings.SCREEN_WIDTH - 50:
            self.counter_for_direction = 100
            self.direction = -1
            self.rect.y += settings.ENEMY_DROP_SPEED
        elif self.rect.left < 50:
            self.counter_for_direction = -100
            self.direction = 1
            self.rect.y += settings.ENEMY_DROP_SPEED
        



if __name__ == "__main__":
    import main