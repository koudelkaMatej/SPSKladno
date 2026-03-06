import pygame
from Player import *
from Block import Block
from settings import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()


hrac = Player()
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
blok = Block()
blok_group = pygame.sprite.Group()
blok_group.add(blok)
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hrac_group.update()
    hrac_group.draw(screen)
    blok_group.update()
    blok_group.draw(screen)

    if pygame.sprite.spritecollide(hrac, blok_group, True, pygame.sprite.collide_mask):
        print("KOLIZE!")
        pygame.time.delay(1000)
        running = False

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()