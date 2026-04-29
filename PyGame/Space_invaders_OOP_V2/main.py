import pygame
import settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

enemy_group = pygame.sprite.Group()
def create_enemies():
    x = 75
    y = 25
    for i in range(2):
        for j in range(5): 
            enemy = Enemy(x,y)
            x += 50
            enemy_group.add(enemy)
        y += 50
        x = 75
create_enemies()


running = True
while running:
    clock.tick(settings.FPS)  # Limit to 45 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_SPACE and player.cooldown == 0:
                bullet = Bullet(player.rect.left + 5,player.rect.top + 40,"Player")
                player_group.add(bullet)
                bullet = Bullet(player.rect.right - 5,player.rect.top + 40,"Player")
                player_group.add(bullet)
                player.cooldown = pygame.time.get_ticks()
    screen.fill(settings.BG_COLOR)
    player_group.update()
    player_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.flip()
pygame.quit()