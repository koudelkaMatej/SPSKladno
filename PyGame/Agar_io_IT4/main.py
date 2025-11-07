import pygame
from settings import *
from Player import Player
from Blob import Blob
from circle_overlap_percentage import circle_overlap_percentage
from Player_AI import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player_colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, WHITE, BLACK]
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_START_SIZE, player_colors.pop())
player_group = pygame.sprite.Group()
player_group.add(player)
blob_group = pygame.sprite.Group()
ai_group = pygame.sprite.Group()

player_ai = Player_AI(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_START_SIZE, player_colors.pop())
player_group.add(player_ai)
ai_group.add(player_ai)


GENERATE_BLOBS = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATE_BLOBS, 1000)

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
        for player in player_group:
                overlap = circle_overlap_percentage(player.rect.centerx, player.rect.centery, player.radius, blob.x, blob.y, blob.radius)
                if overlap > 90:
                    if player.radius >= blob.radius+5:
                        player.radius += int(blob.radius * 0.2)
                        blob_group.remove(blob)
    
    for ai in ai_group:
        for player in player_group:
                overlap = circle_overlap_percentage(player.rect.centerx, player.rect.centery, player.radius, ai.rect.centerx, ai.rect.centery, ai.radius)
                if overlap > 90 and player != ai:
                    if player.radius >= ai.radius+5:
                        player.radius += int(ai.radius * 0.2)
                        player_group.remove(ai)
                        ai_group.remove(ai)
                overlap = circle_overlap_percentage(ai.rect.centerx, ai.rect.centery, ai.radius,player.rect.centerx, player.rect.centery, player.radius)
                if overlap > 90 and player != ai:
                    if ai.radius >= player.radius+5:
                        ai.radius += int(player.radius * 0.2)
                        player_group.remove(player)
                        ai_group.remove(player)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
