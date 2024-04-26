# import pygame package 
import pygame 
from Player import *
from Enemy import *
pygame.init() 
def getHighScore(): # čtení souboru
    try:
        with open("spaceinvadersObjektove/highestScore.txt", 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File 'spaceinvadersObjektove/highestScore.txt' not found.")
        return None
def generateEnemies(): # funkce pro vykreslení všech nepřátel na mapě
	generetedEnemies = pygame.sprite.Group()
	y = 100
	for i in range(5):
		x = 40
		for j in range(3):
			generetedEnemies.add(Enemy(x,y,enemyImagePath,enemySize))
			x += 50
		y += 50
	y = 100
	for i in range(5):
		x = 340
		for j in range(3):
			generetedEnemies.add(Enemy(x,y,enemyImagePath,enemySize))
			x += 50
		y += 50
	return generetedEnemies
# definování základních proměnných
clock = pygame.time.Clock()  # pro FPS
screen = pygame.display.set_mode((550, 500))
width, height = screen.get_size()
spaceshipImagePath = "spaceinvadersObjektove/obr/spaceship.png"
spaceshipSize = (60,60)
enemyImagePath = "spaceinvadersObjektove/obr/ufo.png"
enemySize = (40,40)
missleImagePath = "spaceinvadersObjektove/obr/shot.png"
missleSize = (10,30)
player = Player(275,460,spaceshipImagePath,spaceshipSize,width,height)
enemy = Enemy(45,45,enemyImagePath,enemySize)
enemies = generateEnemies()
score = 0 # pro pocitani skore hrace
highScore = getHighScore()
font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render(f'Score: {score}', True, (255,0,0),(0,0,0))
textRect = text.get_rect()
textRect = (15,15)
text2 = font.render(f'HighScore: {highScore}', True, (255,0,0),(0,0,0))
textRect2 = text2.get_rect()
textRect2 = (250,15)

SHOOTING = pygame.USEREVENT + 1   # vlastní event
pygame.time.set_timer(SHOOTING, 2000) # automaticky pohyb nepratel kazdou vterinu
MOOVING = pygame.USEREVENT + 2   # vlastní event
pygame.time.set_timer(MOOVING, 50) # automaticky pohyb nepratel kazdou vterinu
running = True
while running: 
	clock.tick(15)  # FPS
	screen.fill((150, 150, 0))
	pygame.draw.rect(screen,(0,0,0,128),[0,0,550,70])
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False
			pygame.quit()
		if event.type == MOOVING:
			enemies.update()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		player.move("left")
		print("Left key pressed")
	if keys[pygame.K_d]:
		player.move("right")
		print("Right key pressed")
	
	for enemy in enemies:
		if enemy.rect.y >= 550:
			print("Game Over")
	if pygame.sprite.spritecollide(player, enemies, True,pygame.sprite.collide_mask):
		print("kolize")
		player.explosion(screen)
	player.draw(screen)
	enemies.draw(screen)
	text = font.render(f'Score: {score}', True, (255,0,0),(0,0,0))
	screen.blit(text, textRect)
	screen.blit(text2, textRect2)
	pygame.display.update()

