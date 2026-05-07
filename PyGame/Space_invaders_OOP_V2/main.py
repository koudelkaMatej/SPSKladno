import pygame
import settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Boss import Boss
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
clock = pygame.time.Clock()

# vytvoření group a hráče
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
enemy_group = pygame.sprite.Group()


level = 2 #start level 2
def create_lvl(level):# generovani nepratel pro první level
    if level > 5:
        enemy = Boss(150, 25)
        enemy_group.add(enemy)
    else:
        x = 75
        y = 25
        for i in range(level):
            for j in range(level*2): 
                enemy = Enemy(x,y)
                x += 50
                enemy_group.add(enemy)
            y += 50
            x = 75
create_lvl(level)

running = True
while running:
    clock.tick(settings.FPS)  # Limit to 45 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player.cooldown == 0: #kontrola pro střelbu, jestli je cooldown 0, tak můžeme střílet
        bullet = Bullet(player.rect.left + 5,player.rect.top + 40,"Player")
        player_bullet_group.add(bullet)
        bullet = Bullet(player.rect.right - 5,player.rect.top + 40,"Player")
        player_bullet_group.add(bullet)
        player.cooldown = pygame.time.get_ticks()
    for enemy in enemy_group:
        if enemy.check_if_enemy_shoot():
            bullet = Bullet(enemy.rect.centerx,enemy.rect.bottom)
            enemy_bullet_group.add(bullet)
        
    screen.fill(settings.BG_COLOR)
    player_group.update()
    player_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)

    # kontrola kolize mezi kulkami a hráčem
    if pygame.sprite.groupcollide(player_group, enemy_bullet_group, True, True, collided = pygame.sprite.collide_mask):
        print("Player hit!")
        running = False
    # kontrola kolize mezi střelou hráče a nepřáteli
    if pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, True, collided = pygame.sprite.collide_mask):
        if enemy.hp > 1:
            enemy.hp -= 1
            print("Enemy hit! HP left:", enemy.hp)
        else:
            enemy.kill()
            print("Enemy shotted down!")
        if len(enemy_group) == 0:
            level += 1
            create_lvl(level) 
    if pygame.sprite.groupcollide(enemy_group, player_group, True, True, collided = pygame.sprite.collide_mask):
        print("Player hit by enemy!")
        running = False


    pygame.display.flip()
pygame.quit()