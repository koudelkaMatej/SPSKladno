from settings import *
import pygame
pygame.font.init()
# Function to draw the HP bar
def draw_hp_bar(screen, current_hp, max_hp=100):
    # Calculate the width of the health bar based on current HP
    hp_percentage = current_hp / max_hp
    bar_width = int(HP_BAR_WIDTH * hp_percentage)

    # Determine color based on HP percentage
    if current_hp > max_hp * 0.5:
        color = GREEN
    elif current_hp > max_hp * 0.2:
        color = YELLOW
    else:
        color = RED

    text_font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    hp_text = text_font.render(f'HP: {current_hp}/{max_hp}', True, WHITE)
    screen.blit(hp_text, (50, 25))
    # Draw the background of the HP bar
    pygame.draw.rect(screen, BLACK, (50, 50, HP_BAR_WIDTH, HP_BAR_HEIGHT))
    # Draw the current HP
    pygame.draw.rect(screen, color, (50, 50, bar_width, HP_BAR_HEIGHT))
    # Draw the border
    pygame.draw.rect(screen, WHITE, (50, 50, HP_BAR_WIDTH, HP_BAR_HEIGHT), 1)

def draw_stamina_bar(screen, current_stamina, max_stamina=100):
    stamina_percentage = current_stamina / max_stamina
    bar_width = int(STAMINA_BAR_WIDTH * stamina_percentage)

    text_font = pygame.font.Font(FONT_NAME, FONT_SIZE - 4)
    stamina_text = text_font.render(f'ST: {current_stamina}/{max_stamina}', True, WHITE)
    screen.blit(stamina_text, (50, 72))
    # Background
    pygame.draw.rect(screen, BLACK, (50, 90, STAMINA_BAR_WIDTH, STAMINA_BAR_HEIGHT))
    # Current stamina
    pygame.draw.rect(screen, BLUE, (50, 90, bar_width, STAMINA_BAR_HEIGHT))
    # Border
    pygame.draw.rect(screen, WHITE, (50, 90, STAMINA_BAR_WIDTH, STAMINA_BAR_HEIGHT), 1)
