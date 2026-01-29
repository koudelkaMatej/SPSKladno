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
        self.hitbox = self.rect.copy()  # stable collision box
        self.last_update = pygame.time.get_ticks()
        self.status = "alive"
        self.speed = 3
        self.hp = 100
        self.is_alive = True
        self.death_animation_played = False
        self.facing = 'down'
        self.attack_cooldown = 1000  # milliseconds
        self.last_attack_time = 0
        self.attack_animation_played = False

    def update(self, walls=None) -> None:
        keys = pygame.key.get_pressed()
        self.speed = 3
        now = pygame.time.get_ticks()

        if self._is_in_attack_cooldown(now):
            self._frame_update()
            return

        self._handle_idle_hp_drain(keys)
        self._handle_movement(keys, walls)
        self._handle_attack(keys)
        self._handle_death()
        self._handle_idle_animation(keys)
        self._clamp_frame_index()
        self._frame_update()
        self._check_death_animation_finished()

    
    def _frame_update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > FRAME_CHANGE_DELAY: 
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
        self.image = self.animations[self.current_animation][self.current_frame]
        # Sync drawing rect to stable hitbox center
        self.rect = self.image.get_rect(center=self.hitbox.center)


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
        self.animations["attackLeft"] = self.animations["attackRight"].copy()
        for i in range(len(self.animations["attackLeft"])):
            self.animations["attackLeft"][i] = pygame.transform.flip(self.animations["attackLeft"][i], True, False)



    def _is_in_attack_cooldown(self, now: int) -> bool:
        return now - self.last_attack_time < self.attack_cooldown

    def _handle_idle_hp_drain(self, keys):
        if keys[pygame.K_LCTRL]:
            self.hp -= 1

    def _handle_movement(self, keys, walls):
        if keys[pygame.K_LSHIFT]:
            self.speed = 5

        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
            self.current_animation = "moveLeft"
            self.facing = "left"
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed
            self.current_animation = "moveRight"
            self.facing = "right"
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
            self.current_animation = "moveUp"
            self.facing = "up"
        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
            self.facing = "down"
            self.current_animation = "moveDown"

        # Sync rect to hitbox for collision check
        self.rect.center = self.hitbox.center

        if self._check_wall_collision(walls):
            if keys[pygame.K_LEFT]:
                self.hitbox.x += self.speed 
            if keys[pygame.K_RIGHT]:
                self.hitbox.x -= self.speed 
            if keys[pygame.K_UP]:
                self.hitbox.y += self.speed 
            if keys[pygame.K_DOWN]:
                self.hitbox.y -= self.speed 

            # Sync rect again after collision resolution
            self.rect.center = self.hitbox.center 

    def _handle_attack(self, keys):
        if not keys[pygame.K_SPACE]:
            return

        self.attack_animation_played = True
        self.last_attack_time = pygame.time.get_ticks()
        self.current_frame = 0

        if self.facing == "down":
            self.current_animation = "attackDown"
        elif self.facing == "up":
            self.current_animation = "attackUp"
        elif self.facing == "left":
            self.current_animation = "attackLeft"
        elif self.facing == "right":
            self.current_animation = "attackRight"

    def _handle_death(self):
        if self.hp <= 0 and not self.death_animation_played:
            self.current_animation = "death"
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.death_animation_played = True

    def _handle_idle_animation(self, keys):
        if not any(keys) and not self.death_animation_played:
            self.current_animation = "idle"

    def _clamp_frame_index(self):
        if self.current_frame >= len(self.animations[self.current_animation]):
            self.current_frame = 0

    def _check_death_animation_finished(self):
        if (
            self.current_animation == "death"
            and self.current_frame == len(self.animations["death"]) - 1
        ):
            self.is_alive = False

    def _check_wall_collision(self, walls):
        """Kontroluje kolizi se zdmi a vraci True, pokud dojde ke kolizi."""
        hits = pygame.sprite.spritecollide(self, walls, False, pygame.sprite.collide_mask)
        return bool(hits)

if __name__ == "__main__":
    import pokus1