import pygame
from Player import *
from Block import Block
from settings import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()

hrac = Player(WIDTH // 2, HEIGHT)
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
blok = Block(WIDTH // 2, 0)
blok_group = pygame.sprite.Group()
blok_group.add(blok)
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hrac_group.update()
    hrac_group.draw(screen)
    blok_group.update()
    blok_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()