import pygame
import settings
import random as rand
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,kdo_vystrelil = "alien"): #když nezadám kdo_vystrelil, tak střílí alien
        super().__init__()
        self.kdo_vystrelil = kdo_vystrelil
        if kdo_vystrelil == "alien":
            self.image = pygame.image.load(settings.ENEMY_BULLET_IMAGE_PATH).convert_alpha()
            self.rect = self.image.get_rect(top=y,centerx = x) # center = (x,y)¨
            self.speed = settings.ENEMY_BULLET_SPEED
        else:
            self.image = pygame.image.load(settings.PLAYER_BULLET_IMAGE_PATH).convert_alpha()
            self.rect = self.image.get_rect(bottom=y,centerx = x) # center = (x,y)¨
            self.speed = settings.PLAYER_BULLET_SPEED * -1 # hráč střílí nahoru, takže rychlost je záporná

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > settings.SCREEN_HEIGHT: #kontrola pro oba hráče
            self.kill()



if __name__ == "__main__":
    import main