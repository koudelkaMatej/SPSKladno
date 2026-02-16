import pygame
from settings import *

class Level:   
    def __init__(self):
        self.current_level = 1
        self.level_data = []
        self.__load_level()

    def __load_level(self):
        level_data = []
        with open(LEVEL_PATH.format(self.current_level), 'r', encoding='utf-8-sig') as file:
            for line in file:
                row = list(map(int, line.strip().split(';')))
                level_data.append(row)
        self.level_data = level_data


if __name__ == "__main__":
    import main