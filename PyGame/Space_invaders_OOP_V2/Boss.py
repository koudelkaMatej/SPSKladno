import pygame
from Enemy import Enemy
import settings
import random as rand
class Boss(Enemy):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.BOSS_SCALE,self.image.get_height()*settings.BOSS_SCALE))
        self.hp = 20

if __name__ == "__main__":
    import main