import pygame, os
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = {}
        self.load_animation_frames(os.path.join(SWORD_PATH_BASE))
        self.current_animation = "idle_down"
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

        # Skip all actions when death animation is playing
        if not self.death_animation_played:
            self._handle_idle_hp_drain(keys)
            self._handle_movement(keys, walls)
            self._handle_attack(keys)
            self._handle_idle_animation(keys)
        
        self._handle_death()
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
        animation_types = [
            "idle_down", "idle_up", "idle_left",  "idle_right", 
            "walk_up", "walk_down", "walk_left", "walk_right", "run_up", "run_down", "run_left", "run_right",
            "slash_up", "slash_down", "slash_left", "slash_right", "thrust_up", "thrust_down", "thrust_left", "thrust_right",
            "sit_down", "sit_up", "sit_left", "sit_right",
            "death"
        ]
        for animation in animation_types:
            path = os.path.join(base_folder, *animation.split("_"))
            if not os.path.isdir(path):
                print(f"Warning: Animation path '{path}' not found for '{animation}'.")
                self.animations[animation] = []
                continue
            frames = []
            for file_name in sorted(os.listdir(path)):
                if file_name.endswith('.png'):
                    image_path = os.path.join(path, file_name)
                    image = pygame.image.load(image_path).convert_alpha()
                    scaled_image = pygame.transform.scale(
                        image,
                        (int(image.get_width() * PLAYER_SCALE), int(image.get_height() * PLAYER_SCALE))
                    )
                    frames.append(scaled_image)
            self.animations[animation] = frames



    def _is_in_attack_cooldown(self, now: int) -> bool:
        return now - self.last_attack_time < self.attack_cooldown

    def _handle_idle_hp_drain(self, keys):
        if keys[pygame.K_LCTRL]:
            self.hp -= 1

    def _handle_movement(self, keys, walls):
        if keys[pygame.K_LSHIFT]:
            self.speed = 5
        if keys[pygame.K_LEFT] :
            self.hitbox.x -= self.speed
            self.facing = "left"
        if keys[pygame.K_RIGHT] :
            self.hitbox.x += self.speed

            self.facing = "right"
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
            self.facing = "up"
        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
            self.facing = "down"
        
        self._update_movement_animation()

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

    def _update_movement_animation(self):
        """Update animation based on current speed and facing direction."""
        animation_prefix = "run" if self.speed == 5 else "walk"
        self.current_animation = f"{animation_prefix}_{self.facing}" 

    def _handle_attack(self, keys):
        if not keys[pygame.K_SPACE]:
            return

        self.attack_animation_played = True
        self.last_attack_time = pygame.time.get_ticks()
        self.current_frame = 0

        if self.facing == "down":
            self.current_animation = "slash_down"
        elif self.facing == "up":
            self.current_animation = "slash_up"
        elif self.facing == "left":
            self.current_animation = "slash_left"
        elif self.facing == "right":
            self.current_animation = "slash_right"

    def _handle_death(self):
        if self.hp <= 0 and not self.death_animation_played:
            self.current_animation = "death"
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.death_animation_played = True

    def _handle_idle_animation(self, keys):
        if not any(keys) and not self.death_animation_played:
            self.current_animation = f"idle_{self.facing}"

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