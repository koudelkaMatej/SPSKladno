import pygame, os
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = {}
        self.load_animation_frames(SWORD_PATH_BASE)
        self.current_animation = "idle"
        self.current_frame = 0
        self.image = self.animations[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.last_update = pygame.time.get_ticks()
        self.status = "alive"
        self.speed = 3
        self.hp = 100
        self.alive = True
        self.death_animation_played = False
        self.facing = 'down'
    def update(self):
        keys = pygame.key.get_pressed()

        # Idle check
        if keys[pygame.K_LCTRL]:
            self.hp = 0

        # movement of Character
        if keys[pygame.K_LSHIFT]:
            self.speed = 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.current_animation = "moveLeft"
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.current_animation = "moveRight"
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.current_animation = "moveUp"
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed    
            self.facing = 'down'
            self.current_animation = "moveDown"

        # Attack check
        if keys[pygame.K_SPACE]:
            if self.facing == "down":
                self.current_animation = "attackDown"
            elif self.facing == "up":
                self.current_animation = "attackUp"


        #Death check
        if self.hp <=0 and not self.death_animation_played:
            self.current_animation = "death"
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.death_animation_played = True

        # Animation update
        if not any(keys) and not self.death_animation_played:
            self.current_animation = "idle"
        if self.current_frame >= len(self.animations[self.current_animation]):
            self.current_frame = 0
        now = pygame.time.get_ticks()
        if now - self.last_update > FRAME_CHANGE_DELAY: 
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
        self.image = self.animations[self.current_animation][self.current_frame]
        
        # Check if death animation finished
        if self.current_animation == "death" and self.current_frame == len(self.animations["death"]) - 1:
            self.alive = False





    def is_alive(self):
        return self.alive










    def load_animation_frames(self, base_folder):
        self.animations.clear()
        if not base_folder or not os.path.isdir(base_folder):
            return
        for entry in os.scandir(base_folder):
            if not entry.is_dir():
                continue
            state_name = entry.name  # e.g. "idle"
            state_path = entry.path
            frame_files = [
                f.path for f in os.scandir(state_path)
                if f.is_file() and f.name.lower().endswith(".png")
            ]
            frame_files.sort(key=lambda p: os.path.basename(p).lower())
            if not frame_files:
                continue

            frames = []
            for p in frame_files:
                img = pygame.image.load(p).convert_alpha()
                if PLAYER_SCALE != 1:
                    img = pygame.transform.scale(
                        img,
                        (int(img.get_width() * PLAYER_SCALE), int(img.get_height() * PLAYER_SCALE))
                    )
                frames.append(img)

            self.animations[state_name] = frames

        self.animations["moveLeft"] = self.animations["moveRight"].copy()
        for i in range(len(self.animations["moveLeft"])):
            self.animations["moveLeft"][i] = pygame.transform.flip(self.animations["moveLeft"][i], True, False)


if __name__ == "__main__":
    import pokus1