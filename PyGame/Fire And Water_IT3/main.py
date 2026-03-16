import pygame
from settings import *
from Level import Level
from Fireboy import Fireboy
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fire and Water Game")
clock = pygame.time.Clock()



level = Level()
fireboy = Fireboy(100, 760)
players_group = pygame.sprite.Group()
players_group.add(fireboy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)

    players_group.update()
    players_group.draw(screen)
    level.draw_level(screen)
    if fireboy.rect.collidelist(level.dirt_list) != -1:
        
        fireboy.rect.bottom = level.dirt_list[fireboy.rect.collidelist(level.dirt_list)].top
        fireboy.jumping = False
        fireboy.jump_velocity = 0
        fireboy.on_ground = True
    if fireboy.rect.collidelist(level.dirt_list) == -1:
        fireboy.on_ground = False
        

    pygame.display.flip()
    clock.tick(FPS)