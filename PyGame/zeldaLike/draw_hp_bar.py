from settings import *
import pygame
pygame.font.init()
# Function to draw the HP bar
def draw_hp_bar(screen, current_hp):
    # Calculate the width of the health bar based on current HP
    hp_percentage = current_hp / 100
    bar_width = int(HP_BAR_WIDTH * hp_percentage)

    # Determine color based on HP percentage
    if current_hp > 50:
        color = GREEN
    elif current_hp > 20:
        color = YELLOW
    else:
        color = RED

    text_font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    hp_text = text_font.render(f'HP: {current_hp}/100', True, WHITE)
    screen.blit(hp_text, (50, 25))
    # Draw the background of the HP bar
    pygame.draw.rect(screen, BLACK, (50, 50, HP_BAR_WIDTH, HP_BAR_HEIGHT))
    # Draw the current HP
    pygame.draw.rect(screen, color, (50, 50, bar_width, HP_BAR_HEIGHT))
    # Draw the border
    pygame.draw.rect(screen, WHITE, (50, 50, HP_BAR_WIDTH, HP_BAR_HEIGHT), 2)
