SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000
FPS = 60

PLAYER_X_SIZE = 40
PLAYER_Y_SIZE = 75
TILE_SIZE = 50 # CSV je napocitane na 50px což je vlastně 1000/50 = 20 sloupců a řádků

LEVEL_PATH = 'Assets/Levels/level{}.csv'  # {} je číslo levelu
# number of tiles
# 0 = empty tile
# 1 = dirt tile


DIRT_PATH = 'Assets/ohen a voda/dirt/dirt.png'
# 2 = lava tile
LAVA_PATH = 'Assets/ohen a voda/lava/{}.png'.format(1)
# 12 = lava left tile
# 21 = lava right tile
LAVA_RIGHT_PATH = 'Assets/ohen a voda/lava_kraj/{}.png'
# 3 = water tile
WATER_PATH = 'Assets/ohen a voda/voda/{}.png'
# 13 = water left tile
# 31 = water right tile
WATER_RIGHT_PATH = 'Assets/ohen a voda/voda_kraj/{}.png'
# 4 = poison tile
POISON_PATH = 'Assets/ohen a voda/jed/{}.png'
# 14 = poison left tile
# 41 = poison right tile
POISON_RIGHT_PATH = 'Assets/ohen a voda/jed_kraj/{}.png'
# 5 = coin tile
COIN_PATH = 'Assets/ohen a voda/coin/coin.png'
# 6 = exit tile
EXIT_PATH = 'Assets/ohen a voda/vychod/exit.png'
# 7 = fire player
BOY_IDLE_PATH = 'Assets/ohen a voda/boy_still/{}.png'
BOY_RIGHT_PATH = 'Assets/ohen a voda/boy_right/{}.png'
# 8 = water player
GIRL_IDLE_PATH = 'Assets/ohen a voda/girl_still/{}.png'
GIRL_RIGHT_PATH = 'Assets/ohen a voda/girl_right/{}.png'
# 9 = switch tile


if __name__ == "__main__":
    import main