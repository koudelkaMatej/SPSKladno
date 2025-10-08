import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, imagePath, blockSize):
        super().__init__()
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (blockSize, blockSize))
        self.rect = self.image.get_rect(center=(x, y))  # Use topleft for positioning
        self.velocity = 5
    def update(self,):
        self.rect.y += self.velocity  # Update the rect's y position
        if self.rect.top > 600: # 600 = vyska obrazovky
            self.kill()  # Remove the sprite from all sprite groups

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the image at the rect's position
