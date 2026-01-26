import pygame
from settings import *
from Player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Zelda Like Game')
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()
player = Player(START_X, START_Y)
player_group.add(player)

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_group.update()
    player_group.draw(screen)



    if player.alive == False:
        running = False
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
