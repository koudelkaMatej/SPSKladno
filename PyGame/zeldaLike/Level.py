import pygame
from settings import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))

class Level:   
    def __init__(self):
        self.current_level = 1
        self.level_data = []
        self.load_level()
        self.dark_floor_image = pygame.image.load(FLOOR_DARK_IMAGE_PATH).convert()
        self.dark_floor_image = pygame.transform.scale(self.dark_floor_image, (TILE_SIZE, TILE_SIZE))
        self.light_floor_image = pygame.image.load(FLOOR_LIGHT_IMAGE_PATH).convert()
        self.light_floor_image = pygame.transform.scale(self.light_floor_image, (TILE_SIZE, TILE_SIZE))
        self.wall_image = pygame.image.load(WALL_IMAGE_PATH).convert()
        self.wall_image = pygame.transform.scale(self.wall_image, (TILE_SIZE, TILE_SIZE))
        
        # Pozice monster
        self.monster_positions = {"Skeletons": [], "Dragons": []}
        self.find_monster_positions()

        # Vytvoření sprite grupy pro zdi (kolize)
        self.walls = pygame.sprite.Group()
        self.create_walls()


    def load_level(self):
        level_data = []
        with open(LEVEL_PATH.format(self.current_level), 'r', encoding='utf-8-sig') as file:
            for line in file:
                row = list(map(int, line.strip().split(';')))
                level_data.append(row)
        self.level_data = level_data
    
    def create_walls(self):
        """Vytvoří sprite grupu zdí pro detekci kolizí"""
        self.walls.empty()
        for radek in range(len(self.level_data)):
            for sloupec in range(len(self.level_data[0])):
                if self.level_data[radek][sloupec] == 1:  # 1 = zeď
                    wall = Wall(sloupec * TILE_SIZE, radek * TILE_SIZE)
                    self.walls.add(wall)

    def find_monster_positions(self):
        """Najde pozice monster v levelu (55 = Skeleton)"""
        for radek in range(len(self.level_data)):
            for sloupec in range(len(self.level_data[0])):
                if self.level_data[radek][sloupec] == 55:  # 55 = pozice pro skeleton
                    x = sloupec * TILE_SIZE + TILE_SIZE // 2
                    y = radek * TILE_SIZE + TILE_SIZE // 2
                    self.monster_positions["Skeletons"].append((x, y))


                    


if __name__ == "__main__":
    import pokus1