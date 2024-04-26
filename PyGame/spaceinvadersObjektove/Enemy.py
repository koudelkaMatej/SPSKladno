import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,imagePath,enemySize):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image,enemySize)
        self.rect = self.image.get_rect(center=(x, y)) 
        self.counter = 0
        self.direction = 1  # 1 for right, -1 for left

    def draw(self,screen):
        screen.blit(self.image, self.rect) 

    def update(self):
        self.rect.x += self.direction * 10  # Move based on direction
        self.counter += self.direction  # Update the counter

        if abs(self.counter) >= 7:
            self.direction *= -1
            self.counter = 0
            self.rect.y += 20