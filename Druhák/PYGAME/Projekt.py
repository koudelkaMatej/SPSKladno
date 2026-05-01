import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation Example")

# Load sprite images
sprite_images = [pygame.image.load(f"PyGame/spaceinvadersObjektove/obr/0exploze.png"), pygame.image.load(f"PyGame/spaceinvadersObjektove/obr/1exploze.png"), pygame.image.load(f"PyGame/spaceinvadersObjektove/obr/2exploze.png"), pygame.image.load(f"PyGame/spaceinvadersObjektove/obr/3exploze.png"), pygame.image.load(f"PyGame/spaceinvadersObjektove/obr/4exploze.png"), pygame.image.load(f"PyGame/spaceinvadersObjektove/obr/5exploze.png")]
sprite_index = 0
sprite_rect = sprite_images[0].get_rect(center=(screen_width // 2, screen_height // 2))

# Set up timing variables
animation_duration = 100  # Time between each frame in milliseconds
last_update = pygame.time.get_ticks()

frame_counter = 0  # Counts the number of frames that have passed
frames_per_image = 10  # Change this to control the speed of the animation

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animation logic
    frame_counter += 1
    if frame_counter >= frames_per_image:
        frame_counter = 0
        sprite_index += 1
        if sprite_index == len(sprite_images):
            sprite_index = 0

    # Drawing
    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(sprite_images[sprite_index], sprite_rect)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
