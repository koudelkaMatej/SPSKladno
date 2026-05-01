import pygame
from settings import *
from Level import Level
from Fireboy import Fireboy
from WaterGirl import WaterGirl
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fire and Water Game")
clock = pygame.time.Clock()



level = Level()
fireboy = Fireboy(100, 760)
watergirl = WaterGirl(300, 760)
players_group = pygame.sprite.Group()
players_group.add(fireboy)
players_group.add(watergirl)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)

    players_group.update()
    players_group.draw(screen)
    level.draw_level(screen)
    #collision detection between players and dirt tiles 
    for player in players_group:
        if player.rect.collidelist(level.dirt_list) != -1: 
            if player.jump_velocity < 0:  # ceiling collision
                player.rect.top = level.dirt_list[player.rect.collidelist(level.dirt_list)].bottom
                player.jump_velocity = 0
            else:
                player.rect.bottom = level.dirt_list[player.rect.collidelist(level.dirt_list)].top
                player.on_ground = True
        else:
            player.on_ground = False   
        if player.rect.collidelist(level.lava_list) != -1:
            player.check_lava_collision(level)
            player.check_water_collision(level)
            running = player.water_lava_interaction(level)




    pygame.display.flip()
    clock.tick(FPS)