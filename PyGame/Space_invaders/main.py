import pygame
from settings import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
running = True
def vypis_menu():
    screen.fill((0, 0, 127))
    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(settings_text, settings_rect)
    screen.blit(quit_text, quit_rect)
def vypis_settings():
    screen.fill((0, 0, 127))
    screen.blit(res800_text, res800_rect)
    screen.blit(res1024_text, res1024_rect)
    screen.blit(res1280_text, res1280_rect)
    screen.blit(back_text, back_rect)
state = "MENU"   # MENU, PLAYING, PAUSED, GAME_OVER
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "MENU":
                if play_rect.collidepoint(event.pos):
                    state = "PLAYING"
                elif settings_rect.collidepoint(event.pos):
                    state = "SETTINGS"
                elif quit_rect.collidepoint(event.pos):
                    running = False
            elif state == "SETTINGS":
                if res800_rect.collidepoint(event.pos):
                    screen = pygame.display.set_mode((800, 600))
                elif res1024_rect.collidepoint(event.pos):
                    screen = pygame.display.set_mode((1024, 768))
                elif res1280_rect.collidepoint(event.pos):
                    screen = pygame.display.set_mode((1280, 960))
                elif back_rect.collidepoint(event.pos):
                    state = "MENU"
    if state == "MENU":
        vypis_menu()
    elif state == "PLAYING":
        # herní logika
        pass
    elif state == "SETTINGS":
        vypis_settings()
    elif state == "GAME_OVER":
        # zobrazení skóre, restart
        pass
    pygame.display.flip()
pygame.quit()