import pygame
import settings

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = [pygame.image.load(settings.EXPLOSION_IMAGE_PATH.format(i)).convert_alpha() for i in range(1, 6)]
        self.current_image = 0
        self.image = self.animations[self.current_image]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_speed = 100  # Adjust this value to change the speed of the explosion animation
        self.last_update_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_speed:
            self.current_image += 1
            if self.current_image < len(self.animations):
                self.image = self.animations[self.current_image]
                self.last_update_time = current_time
            else:
                self.kill()