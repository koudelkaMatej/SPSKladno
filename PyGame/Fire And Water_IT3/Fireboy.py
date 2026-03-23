import pygame
from settings import *
import os
class Fireboy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = {}
        self.idle_path = FIREBOY_IDLE_IMAGE_PATH
        self.right_path = FIREBOY_RIGHT_IMAGE_PATH
        self.load_animation_frames()
        self.current_animation = 'idle'
        self.animation_index = 0
        self.image = self.animations[self.current_animation][self.animation_index]
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.image_mask = pygame.mask.from_surface(self.image)
        self.jumping = False
        self.jump_velocity = 0
        self.jump_force = JUMP_FORCE
        self.on_ground = True

        

    def load_animation_frames(self):
        # idle animation
        idle_animations = []
        left_animations = []
        right_animations = []
        cesta = os.path.dirname(self.idle_path)
        pocet = sum(1 for f in os.scandir(cesta) if f.is_file() and f.name.endswith(".png"))
        for i in range(1,pocet):
            img = pygame.image.load(self.idle_path.format(i))
            img = pygame.transform.scale(img, (img.get_width() * FIREBOY_SCALE, img.get_height() * FIREBOY_SCALE))
            idle_animations.append(img)
        cesta = os.path.dirname(self.right_path)
        pocet = sum(1 for f in os.scandir(cesta) if f.is_file() and f.name.endswith(".png"))
        right_animations = [pygame.image.load(self.right_path.format(i)) for i in range(1,pocet)]
        right_animations = [pygame.transform.scale(img, (img.get_width() * FIREBOY_SCALE, img.get_height() * FIREBOY_SCALE)) for img in right_animations]
        left_animations = [pygame.transform.flip(img, True, False) for img in right_animations]
        self.animations ={
            'idle': idle_animations,
            'right': right_animations,
            'left': left_animations
        }

    def _movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.current_animation = 'left'
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.current_animation = 'right'
        else:
            self.current_animation = 'idle'
        if keys[pygame.K_UP] and self.on_ground:
            self.jumping = True
            self.jump_velocity = self.jump_force
            self.on_ground = False

    def update(self):
        self._movement()
        if not self.on_ground:
            self.rect.y += self.jump_velocity
            self.jump_velocity += GRAVITY
        else:
            self.jump_velocity = 0
            self.jumping = False






        self.animation_index += 0.1
        if self.animation_index >= len(self.animations[self.current_animation]):
            self.animation_index = 0
        self.image = self.animations[self.current_animation][int(self.animation_index)]
        self.image_mask = pygame.mask.from_surface(self.image)



if __name__ == "__main__":
    import main 