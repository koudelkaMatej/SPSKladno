import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, imagePath, playerSize,width,height):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image,playerSize)
        self.rect = self.image.get_rect(center=(x, y)) 
        self.screenWidth = width
        self.screenHeight = height

    def move(self,direction):
        if direction == "left":
            if self.rect.x > 5:
                self.rect.x -= 5
        elif direction == "right":
            if self.rect.x < self.screenHeight - 10:
                self.rect.x += 5        
                
    def draw(self,screen):
        screen.blit(self.image, self.rect) 

    def explosion(self,screen):
        exploze = pygame.image.load("spaceinvadersObjektove/obr/0exploze.png")
        exploze = pygame.transform.scale(self.image,(40,40))
        screen.blit(exploze,self.rect)
        pygame.time.delay(5000)
