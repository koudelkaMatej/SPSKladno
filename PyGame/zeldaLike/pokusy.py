import pygame
import os
import glob

class Player:
    def __init__(self, image_files):
        self.images = [pygame.image.load(img) for img in image_files]
        self.current_image = 0
        self.image_timer = 0
        self.ANIMATION_TIME = 150
        self.rect = self.images[0].get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        self.image_timer += pygame.time.get_ticks()
        if self.image_timer > self.ANIMATION_TIME:
            self.image_timer = 0
            self.current_image = (self.current_image + 1) % len(self.images)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1

    def draw(self, screen):
        img = self.images[self.current_image]
        img = pygame.transform.scale(img, (img.get_width() // 0.5, img.get_height() // 0.5))
        screen.blit(img, ((self.rect.x - img.get_width() //2, self.rect.y)))

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
image_files = sorted(glob.glob("obrazky/character/sword/attackDown/*.png"))
player = Player(image_files)

# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player
    player.update()

    # Draw everything
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.time.delay(100)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()