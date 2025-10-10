import pygame
from pygame.locals import *
from settings import *
from World import World
import random
from Player import Player
import os
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Oheň a voda')

def draw_grid():
	for line in range(0, SCREEN_WIDTH // TILE_SIZE + 1):
		pygame.draw.line(screen, (255, 255, 255), (0, line * TILE_SIZE), (SCREEN_WIDTH, line * TILE_SIZE))
		pygame.draw.line(screen, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, SCREEN_HEIGHT))

# map from csv
with open('mapa.csv', 'r') as f:
	world_data = f.readlines()
	world_data = [list(map(int, row.strip().split(';'))) for row in world_data]

world = World(world_data)

sun_img = pygame.image.load(SUN_IMAGE_PATH)
random_sun_x = random.randint(50, SCREEN_WIDTH - sun_img.get_width() - (SCREEN_WIDTH - world_data[0].count(1) * TILE_SIZE))
bg_img = pygame.image.load(SKY_IMAGE_PATH)

def draw_bg():
	screen.blit(bg_img, (0, 0))
	screen.blit(sun_img, (random_sun_x, 100))

folder_path = PLAYER_IMAGE_IDLE_PATH
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
num_files = len(files)  # Count the number of files
print(num_files)

player = Player()
group_player = pygame.sprite.Group()
group_player.add(player)


run = True
while run:
	draw_bg()
	world.draw()
	group_player.update()
	group_player.draw(screen)
#draw_grid()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.update()
pygame.quit()