import pygame
from settings import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Snake")
#pygame.display.set_icon(pygame.image.load('assets/snake_icon.png'))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    start_game_text = font.render("Start Game", True, GREEN)
    settings_text = font.render("Settings", True, BLUE)
    quit_game_text = font.render("Quit Game", True, RED)
    screen.blit(start_game_text, (SCREEN_WIDTH // 2 - start_game_text.get_width() // 2, 150))
    screen.blit(settings_text, (SCREEN_WIDTH // 2 - settings_text.get_width() // 2, 300))
    screen.blit(quit_game_text, (SCREEN_WIDTH // 2 - quit_game_text.get_width() // 2, 450))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
