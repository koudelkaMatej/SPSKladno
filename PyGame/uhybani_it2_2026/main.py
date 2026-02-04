# import pygame package
import pygame
pygame.init()
Icon = pygame.image.load('obrazky/icon.png')
# We use set_icon to set new icon
pygame.display.set_icon(Icon)
screen = pygame.display.set_mode((400, 500))
color1 = "red"
color = (255,255,0)
# Changing surface color


running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    screen.fill(color1)



  
# Drawing Rectangle
    pygame.draw.rect(screen, color, 
                 pygame.Rect(30, 30, 60, 60))

    pygame.display.update()