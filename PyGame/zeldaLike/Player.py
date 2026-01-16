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
        self.alive = True
    def update(self):
        if self.alive:
            keys = pygame.key.get_pressed()
            if self.current_animation != "death":
                if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]):
                    self.current_animation = "idle"
                if keys[pygame.K_SPACE]:
                    self.current_animation = "death"
                    self.current_frame = 0
                if keys[pygame.K_LEFT]:
                    self.rect.x -= 5
                    self.current_animation = "moveLeft"
                if keys[pygame.K_RIGHT]:
                    self.rect.x += 5
                    self.current_animation = "moveRight"
                if keys[pygame.K_UP]:
                    self.rect.y -= 5
                    self.current_animation = "moveUp"
                if keys[pygame.K_DOWN]:
                    self.rect.y += 5    
                    self.current_animation = "moveDown"
                if self.current_frame >= len(self.animations[self.current_animation]):
                    self.current_frame = 0
                self.image = self.animations[self.current_animation][self.current_frame]
                now = pygame.time.get_ticks()
                if now - self.last_update > FRAME_CHANGE_DELAY: 
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
            elif self.current_animation == "death":
                if self.current_frame == len(self.animations["death"]):
                    print("Player has died.")
                    self.alive = False
                    now = pygame.time.get_ticks()
                    self.last_update = now
                    self.current_frame = 0
        else:
            now = pygame.time.get_ticks()
            if now - self.last_update > FRAME_CHANGE_DELAY: 
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
                self.image = self.animations[self.current_animation][self.current_frame]
            else:
                self.image = self.animations["death"][-1]















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