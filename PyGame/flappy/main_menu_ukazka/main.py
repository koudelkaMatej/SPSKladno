import pygame
from settings import *
pygame.init()
pygame.font.init()  # inicializace fontu



font = pygame.font.Font(None, 30)  # inicializace fontu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()  # pro FPS  
clock.tick(FPS)  # FPS
running = True
active_screen = "main_menu"  # proměnná pro sledování aktivní obrazovky
while running:
    if active_screen == "main_menu":
        screen.fill(WHITE)
        startGameText = font.render("Start Game", True, BLACK)
        startGameTextRect = startGameText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-50))
        pygame.draw.rect(screen, BRIGHT_ORANGE, startGameTextRect.inflate(20, 10))  # Add background color
        screen.blit(startGameText, startGameTextRect)

        settingsText = font.render("Settings", True, BLACK)
        settingsTextRect = settingsText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 ))
        pygame.draw.rect(screen, BRIGHT_ORANGE, settingsTextRect.inflate(20, 10))  # Add background color
        screen.blit(settingsText, settingsTextRect)

        exitText = font.render("Exit", True, BLACK)
        exitTextRect = exitText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.draw.rect(screen, BRIGHT_ORANGE, exitTextRect.inflate(20, 10))
        screen.blit(exitText, exitTextRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settingsTextRect.collidepoint(event.pos):
                    active_screen = "settings"
                if exitTextRect.collidepoint(event.pos):
                    running = False

        
    elif active_screen == "settings":
        screen.fill(GRAY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitTextRect.collidepoint(event.pos):
                    active_screen = "main_menu"

    clock.tick(FPS)  # FPS
    pygame.display.flip()
