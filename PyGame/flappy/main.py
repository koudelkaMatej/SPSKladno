import pygame
from settings import *
from Slider import *
from Flappy import *
from Pipe import *
pygame.init()
pygame.font.init()  # inicializace fontu
pygame.mixer.init()  # inicializace zvuku

score = 0 
font = pygame.font.Font(None, 30)  # inicializace fontu
user_text = ""  # text pro jméno hráče
with open("highscore.txt", "r") as file:  # načtení skóre ze souboru
    highscore_name = file.readline() 
    highscore_score = int(file.readline())
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT-150))  # změna velikosti pozadí
ground_image = pygame.image.load(GROUND_IMAGE_PATH).convert()
ground_image = pygame.transform.scale(ground_image, (SCREEN_WIDTH+35, 150))  # změna velikosti pozadí
font = pygame.font.Font(None, 30)  # inicializace fontu

clock = pygame.time.Clock()  # pro FPS
clock.tick(FPS)  # FPS
running = True

ground_scroll = 0  # posun pozadí
ground_scroll_change = 4  # změna posunu pozadí

def draw_background():
    global ground_scroll
    # background image on screen
    screen.blit(background_image, (0, 0))
    screen.blit(ground_image, (ground_scroll, SCREEN_HEIGHT - 150))  # vykreslení pozadí
    ground_scroll -= ground_scroll_change  # posun pozadí
    if abs(ground_scroll) > 27:  # pokud je pozadí posunuto o více než šířku obrazovky
        ground_scroll = 0  # resetuji posun pozadí

def draw_score_text(score,highscore_name=None, highscore_score=None):
    score_text = font.render(f"Score: {score} Points", True, BLACK)  # vykreslení skóre
    score_text_rect = score_text.get_rect(center=(100, SCREEN_HEIGHT - 100))  # umístění textu na střed obrazovky
    score_text_rect.left = 100  # umístění textu na levý okraj obrazovky
    screen.blit(score_text, score_text_rect)  # vykreslení textu na obrazovku
    if highscore_name and highscore_score:  # pokud je highscore
        highscore_text = font.render(f"Record: {highscore_name}: {highscore_score} Points", True, BLACK)  # vykreslení highscore
        highscore_text_rect = highscore_text.get_rect()  # umístění textu na střed obrazovky
        highscore_text_rect.left = 100
        highscore_text_rect.top = SCREEN_HEIGHT - 50
        screen.blit(highscore_text, highscore_text_rect)

pipe_group = pygame.sprite.Group()  # skupina pro trubky
GENERATE_PIPES = pygame.USEREVENT + 1  # událost pro generování trubek
pygame.time.set_timer(GENERATE_PIPES, 1500)  # generování trubek každých 1,5 sekundy

def save_highscore_menu():
    base_font = pygame.font.Font(None, 40)
    save_highscore_menu_running = True

    # stores text taken by keyboard
    user_text = ''

    # set left, top, width, height in 
    # Pygame.Rect()
    input_rect = pygame.Rect(200, 200, 140, 32)
    color_active = pygame.Color("lightskyblue")
    color_passive = pygame.Color("gray15")
    color = color_passive

    active = False

    while save_highscore_menu_running == True:
        draw_background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_highscore_menu_running = False

            # when mouse collides with the rectangle
            # make active as true
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True

            # if the key is physically pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # stores text except last letter
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode
                if event.key == pygame.K_RETURN:
                    if user_text:
                        global highscore_name
                        highscore_name = user_text
                        save_highscore_menu_running = False
        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen, color, input_rect)
        
        # render the text
        who_played_text = base_font.render("Who played?", True, (255, 255, 255))
        screen.blit(who_played_text, (input_rect.x, input_rect.y - 30))  # vykreslení textu nad vstupním polem
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)

def game_menu():
    global score, user_text
    global highscore_name, highscore_score
    game_menu_running = True
    player = Flappy()
    player_group = pygame.sprite.Group()
    player_group.add(player)
    pygame.time.delay(1000)  # zpoždění pro načtení hry
    while game_menu_running:
        draw_background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_menu_running = False
            if event.type == GENERATE_PIPES:
                pipe_group.add(Pipe("up"))
                pipe_group.add(Pipe("down"))
        # Zde by měl být kód pro hru
        player_group.update()
        player_group.draw(screen)
        pipe_group.update()
        pipe_group.draw(screen)
        if pygame.sprite.spritecollide(player, pipe_group, False):
            game_menu_running = False
            save_highscore_menu()
            if score > highscore_score:  # pokud je skóre vyšší než highscore
                highscore_score = score  # aktualizace highscore
                with open("highscore.txt", "w") as file:  # zápis highscore do souboru
                    file.write(f"{highscore_name}{highscore_score}")
        for pipe in pipe_group:
            if pipe.rect.right < player.rect.left and not pipe.pipe_passed:
                score += 5  # zvýšení skóre, pokud hráč projde trubkou
                pipe.pipe_passed = True  # nastavení flagu, že trubka byla projita
        draw_score_text(score,highscore_name,highscore_score)  # vykreslení skóre
        pygame.display.flip()
        clock.tick(FPS)  # FPS



# hlavní menu
def main_menu():
    volume_slider = Slider(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 20, 0.0, 1.0, MUSIC_VOLUME)
    pygame.mixer.music.load(MENU_MUSIC)
    pygame.mixer.music.play(-1)  # -1 znamená, že se bude hrát do nekonečna
    pygame.mixer.music.set_volume(MUSIC_VOLUME)  # nastavení hlasitosti
    main_menu_running = True
    settings_menu_running = False
    while main_menu_running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exitTextRect.collidepoint(event.pos):
                main_menu_running = False
            if settingsTextRect.collidepoint(event.pos):
                settings_menu_running = True
            if startGameTextRect.collidepoint(event.pos):
                game_menu()
                main_menu_running = False

        if settings_menu_running == False: 
            startGameText = font.render("Start Game", True, BLACK)
            startGameTextRect = startGameText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-50))
            pygame.draw.rect(screen, BRIGHT_ORANGE, startGameTextRect.inflate(20, 10))  # Add background color
            screen.blit(startGameText, startGameTextRect)
            settingsText = font.render("Settings", True, BLACK)
            settingsTextRect = settingsText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 ))
            pygame.draw.rect(screen, BRIGHT_ORANGE, settingsTextRect.inflate(20, 10))  # Add background color

            screen.blit(settingsText, settingsTextRect)
            exitText = font.render("Exit", True, BLACK)
            exitTextRect = exitText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            pygame.draw.rect(screen, BRIGHT_ORANGE, exitTextRect.inflate(20, 10))
            screen.blit(exitText, exitTextRect)
        else:
            backText = font.render("Back", True, BLACK)
            backTextRect = backText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
            pygame.draw.rect(screen, BRIGHT_ORANGE, backTextRect.inflate(20, 10))  # Add background color
            screen.blit(backText, backTextRect)
            volume_slider.draw(screen)
            volume_slider.handle_event(event)
            pygame.mixer.music.set_volume(volume_slider.get_value())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backTextRect.collidepoint(pygame.mouse.get_pos()):
                    settings_menu_running = False




        pygame.display.flip()


while running:  # vše co je zde měním dynamicky dle ticku
    main_menu()
    running = False
