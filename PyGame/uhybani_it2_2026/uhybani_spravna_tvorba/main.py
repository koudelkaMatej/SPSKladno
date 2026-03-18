import pygame
import settings
from Player import *
from Block import Block
from settings import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()
with open("highscore.txt", "r") as f:
    highscore = int(f.read())
score = 0
score_font = pygame.font.SysFont("Arial", 30)
score_text = score_font.render(f"Score: {score}", True, BLACK)
score_rect = score_text.get_rect(topleft=(10, 10))
highscore_text = score_font.render(f"Highscore: {highscore}", True, BLACK)
highscore_rect = highscore_text.get_rect(topleft=(10, 40))
hrac = Player()
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
blok = Block()
blok_group = pygame.sprite.Group()
blok_group.add(blok)

BLOCK_SPAWN = pygame.USEREVENT + 1
spawning_timer = 2000
pygame.time.set_timer(BLOCK_SPAWN, spawning_timer)

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == BLOCK_SPAWN:
            blok_group.add(Block())
            score += 1
            score_text = score_font.render(f"Score: {score}", True, BLACK)
            if score % 2 == 0 and score != 0:
                spawning_timer = max(500, spawning_timer - 100)
                pygame.time.set_timer(BLOCK_SPAWN, spawning_timer)
            
            if score % 5 == 0 and score != 0:
                 settings.BLOCK_SPEED += 2
        if score >= highscore:
            highscore = score
            highscore_text = score_font.render(f"Highscore: {highscore}", True, BLACK)
    
    hrac_group.update()
    hrac_group.draw(screen)
    blok_group.update()
    blok_group.draw(screen)

    if pygame.sprite.spritecollide(hrac, blok_group, True, pygame.sprite.collide_mask):
        print("KOLIZE!")
        if score >= highscore:
            with open("highscore.txt", "w") as f:
                f.write(str(score))
        pygame.time.delay(1000)
        running = False
    screen.blit(score_text, score_rect)
    screen.blit(highscore_text, highscore_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()