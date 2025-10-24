import pygame
from settings import *
from Player import Player
from Blob import Blob
from circle_overlap_percentage import circle_overlap_percentage

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player_colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, WHITE, BLACK]
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_START_SIZE, player_colors.pop())
player_group = pygame.sprite.Group()
player_group.add(player)
blob_group = pygame.sprite.Group()

GENERATE_BLOBS = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATE_BLOBS, 5000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == GENERATE_BLOBS:
            for i in range(5):
                blob_group.add(Blob())

                
    screen.fill(PINK)
    blob_group.draw(screen)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    player_group.update(mouse_x, mouse_y)
    player_group.draw(screen)

    for blob in blob_group:
        overlap = circle_overlap_percentage(player.x, player.y, player.radius, blob.x, blob.y, blob.radius)
        if overlap > 90:
            if player.radius >= blob.radius+5:
                player.radius += int(blob.radius * 0.2)
                player.image = pygame.Surface((player.radius * 2, player.radius * 2), pygame.SRCALPHA)
                player.image.fill((0, 0, 0, 0))
                pygame.draw.circle(player.image, player.color, (player.radius, player.radius), player.radius)
                blob_group.remove(blob)



    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
