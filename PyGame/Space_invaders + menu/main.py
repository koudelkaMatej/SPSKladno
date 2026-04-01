import pygame
import settings
from Player import *
from Enemy import *
pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
running = True
clock = pygame.time.Clock()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

def vypis_menu():
    screen.fill((0, 0, 127))
    screen.blit(settings.title_text, settings.title_rect)
    screen.blit(settings.play_text, settings.play_rect)
    screen.blit(settings.settings_text, settings.settings_rect)
    screen.blit(settings.quit_text, settings.quit_rect)
def vypis_settings():
    screen.fill((0, 0, 127))
    screen.blit(settings.res800_text, settings.res800_rect)
    screen.blit(settings.res1024_text, settings.res1024_rect)
    screen.blit(settings.res1280_text, settings.res1280_rect)
    screen.blit(settings.back_text, settings.back_rect)

def vypis_hru():
    screen.fill((0, 0, 0))
    player_group.update()
    player_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    bullet_group.update()
    bullet_group.draw(screen)

state = "MENU"   # MENU, PLAYING, PAUSED, GAME_OVER
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "MENU":
                if settings.play_rect.collidepoint(event.pos):
                    state = "PLAYING"
                    player = Player()  # vytvoření hráče
                    player_group.add(player)
                    enemy_group.add(*[Enemy(x*100, 50) for x in range(5)])  # vytvoření nepřátel
                    for i in range(3):
                        screen.fill((0, 0, 0))
                        text = settings.menu_font.render(f"Starting in {3-i}...", True, (255, 255, 255))
                        text_rect = text.get_rect(center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))
                        screen.blit(text, text_rect)
                        pygame.display.flip()
                        pygame.time.delay(1000)
                elif settings.settings_rect.collidepoint(event.pos):
                    state = "SETTINGS"
                elif settings.quit_rect.collidepoint(event.pos):
                    running = False
            elif state == "SETTINGS":
                if settings.res800_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 800, 600
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                    settings.update_rects()
                elif settings.res1024_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 1024, 768
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                    settings.update_rects()
                elif settings.res1280_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 1280, 960
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                    settings.update_rects()
                elif settings.back_rect.collidepoint(event.pos):
                    state = "MENU"
    if state == "MENU":
        vypis_menu()
    elif state == "PLAYING":
        vypis_hru()
    elif state == "SETTINGS":
        vypis_settings()
    elif state == "GAME_OVER":
        # zobrazení skóre, restart
        pass
    pygame.display.flip()
    clock.tick(settings.FPS)
pygame.quit()