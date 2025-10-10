SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60
TILE_SIZE = 50 # CSV je napocitane na 50px což je vlastně 1000/50 = 20 sloupců a řádků
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 70
PLAYER_SPEED = 5
PLAYER_JUMPING_POWER = 8


SUN_IMAGE_PATH = 'Assets/Images/sun.png'
SKY_IMAGE_PATH = 'Assets/Images/sky.png'
DIRT_IMAGE_PATH = 'Assets/Images/dirt.png'
GRASS_IMAGE_PATH = 'Assets/Images/grass.png'
COIN_IMAGE_PATH = 'Assets/Images/coin.png'
EXIT_IMAGE_PATH = 'Assets/Images/exit.png'
LAVA_IMAGE_PATH = 'Assets/Images/lava.png'
BLOB_IMAGE_PATH = 'Assets/Images/blob.png'
PLAYER_IMAGE_MOVE_PATH = "Assets/ohen a voda/boy_right"
PLAYER_IMAGE_IDLE_PATH = "Assets/ohen a voda/boy_still"
PLAYER_IMAGE_PATH = "Assets/Images/guy{}.png"

if __name__ == "__main__":
    import main
    main.main()