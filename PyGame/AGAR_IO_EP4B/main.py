import pygame
from settings import *
from Player import *
from Blob import *
from circle_overlap_percentage import *
from overlap_percentage import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BLACK)
player_group = pygame.sprite.Group()
player_group.add(player)

GENERATE_FOOD = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATE_FOOD, 2000)
food_group = pygame.sprite.Group()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == GENERATE_FOOD:
            for i in range(5):
                food_group.add(Blob())

    screen.fill(PINK)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    food_group.draw(screen)
    player_group.draw(screen)
    player_group.update(mouse_x, mouse_y)

    for blob in food_group:
        overlap = circle_overlap_percentage(player.rect.centerx, player.rect.centery, player.radius, blob.rect.centerx, blob.rect.centery, blob.radius)
        #overlap = overlap_percentage(player.rect.centerx, player.rect.centery, player.radius, blob.rect.centerx, blob.rect.centery, blob.radius)
        if overlap > 70:
            if player.radius >= blob.radius+5:
                player.radius += int(blob.radius * 0.2)
                player.image = pygame.Surface((player.radius * 2, player.radius * 2), pygame.SRCALPHA)
                player.image.fill((0, 0, 0, 0))
                pygame.draw.circle(player.image, player.color, (player.radius, player.radius), player.radius)
                food_group.remove(blob)



    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()