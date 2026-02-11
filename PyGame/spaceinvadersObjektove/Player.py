import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, imagePath, playerSize,width,height):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image,playerSize)
        self.rect = self.image.get_rect(center=(x, y)) 
        self.screenWidth = width
        self.screenHeight = height
        self.explosion_frames = [pygame.image.load(f"obr/{i}exploze.png") for i in range(6)]
        self.explosion_index = 0
        self.explosion_duration = 100  # Time between each frame in milliseconds
        self.last_explosion_update = pygame.time.get_ticks()

    def move(self,direction):
        if direction == "left":
            if self.rect.x > 5:
                self.rect.x -= 5
        elif direction == "right":
            if self.rect.x < self.screenHeight - 10:
                self.rect.x += 5        
                
    def draw(self,screen):
        screen.blit(self.image, self.rect) 

    def explosion(self, screen):
        for i in range(6):
            pygame.time.wait(100)
            current_time = pygame.time.get_ticks()
            if current_time - self.last_explosion_update > self.explosion_duration:
                self.last_explosion_update = current_time
                if self.explosion_index < len(self.explosion_frames) - 1:
                    self.explosion_index += 1
            exploze = self.explosion_frames[self.explosion_index]
            exploze = pygame.transform.scale(exploze, (80, 80))
            screen.blit(exploze, self.rect)
            pygame.display.flip()
            pygame.time.wait(50)