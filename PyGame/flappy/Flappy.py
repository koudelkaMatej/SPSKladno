import pygame
from settings import *

class Flappy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation_index = 0 # index aktuálního obrázku
        self.animation_interval = 10 #počet snímku do výměny obrázku
        self.animation_timer = 0 #počet snímků, které již proběhly od poslední výměny obrázku
        self.animations = []
        self.animations.append(pygame.image.load("assets/bird1.png").convert_alpha())
        self.animations.append(pygame.image.load("assets/bird2.png").convert_alpha())
        self.animations.append(pygame.image.load("assets/bird3.png").convert_alpha())
        self.animations.append(pygame.image.load("assets/bird2.png").convert_alpha())
        for i in range(len(self.animations)):
            self.animations[i] = pygame.transform.scale(self.animations[i], (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image = self.animations[self.animation_index]
        self.rect = self.image.get_rect(center=(50, SCREEN_HEIGHT // 3))
        self.gravity = 0.3 
        self.jump_strength = -5
        self.velocity = 1

    def update(self):
        self.image = self.animations[self.animation_index]  # aktualizace obrázku na základě indexu
        self.animation_timer += 1 # zvýšení časovače
        if self.animation_timer >= self.animation_interval: # pokud uplynul čas pro výměnu obrázku
            self.animation_index += 1 # zvýšení indexu obrázku
            if self.animation_index >= len(self.animations): # pokud je index větší než počet obrázků v listu
                self.animation_index = 0 # resetuji index na první obrázek
            self.animation_timer = 0 # resetuji časovač
        if self.velocity != 0:  
            self.velocity += self.gravity
            self.rect.y += self.velocity
        if self.rect.y > SCREEN_HEIGHT - 150 - PLAYER_HEIGHT: 
            self.rect.y = SCREEN_HEIGHT - 150 - PLAYER_HEIGHT
            self.velocity = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.velocity != 0:
                self.jump()
        if self.velocity < -2:
            self.image = pygame.transform.rotate(self.animations[self.animation_index], 20)
        elif self.velocity > 2:
            self.image = pygame.transform.rotate(self.animations[self.animation_index], -20)
        else:
            self.image = self.animations[self.animation_index]  # reset to normal position
    def jump(self):
        self.velocity = self.jump_strength

if __name__ == "__main__":
    import main