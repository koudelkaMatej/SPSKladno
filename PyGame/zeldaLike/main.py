from PIL import Image
import os
def get_image_dimensions(folder_path):
    max_width = 0
    max_height = 0
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        if width > max_width:
                            max_width = width
                        if height > max_height:
                            max_height = height
                except Exception as e:
                    print(f"Error reading image '{file_path}': {e}")
    
    return max_width, max_height

folder_path = "obrazky/character"  # Zadejte cestu k adresáři s obrázky
max_width, max_height = get_image_dimensions(folder_path)
print(f"Max width: {max_width}, Max height: {max_height}")


import pygame
from settings import *
import os
import glob
#############################################################################
# Initialize the game
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pokelike')
clock = pygame.time.Clock()
#############################################################################
# Title and Icon
icon = pygame.image.load(ICON_IMAGE_PATH)
pygame.display.set_icon(icon)
#############################################################################
#assets
class Location:
    def __init__(self, name, image_path):
        self.name = name
        self.image = pygame.image.load(image_path)
#######################
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.scale = player_scale
        self.image = pygame.image.load(PLAYER_IMAGES_PATH + "/sword/moveDown/1.png")
        self.image_width, self.image_height = self.image.get_size()
        self.scale = player_scale
        self.image = pygame.transform.scale(self.image, (int(self.image_width*self.scale), int(self.image_height*self.scale)))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(START_X + self.image_width, START_Y))
        self.speed = 1
        self.location = LOCATION_HOME
        self.animations = {}
        self.load_images()
        self.frame_index = 0
        self.last_frame_update = pygame.time.get_ticks()
        self.current_time = 0
        self.elapsed_time = 0
        self.choosenAnimation = 0
        self.equip = "Sword"
        self.currentAnimation = None
        self.idle = True
        self.FRAME_CHANGE_DELAY = FRAME_CHANGE_DELAY
        self.facing = 'moveDown'
        self.block = False

    def update(self):
        self.idle = True
        self.FRAME_CHANGE_DELAY = FRAME_CHANGE_DELAY
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_LSHIFT]:
            self.speed = 3
        else:
            self.speed = 1
        if self.block == False:
            if keys[pygame.K_LEFT]:
                if self.facing != 'moveLeft':
                    self.frame_index = 0
                self.rect.x -= self.speed
                self.idle = False
                self.facing = 'moveLeft'
            
            if keys[pygame.K_RIGHT]:
                if self.facing != 'moveRight':
                    self.frame_index = 0
                self.rect.x += self.speed
                self.idle = False
                self.facing = 'moveRight'     
            if keys[pygame.K_UP]:
                if self.facing != 'moveUp':
                    self.frame_index = 0
                self.rect.y -= self.speed
                self.idle = False
                self.facing = 'moveUp'
            
            if keys[pygame.K_DOWN]:
                if self.facing != 'moveDown':
                    self.frame_index = 0
                self.rect.y += self.speed
                self.idle = False
                self.facing = 'moveDown'
            
            if keys[pygame.K_SPACE]:
                self.block = True
                self.frame_index = 0
                if self.facing == 'moveLeft':
                    self.facing = 'attackLeft'
                elif self.facing == 'moveRight':
                    self.facing = 'attackRight'
                elif self.facing == 'moveUp':
                    self.facing = 'attackUp'
                elif self.facing == 'moveDown':
                    self.facing = 'attackDown'
                else:
                    self.block = False
                self.idle = False
        if self.idle == True:
            if self.facing != 'idle':
                self.frame_index = 0
            self.facing = 'idle'
            self.FRAME_CHANGE_DELAY = 200
        self.currentAnimation = self.animations[self.equip][self.facing]

        self.elapsed_time = pygame.time.get_ticks() - self.last_frame_update

        if self.elapsed_time >= self.FRAME_CHANGE_DELAY:
            self.last_frame_update = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.currentAnimation):
                self.frame_index = 0
                if self.block == True:
                    self.block = False
                    if self.facing.__contains__('attack'):
                        #self.facing = self.facing.replace('attack', 'move')
                        self.idle = True

        self.image = self.currentAnimation[self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
       screen.blit(self.image, ((self.rect.x - self.image.get_width() //2, self.rect.centery - self.image.get_height() //2)))


    def load_and_scale_images(self,path, scale):
        image_files = sorted(glob.glob(f"{path}/*.png"))
        images = [pygame.image.load(img).convert_alpha()    for img in image_files]
        return [pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale))) for img in images]

    def load_images(self):

        self.animations = {
            'Sword': {
                'attackDown': self.load_and_scale_images(SWORD_ATTACK_DOWN_PATH, self.scale),
                'attackUp': self.load_and_scale_images(SWORD_ATTACK_UP_PATH, self.scale),
                'attackRight': self.load_and_scale_images(SWORD_ATTACK_RIGHT_PATH, self.scale),
                'attackLeft': [pygame.transform.flip(img, True, False) for img in self.load_and_scale_images(SWORD_ATTACK_RIGHT_PATH, self.scale)],
                'moveDown': self.load_and_scale_images(SWORD_MOVE_DOWN_PATH, self.scale),
                'moveUp': self.load_and_scale_images(SWORD_MOVE_UP_PATH, self.scale),
                'moveRight': self.load_and_scale_images(SWORD_MOVE_RIGHT_PATH, self.scale),
                'moveLeft': [pygame.transform.flip(img, True, False) for img in self.load_and_scale_images(SWORD_MOVE_RIGHT_PATH, self.scale)],
                'idle': [pygame.transform.flip(img, True, False) for img in self.load_and_scale_images(SWORD_IDLE_PATH, self.scale)],
                'death': [pygame.transform.flip(img, True, False) for img in self.load_and_scale_images(SWORD_DEATH_PATH, self.scale)],
            }
        }


#############################################################################
# setting up the game
player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
player_group = pygame.sprite.Group()
player_group.add(player)
#run
running = True
while running:
    screen.fill((255, 255, 255))
    player_group.update()
    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.display.update()
    clock.tick(FPS)