import pygame
from settings import *

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.head = pygame.image.load(HEAD_IMAGE_PATH).convert_alpha()
        self.body = pygame.image.load(BODY_IMAGE_PATH).convert_alpha()
        self.tail = pygame.image.load(TAIL_IMAGE_PATH).convert_alpha()
        self.head = pygame.transform.scale(self.head, (CELL_SIZE, CELL_SIZE))
        self.body = pygame.transform.scale(self.body, (CELL_SIZE, CELL_SIZE))
        self.tail = pygame.transform.scale(self.tail, (CELL_SIZE, CELL_SIZE))
        self.body_coords = [(200,200), (180,200), (160,200)] # head - body - tail

        #self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        #self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH // 2, SCREEN_HEIGTH // 2))
        self.direction = pygame.Vector2(0, 0)
        self.speed = CELL_SIZE


    def update(self):
        #self.rect.x += self.direction.x * self.speed
       # self.rect.y += self.direction.y * self.speed
       pass

    def draw(self, screen):
        for index, (x, y) in enumerate(self.body_coords):
            if index == 0:
                screen.blit(self.head, (x, y))
            elif index == len(self.body_coords) - 1:
                screen.blit(self.tail, (x, y))
            else:
                screen.blit(self.body, (x, y))