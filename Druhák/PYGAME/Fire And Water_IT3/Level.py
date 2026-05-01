import pygame
from settings import *

class Level:   
    def __init__(self):
        self.current_level = 1
        self.level_data = []
        self.dirt_list = []
        self.lava_list = []
        self.water_list = []
        self.__load_level()
        self.dirt_image = pygame.image.load(DIRT_IMAGE_PATH).convert_alpha()
        self.dirt_image = pygame.transform.scale(self.dirt_image, (TILE_SIZE, TILE_SIZE))
        self.lava_image = pygame.image.load(LAVA_IMAGE_PATH).convert_alpha()
        self.lava_image = pygame.transform.scale(self.lava_image, (TILE_SIZE, TILE_SIZE))
        self.water_image = pygame.image.load(WATER_IMAGE_PATH).convert_alpha()
        self.water_image = pygame.transform.scale(self.water_image, (TILE_SIZE, TILE_SIZE))


    def __load_level(self):
        level_data = []
        with open(LEVEL_PATH.format(self.current_level), 'r', encoding='utf-8-sig') as file:
            for line in file:
                row = list(map(int, line.strip().split(';')))
                level_data.append(row)
        self.level_data = level_data
        pocet_radku = len(self.level_data)
        pocet_sloupcu = len(self.level_data[0])

        for radek in range(pocet_radku):
            for sloupec in range(pocet_sloupcu):
                if self.level_data[radek][sloupec] == 1:  # dirt tile
                    self.dirt_list.append(pygame.Rect(sloupec * TILE_SIZE, radek * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if self.level_data[radek][sloupec] == 2:  # lava tile
                    self.lava_list.append(pygame.Rect(sloupec * TILE_SIZE, radek * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if self.level_data[radek][sloupec] == 3:  # water tile
                    self.water_list.append(pygame.Rect(sloupec * TILE_SIZE, radek * TILE_SIZE, TILE_SIZE, TILE_SIZE))


    def draw_level(self,screen):
        pocet_radku = len(self.level_data)
        pocet_sloupcu = len(self.level_data[0])

        for radek in range(pocet_radku):
            for sloupec in range(pocet_sloupcu):
                if self.level_data[radek][sloupec] == 1:  # dirt tile
                    screen.blit(self.dirt_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
                if self.level_data[radek][sloupec] == 2:  # lava tile
                    screen.blit(self.lava_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
                if self.level_data[radek][sloupec] == 3:  # water tile
                    screen.blit(self.water_image, (sloupec * TILE_SIZE, radek * TILE_SIZE))
if __name__ == "__main__":
    import main