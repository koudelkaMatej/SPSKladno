import pygame
from settings import *
from Level import Level

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fire and Water")
clock = pygame.time.Clock()
running = True


dirt_image = pygame.image.load(DIRT_PATH).convert_alpha()
dirt_image = pygame.transform.scale(dirt_image, (TILE_SIZE, TILE_SIZE))
level = Level()

def draw_level():
    pocet_radku = len(level.level_data)
    pocet_sloupcu = len(level.level_data[0])

    for radek in range(pocet_radku):
        for sloupec in range(pocet_sloupcu):
            if level.level_data[radek][sloupec] == 1:  # dirt tile
                screen.blit(dirt_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    screen.fill((0, 0, 0))  # Clear screen with black
    draw_level()
    clock.tick(FPS)

pygame.quit()
