import pygame
from settings import *
# Slider Class
class Slider:
    def __init__(self, x, y, width, height, min_val=0.0, max_val=1.0, initial_val=0.5):
        self.rect = pygame.Rect(x, y, width, height)  # Slider track
        self.handle_rect = pygame.Rect(x + (initial_val * width), y - height // 2, height, height)  # Slider handle
        self.min_val = min_val
        self.max_val = max_val
        self.value = MUSIC_VOLUME
        self.dragging = False

    def draw(self, screen):
        # Draw the slider track
        pygame.draw.rect(screen, GRAY, self.rect)
        # Draw the slider handle
        pygame.draw.ellipse(screen, BRIGHT_ORANGE, self.handle_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                # Move the handle within the slider track
                self.handle_rect.x = max(self.rect.x, min(event.pos[0], self.rect.x + self.rect.width - self.handle_rect.width))
                # Update the slider value
                self.value = (self.handle_rect.x - self.rect.x) / self.rect.width

    def get_value(self):
        # Return the current value scaled to the range [min_val, max_val]
        return self.min_val + (self.value * (self.max_val - self.min_val))