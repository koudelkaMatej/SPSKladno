import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, imagePath, playerSize):
        super().__init__()
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (playerSize, playerSize))
        self.rect = self.image.get_rect(center=(x, y)) 

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.x > 5:
                self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            if self.rect.x < 335:
                self.rect.x += 5      
                
    def draw(self,screen):
        screen.blit(self.image, self.rect) 
