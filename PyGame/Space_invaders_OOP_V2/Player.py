import pygame
import settings
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.PLAYER_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
        self.rect = self.image.get_rect(bottom=settings.SCREEN_HEIGHT, centerx=settings.SCREEN_WIDTH // 2) # center = (x,y)¨
        self.speed = settings.PLAYER_SPEED 
        self.cooldown = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed   
        if keys[pygame.K_RIGHT] and self.rect.right < settings.SCREEN_WIDTH:
            self.rect.x += self.speed
        #shooting kontrola
        if self.cooldown + 1000 < pygame.time.get_ticks():
            self.cooldown = 0

if __name__ == "__main__":
    import main