import pygame

pygame.init()
clock = pygame.time.Clock()  # pro FPS
screen = pygame.display.set_mode((400, 600))

running = True
a = 50
b = 200  # vykreslím a už neměním (statické části)
vlevo = False
ball = pygame.image.load('ball_image.png')  # NAČTENÍ OBRÁZKU
ball = pygame.transform.scale(ball, (40, 40))  # menim velikost obrazku
rotation_angle = 0
while running:  # vše co je zde měním dynamicky dle ticku
    clock.tick(60)  # FPS
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Rotate the ball image
    rotated_ball = pygame.transform.rotate(ball, rotation_angle)
    ball_rect = rotated_ball.get_rect(center=(a, b))

    screen.blit(rotated_ball, ball_rect)  # vykreslení rotovaného obrázku
    pygame.draw.line(screen, (255, 102, 0), [25, b+20], [370, b+20], 5)

    if vlevo:
        a -= 1
        rotation_angle += 15  # Rotate clockwise 
        if a <= 50:
            vlevo = False
    else:
        a += 1
        rotation_angle -= 15  # Rotate counterclockwise
        if a >= 350:
            vlevo = True

    pygame.display.update()

pygame.quit()
