import pygame
from pygame.locals import *
from settings import *
import os


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.animations = []
		for i in range(1, 5):
			a = pygame.image.load(PLAYER_IMAGE_PATH.format(i)).convert_alpha()
			a = pygame.transform.scale(a, (PLAYER_WIDTH, PLAYER_HEIGHT))
			self.animations.append(a)
		self.current_frame = 0
		self.image = self.animations[self.current_frame].convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 1000 - (SCREEN_WIDTH - TILE_SIZE - PLAYER_WIDTH)
		self.rect.y = 880
		self.speed = PLAYER_SPEED
		self.on_ground = True
		self.m = 1
		self.jumping_power = PLAYER_JUMPING_POWER


	def update(self):
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.rect.x -= self.speed
		if keys[K_RIGHT]:
			self.rect.x += self.speed

		if keys[K_UP] and self.on_ground:
			self.on_ground = False
			
		if not self.on_ground:
			F = (1 / 2) * self.m * (self.jumping_power ** 2) 
			self.jumping_power -= 1
			if self.jumping_power < 0: 
				self.m = -1
			if self.jumping_power < -PLAYER_JUMPING_POWER:
				self.on_ground = True
				self.jumping_power = PLAYER_JUMPING_POWER
				self.m = 1
			self.rect.y -= int(F) 

if __name__ == "__main__":
	import main
	main.main()