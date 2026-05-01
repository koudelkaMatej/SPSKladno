from settings import *
import pygame
pygame.font.init()
# Function to draw the HP bar
def draw_hp_bar_enemies(screen, current_hp,x=0, y=0, max_hp=50):
    # Calculate the width of the health bar based on current HP
    hp_percentage = current_hp / max_hp
    bar_width = int(HP_BAR_WIDTH * hp_percentage)

    # Determine color based on HP percentage
    if hp_percentage > 0.5:
        color = GREEN
    elif hp_percentage > 0.2:
        color = YELLOW
    else:
        color = RED
    # Draw the background of the HP bar
    pygame.draw.rect(screen, BLACK, (x, y + 25, HP_BAR_WIDTH * 0.4, HP_BAR_HEIGHT * 0.2))
    # Draw the current HP
    pygame.draw.rect(screen, color, (x, y + 25, bar_width * 0.4 , HP_BAR_HEIGHT * 0.2))
    # Draw the border
    pygame.draw.rect(screen, WHITE, (x, y + 25, HP_BAR_WIDTH * 0.4, HP_BAR_HEIGHT * 0.2), 1)