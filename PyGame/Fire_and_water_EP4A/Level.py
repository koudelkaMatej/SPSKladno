import pygame
from settings import *

class Level:   
    def __init__(self):
        self.current_level = 1
        self.level_data = self.load_level()

    def load_level(self):
        level_data = []
        with open(LEVEL_PATH.format(self.current_level), 'r', encoding='utf-8-sig') as file:
            for line in file:
                row = list(map(int, line.strip().split(';')))
                print(row)
        print(level_data)
        return level_data


