import pygame
import Button

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load Button images
start_img = pygame.image.load("D:\SPS - programovani\GitHub SPS\SPSKladno\PyGame\mainMenu\exit_btn.png").convert_alpha()
exit_img = pygame.image.load('D:\SPS - programovani\GitHub SPS\SPSKladno\PyGame\mainMenu\start_btn.png').convert_alpha()

#create Button instances
start_Button = Button.Button(100, 200, start_img, 0.8)
exit_Button = Button.Button(450, 200, exit_img, 0.8)

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	if start_Button.draw(screen):
		print('START')
	if exit_Button.draw(screen):
		print('EXIT')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()