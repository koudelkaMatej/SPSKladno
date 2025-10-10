import pygame
from Block import *
from Player import *
import random
pygame.init()
pygame.font.init()
clock = pygame.time.Clock() # pro FPS
screen = pygame.display.set_mode((400, 700))
# font
font = pygame.font.Font(None, 36)
# text
score = 0
with open("highscore.txt", "r") as file:
    high_score = int(file.read())
text = font.render(f"Score: {score}", True, (255, 0, 0))
textRect = text.get_rect()
textRect.center = (50, 650)

high_text = font.render(f"HighScore: {high_score}", True, (255, 0, 0))
high_textRect = high_text.get_rect()
high_textRect.center = (300, 650)

# Vytvoření hráče
player = Player(200, 560, "obrazky/spaceship.png", 80)

# Vytvoření bloků
all_block_list = pygame.sprite.Group()
randomX = random.randint(25, 375)
block = Block(randomX, 25, "obrazky/ground.png", 50)
all_block_list.add(block)

# user event
ADD_BLOCK = pygame.USEREVENT + 1
event_ADD_BLOCK_timer = 1000
pygame.time.set_timer(ADD_BLOCK, event_ADD_BLOCK_timer) # 1000 ms = 1s

running = True
while running: # vše co je zde měním dynamicky dle ticku
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ADD_BLOCK:
            randomX = random.randint(25, 375)
            block = Block(randomX, 25, "obrazky/ground.png", 50)
            all_block_list.add(block)
            score +=10
            if score % 20 == 0:
                #event_ADD_BLOCK_timer -= 50
                #pygame.time.set_timer(ADD_BLOCK,max(200,event_ADD_BLOCK_timer))
                all_block_list.velocity += 5
            if score > high_score:
                high_score = score
    # Update vsech prvků
    if pygame.sprite.spritecollide(player, all_block_list, False, pygame.sprite.collide_mask):
        with open("highscore.txt", "w") as file:
                    file.write(str(high_score))
        pygame.time.delay(2000)
        running = False
    all_block_list.update()
    player.update()
    # vykresleni vsech prvku
    player.draw(screen)
    all_block_list.draw(screen)
    # score
    text = font.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(text, textRect)
    high_text = font.render(f"HighScore: {high_score}", True, (255, 0, 0))
    screen.blit(high_text, high_textRect)
    pygame.display.flip()
    clock.tick(60) # FPS
pygame.quit()
