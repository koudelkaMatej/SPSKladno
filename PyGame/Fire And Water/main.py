import pygame
from pygame.locals import *
from settings import *
import random
import os
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fire And Water")
clock = pygame.time.Clock()
levels = []
#mapa - 0 zem(grass) 1 platforma 2 dvere 3 coin 4 ohen 5 voda 6 jed 7 enemy 8 boy 9 girl
# 41 ohen vlevo 49 ohen vpravo 51 voda vlevo 59 voda vpravo 61 jed vlevo 69 jed vpravo 


running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False	

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()
sys.exit()
