import pygame
from settings import *
from AI_player import AI_player
from Player import Player
from Blob import Blob
from circle_overlap_percentage import circle_overlap_percentage

def kdoCoZere(hrac_group, jidlo_group):
    for hrac in hrac_group:
        for jidlo in jidlo_group:
            overlap = circle_overlap_percentage(hrac.x, hrac.y, hrac.radius, jidlo.x, jidlo.y, jidlo.radius)
            if overlap > 90:
                if hrac.radius >= jidlo.radius+5:
                    hrac.radius += int(jidlo.radius * 0.2)
                    hrac.image = pygame.Surface((hrac.radius * 2, hrac.radius * 2), pygame.SRCALPHA)
                    hrac.image.fill((0, 0, 0, 0))
                    pygame.draw.circle(hrac.image, hrac.color, (hrac.radius, hrac.radius), hrac.radius)
                    jidlo_group.remove(jidlo)
                elif jidlo.radius >= hrac.radius+5:
                    jidlo.radius += int(hrac.radius * 0.2)
                    jidlo.image = pygame.Surface((jidlo.radius * 2, jidlo.radius * 2), pygame.SRCALPHA)
                    jidlo.image.fill((0, 0, 0, 0))
                    pygame.draw.circle(jidlo.image, jidlo.color, (jidlo.radius, jidlo.radius), jidlo.radius)
                    print("sezral jsem", hrac.color)
                    player_group.remove(hrac)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player_colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, WHITE, BLACK]
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_START_SIZE, player_colors.pop())
player_group = pygame.sprite.Group()
player_group.add(player)
blob_group = pygame.sprite.Group()
ai_group = pygame.sprite.Group()
ai1 = AI_player(-100,-100,30,player_colors.pop())
ai2 = AI_player(200,200,30,player_colors.pop())
ai_group.add(ai1)
ai_group.add(ai2)



GENERATE_BLOBS = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATE_BLOBS, 5000)

scroolx_speed = PLAYER_SPEED
scrooly_speed = PLAYER_SPEED


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
    # Move the player towards the mouse position and scrool the screen if necessary

    player_group.update(mouse_x, mouse_y)
    player_group.draw(screen)

    ai_group.update(mouse_x, mouse_y)
    ai_group.draw(screen)
    if mouse_x < 100:
        for sprite in player_group.sprites() + ai_group.sprites() + blob_group.sprites():
            sprite.rect.centerx += scroolx_speed   # update pro blob
            sprite.x += scroolx_speed   # nova souradnice hracu
    elif mouse_x > SCREEN_WIDTH - 100:
        for sprite in player_group.sprites() + ai_group.sprites() + blob_group.sprites():
            sprite.rect.centerx -= scroolx_speed
            sprite.x -= scroolx_speed   
    if mouse_y < 100:
        for sprite in player_group.sprites() + ai_group.sprites() + blob_group.sprites():
            sprite.rect.centery += scrooly_speed
            sprite.y += scroolx_speed   
    elif mouse_y > SCREEN_HEIGHT - 100:
        for sprite in player_group.sprites() + ai_group.sprites() + blob_group.sprites():
            sprite.rect.centery -= scrooly_speed
            sprite.y -= scroolx_speed   
    kdoCoZere(player_group,blob_group)
    kdoCoZere(ai_group,blob_group)
    kdoCoZere(player_group,ai_group)
    kdoCoZere(ai_group,ai_group)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
