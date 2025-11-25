import pygame
from settings import *
from Apple import Apple
from Snake import Snake
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Snake")
#pygame.display.set_icon(pygame.image.load('assets/snake_icon.png'))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 74)

start_game_text = font.render("Start Game", True, GREEN)
settings_text = font.render("Settings", True, BLUE)
quit_game_text = font.render("Quit Game", True, RED)
resolution_600x600_text = font.render("600x600", True, RED)
resolution_800x800_text = font.render("800x800", True, RED)
resolution_1000x1000_text = font.render("1000x1000", True, RED)
back_to_menu_text = font.render("Back to Menu", True, YELLOW)
def kalibrate_text_rects():
    global start_game_text_rect, settings_text_rect, quit_game_text_rect, back_to_menu_text_rect
    global resolution_600x600_text_rect, resolution_800x800_text_rect, resolution_1000x1000_text_rect, screen
    start_game_text_rect = start_game_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGTH // 5))
    settings_text_rect = settings_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGTH // 2))
    quit_game_text_rect = quit_game_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGTH //1.2))
    back_to_menu_text_rect = back_to_menu_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGTH //1.2))
    resolution_600x600_text_rect = settings_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGTH // 2))
    resolution_800x800_text_rect = settings_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGTH // 3))
    resolution_1000x1000_text_rect = settings_text.get_rect(center=(SCREEN_WIDTH // 2 - 30, SCREEN_HEIGTH // 5.2))
kalibrate_text_rects()
running = True

def settings_menu():
    settings_running = True
    global screen, SCREEN_WIDTH, SCREEN_HEIGTH
    while settings_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_menu_text_rect.collidepoint(event.pos):
                    settings_running = False
                elif resolution_600x600_text_rect.collidepoint(event.pos):
                    print("600x600 selected")
                    SCREEN_WIDTH, SCREEN_HEIGTH = 600, 600
                elif resolution_800x800_text_rect.collidepoint(event.pos):
                    print("800x800 selected")
                    SCREEN_WIDTH, SCREEN_HEIGTH = 800, 800
                elif resolution_1000x1000_text_rect.collidepoint(event.pos):
                    print("1000x1000 selected")
                    SCREEN_WIDTH, SCREEN_HEIGTH = 1000, 1000
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
                kalibrate_text_rects()

        screen.fill(BLACK)
        pygame.draw.rect(screen, PINK, resolution_600x600_text_rect.inflate(20, 10))
        screen.blit(resolution_600x600_text, resolution_600x600_text_rect)
        pygame.draw.rect(screen, PINK, resolution_800x800_text_rect.inflate(20, 10))
        screen.blit(resolution_800x800_text, resolution_800x800_text_rect)
        pygame.draw.rect(screen, PINK, resolution_1000x1000_text_rect.inflate(20, 10))
        screen.blit(resolution_1000x1000_text, resolution_1000x1000_text_rect)
        screen.blit(back_to_menu_text, back_to_menu_text_rect)

        pygame.display.flip()
        clock.tick(FPS)


##############################
apple_red_group = pygame.sprite.Group()
apple_green_group = pygame.sprite.Group()
snake_group = pygame.sprite.Group()
apple_red_group.add(Apple(RED_APPLE_IMAGE_PATH))
generate_green_food = pygame.USEREVENT + 1
pygame.time.set_timer(generate_green_food, 15000)
snake = Snake()
snake_group.add(snake)

def main_game_menu():
    green_apple_elapsed_time = 0
    game_menu_running = True
    
    while game_menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_menu_running = False
            if event.type == generate_green_food:
                apple_green_group.add(Apple(GREEN_APPLE_IMAGE_PATH))
                green_apple_elapsed_time = pygame.time.get_ticks()
        if green_apple_elapsed_time + 10000 < pygame.time.get_ticks():
            apple_green_group.empty()
        if len(apple_red_group) == 0:
            apple_red_group.add(Apple(RED_APPLE_IMAGE_PATH))
        
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            for apple in apple_red_group:
                if apple.rect.collidepoint(mouse_pos):
                    apple_red_group.remove(apple)
            for apple in apple_green_group:
                if apple.rect.collidepoint(mouse_pos):
                    apple_green_group.remove(apple)
        screen.fill(BLACK)
        apple_red_group.draw(screen)
        apple_green_group.draw(screen)
        snake.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)


##############################
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_game_text_rect.collidepoint(event.pos):
                print("Start Game clicked")
                main_game_menu()
            elif settings_text_rect.collidepoint(event.pos):
                print("Settings clicked")
                settings_menu()
            elif quit_game_text_rect.collidepoint(event.pos):
                running = False
    screen.fill(BLACK)
    screen.blit(start_game_text, start_game_text_rect)
    screen.blit(settings_text, settings_text_rect)
    screen.blit(quit_game_text, quit_game_text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
