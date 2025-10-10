import pygame
pygame.init() 

width_of_window = 600
height_of_window = 600
pygame.display.set_mode((width_of_window,height_of_window))

running  = True
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False