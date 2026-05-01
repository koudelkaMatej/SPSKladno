import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Collision Detection Example")
clock = pygame.time.Clock()
# Player variables
x, y = 250, 250
width, height = 50, 50
hrac = pygame.Rect(x, y, width, height)

# Obstacle variables
x1, y1 = 150, 200
cara1 = pygame.Rect(x1, y1 + 42, 200, 5)
cara2 = pygame.Rect(x1 -150, y1 + 80, 100, 5)
seznamPloch = [cara1,cara2]
# Jump variables
isjump = False
v = 10
m = 1
vf = v

# Game loop
run = True
while run:
    clock.tick(25)
    win.fill((0, 0, 0))
    
    # Draw player
    pygame.draw.rect(win, (255, 0, 0), hrac)
    
    # Draw obstacles
    pygame.draw.rect(win, (255, 255, 0), cara1)
    pygame.draw.rect(win, (255, 255, 0), cara2)

    # Event handling
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False

    # Movement
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_a]:
        hrac.x -= 5
    if keys[pygame.K_d]:
        hrac.x += 5

    # Jump
    if not isjump: 
        if keys[pygame.K_SPACE]: 
            isjump = True

    if isjump: 
        F = (1 / 2) * m * (v ** 2) 
        hrac.y -= F 
        v -= 1
        if v < 0: 
            m = -1
        for cara in seznamPloch:
            if hrac.colliderect(cara): 
                isjump = False
                v = vf - 1
                m = 1
                hrac.bottom = cara.top + 1

    pygame.display.update()
    pygame.time.delay(10) 
    pygame.display.update() 
# closes the pygame window	 
pygame.quit() 
