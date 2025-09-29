import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 600))

window.fill((255, 255, 255))

circle_positions = []
circle_radius = 60
color = (0, 0, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos #pygame.mouse.get_pos()
            circle_positions.append(position)
    
    if len(circle_positions) % 4 == 0:
        for i in range(0,len(circle_positions),4):
            pygame.draw.polygon(window, (255, 0, 0), [circle_positions[i], circle_positions[i+1],circle_positions[i+2],circle_positions[i+3]],0)
        pygame.display.update()
pygame.quit()