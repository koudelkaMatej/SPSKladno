import pygame
from settings import *

class World():
	def __init__(self, data):
		self.tile_list = []
		#load images
		dirt_img = pygame.image.load(DIRT_IMAGE_PATH)
		grass_img = pygame.image.load(GRASS_IMAGE_PATH)
		lava_img = pygame.image.load(LAVA_IMAGE_PATH)  # Assuming you have a lava image
		coin_img = pygame.image.load(COIN_IMAGE_PATH)  # Assuming you have a coin image
		exit_img = pygame.image.load(EXIT_IMAGE_PATH)  # Assuming you have an exit image
		#lava_kraj_l_img = pygame.image.load('Assets/ohen a voda/lava_kraj/111.png')  # Assuming you have a lava image
	#	lava_kraj_p_img = pygame.transform.flip(lava_kraj_l_img, True, False)  # Flip the image horizontally
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = pygame.image.load(BLOB_IMAGE_PATH)
					img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 6:
					img = pygame.transform.scale(lava_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 7:
					img = pygame.transform.scale(coin_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 8:
					img = pygame.transform.scale(exit_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			#screen = pygame.display.get_surface()
			pygame.display.get_surface().blit(tile[0], tile[1])

if __name__ == "__main__":
    import main
    main.main()