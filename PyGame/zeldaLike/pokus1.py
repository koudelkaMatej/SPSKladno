import pygame
from settings import *
from Player import Player
from Skeleton import Skeleton
from draw_hp_bar import draw_hp_bar, draw_stamina_bar
from draw_hp_bar_enemies import draw_hp_bar_enemies
from Level import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Zelda Like Game')
clock = pygame.time.Clock()

level = Level()

def create_level_surface(level):
    """Pre-render the entire level to a single surface (called once)"""
    pocet_radku = len(level.level_data)
    pocet_sloupcu = len(level.level_data[0])
    surface = pygame.Surface((pocet_sloupcu * TILE_SIZE, pocet_radku * TILE_SIZE))

    for radek in range(pocet_radku):
        for sloupec in range(pocet_sloupcu):
            if level.level_data[radek][sloupec] == 0:  # floor tile
                surface.blit(level.dark_floor_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
            elif level.level_data[radek][sloupec] == 1:  # wall
                surface.blit(level.wall_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
            elif level.level_data[radek][sloupec] == 2:  # light_floor tile
                surface.blit(level.light_floor_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
            elif level.level_data[radek][sloupec] == 55:  # skeleton spawn (draw as floor)
                surface.blit(level.dark_floor_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
    return surface

level_surface = create_level_surface(level)

player_group = pygame.sprite.Group()
player = Player(START_X, START_Y)
player_group.add(player)

enemy_group = pygame.sprite.Group()
def spawn_enemies(level, enemy_group):
    positions = level.monster_positions
    for pos in positions["Skeletons"]:
        skeleton = Skeleton(pos[0], pos[1])
        skeleton.hitbox.center = pos  # Sync hitbox with spawn position
        skeleton.target_player = player  # Set player as target
        enemy_group.add(skeleton)
spawn_enemies(level, enemy_group)



        

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(level_surface, (0, 0))
    player_group.update(level.walls)
    player_group.draw(screen)
    enemy_group.update(level.walls)
    enemy_group.draw(screen)
    draw_hp_bar(screen, player.hp)
    draw_stamina_bar(screen, player.stamina)
    if player.is_alive == False:
        running = False
    for enemy in enemy_group:
        draw_hp_bar_enemies(screen, enemy.hp, enemy.rect.centerx-35, enemy.rect.centery+20)
        if enemy.attack_animation_played:
            attack_rect = enemy.get_attack_hitbox()
            if attack_rect.colliderect(player.hitbox):
                player.set_damage(enemy.get_damage())
    
    # check if player is attacking and collides with enemy
    if player.attack_animation_played:
        attack_rect = player.get_attack_hitbox()
        for enemy in enemy_group:
            if attack_rect.colliderect(enemy.hitbox):
                enemy.set_damage(player.get_damage())
             
    
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())

pygame.quit()
