import pygame
from settings import *
import os

class Fire_boy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = []
        self.load_animation_frames()
        self.current_frame = 0
        self.image = self.animations[0][self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_interval = 6 #počet snímku do výměny obrázku
        self.animation_timer = 0 #počet snímků, které již proběhly od poslední výměny obrázku

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
           # self.animations = [self.animations[2]]  # right animation
            self.rect.x += 5
        elif keys[pygame.K_LEFT]:
           # self.animations = [self.animations[1]]  # left animation
            self.rect.x -= 5

        if self.animation_timer >= self.animation_interval: # pokud uplynul čas pro výměnu obrázku
            self.current_frame += 1 # zvýšení indexu obrázku
            if self.current_frame >= len(self.animations[0]): # pokud je index větší než počet obrázků v listu
                self.current_frame = 0 # resetuji index na první obrázek
            self.animation_timer = 0 # resetuji časovač
        self.image = self.animations[0][self.current_frame]  # aktualizace obrázku na základě indexu
        self.animation_timer += 1 # zvýšení časovače

    def load_animation_frames(self):
        # idle animation
        idle_animations = []
        left_animations = []
        right_animations = []
        cesta = os.path.dirname(BOY_IDLE_PATH)
        pocet = sum(1 for f in os.scandir(cesta) if f.is_file() and f.name.endswith(".png"))
        for i in range(1,pocet):
            img = pygame.image.load(BOY_IDLE_PATH.format(i))
            img = pygame.transform.scale(img, (PLAYER_X_SIZE, PLAYER_Y_SIZE))
            idle_animations.append(img)
        cesta = os.path.dirname(BOY_RIGHT_PATH)
        pocet = sum(1 for f in os.scandir(cesta) if f.is_file() and f.name.endswith(".png"))
        right_animations = [pygame.image.load(BOY_RIGHT_PATH.format(i)) for i in range(1,pocet)]
        right_animations = [pygame.transform.scale(img, (PLAYER_X_SIZE, PLAYER_Y_SIZE)) for img in right_animations]
        left_animations = [pygame.transform.flip(img, True, False) for img in right_animations]
        self.animations = [idle_animations,left_animations, right_animations, ]  # 0 = idle, 1 = right, 2 = left

    if __name__ == "__main__":
        import main