import pygame
from settings import *
from Player import Player
from draw_hp_bar import draw_hp_bar
from Level import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Zelda Like Game')
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()
player = Player(START_X, START_Y)
player_group.add(player)

level = Level()

def draw_level(level, screen):
    pocet_radku = len(level.level_data)
    pocet_sloupcu = len(level.level_data[0])

    for radek in range(pocet_radku):
        for sloupec in range(pocet_sloupcu):
            if level.level_data[radek][sloupec] == 0:  # floor tile
                screen.blit(level.dark_floor_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
            elif level.level_data[radek][sloupec] == 1:  # wall
                screen.blit(level.wall_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
            elif level.level_data[radek][sloupec] == 2:  # light_floor tile
                screen.blit(level.light_floor_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))


        

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_level(level, screen)
    player_group.update(level.walls)
    player_group.draw(screen)

    draw_hp_bar(screen, player.hp)
    if player.alive == False:
        running = False
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
