import pygame
from settings import *
from Level import Level
from Fireboy import Fireboy
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fire and Water Game")
clock = pygame.time.Clock()

dirt_image = pygame.image.load(DIRT_IMAGE_PATH).convert_alpha()
dirt_image = pygame.transform.scale(dirt_image, (TILE_SIZE, TILE_SIZE))
lava_image = pygame.image.load(LAVA_IMAGE_PATH).convert_alpha()
lava_image = pygame.transform.scale(lava_image, (TILE_SIZE, TILE_SIZE))

level = Level()
fireboy = Fireboy(100, 760)
players_group = pygame.sprite.Group()
players_group.add(fireboy)
def draw_level():
    pocet_radku = len(level.level_data)
    pocet_sloupcu = len(level.level_data[0])

    for radek in range(pocet_radku):
        for sloupec in range(pocet_sloupcu):
            if level.level_data[radek][sloupec] == 1:  # dirt tile
                screen.blit(dirt_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
            if level.level_data[radek][sloupec] == 2:  # lava tile
                screen.blit(lava_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)

    players_group.update()
    players_group.draw(screen)
    draw_level()
    pygame.display.flip()
    clock.tick(FPS)