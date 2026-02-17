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
        self.hitbox = pygame.Rect(0, 0, TILE_SIZE+10 , TILE_SIZE)  # wider collision box
        self.hitbox.midbottom = self.rect.midbottom
        self.hitbox_offset_y = 15  # sprite drawn above hitbox
        self.wall_collision_extend_down = 15  # extra px added to hitbox bottom for down wall check
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
        self.invincibility_duration = 1000  # milliseconds
        self.last_hit_time = 0
        self.slash_damage = 20
        self.thrust_damage = 40
        self.stamina = 100
        self.max_stamina = 100
        self.thrust_stamina_cost = 30
        self.stamina_regen_rate = 1  # points per tick
        self.stamina_regen_interval = 2000  # ms (1 point every 2 sec)
        self.last_stamina_regen = pygame.time.get_ticks()

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
            self._handle_attack_animation(keys)
            self._handle_idle_animation(keys)
        
        self._handle_death()
        self._handle_stamina_regen()
        self._clamp_frame_index()
        self._frame_update()
        self._check_death_animation_finished()

    
    def _frame_update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > FRAME_CHANGE_DELAY: 
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
        self.image = self.animations[self.current_animation][self.current_frame]
        # Sync drawing rect to hitbox with vertical offset (sprite drawn above hitbox)
        self.rect = self.image.get_rect(center=(self.hitbox.centerx, self.hitbox.centery - self.hitbox_offset_y))


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



    def wound_effect(self):
        if not self.is_wounded :
            self.is_wounded = True
            self.hp -= 10
            self.wound_effect_start_time = pygame.time.get_ticks()

    def _is_in_attack_cooldown(self, now: int) -> bool:
        return now - self.last_attack_time < self.attack_cooldown

    def _handle_idle_hp_drain(self, keys):
        if keys[pygame.K_LCTRL]:
            self.hp -= 1

    def _handle_movement(self, keys, walls):
        if keys[pygame.K_LSHIFT]:
            self.speed = 5

        # --- Move X axis first, check collision, resolve ---
        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
            self.facing = "left"
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed
            self.facing = "right"

        self.rect.center = (self.hitbox.centerx, self.hitbox.centery - self.hitbox_offset_y)
        if self._check_wall_collision(walls):
            if keys[pygame.K_LEFT]:
                self.hitbox.x += self.speed
            if keys[pygame.K_RIGHT]:
                self.hitbox.x -= self.speed

        # --- Move Y axis, check collision, resolve ---
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
            self.facing = "up"
        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
            self.facing = "down"

        self.rect.center = (self.hitbox.centerx, self.hitbox.centery - self.hitbox_offset_y)
        if self._check_wall_collision(walls, extend_down=(keys[pygame.K_DOWN])):
            if keys[pygame.K_UP]:
                self.hitbox.y += self.speed
            if keys[pygame.K_DOWN]:
                self.hitbox.y -= self.speed

        self._update_movement_animation()
        self.rect.center = (self.hitbox.centerx, self.hitbox.centery - self.hitbox_offset_y)

    def _update_movement_animation(self):
        """Update animation based on current speed and facing direction."""
        animation_prefix = "run" if self.speed == 5 else "walk"
        self.current_animation = f"{animation_prefix}_{self.facing}" 

    def _handle_attack_animation(self, keys):
        if keys[pygame.K_SPACE]:
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
        elif keys[pygame.K_t]:
            if self.stamina < self.thrust_stamina_cost:
                return  # not enough stamina, do nothing
            self.stamina -= self.thrust_stamina_cost
            self.attack_animation_played = True
            self.last_attack_time = pygame.time.get_ticks()
            self.current_frame = 0
            if self.facing == "down":
                self.current_animation = "thrust_down"
            elif self.facing == "up":
                self.current_animation = "thrust_up"
            elif self.facing == "left":
                self.current_animation = "thrust_left"
            elif self.facing == "right":
                self.current_animation = "thrust_right"

    def _handle_death(self):
        if self.hp <= 0 and not self.death_animation_played:
            self.current_animation = "death"
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.death_animation_played = True

    def _handle_stamina_regen(self):
        now = pygame.time.get_ticks()
        if self.stamina < self.max_stamina and now - self.last_stamina_regen >= self.stamina_regen_interval:
            self.stamina = min(self.stamina + self.stamina_regen_rate, self.max_stamina)
            self.last_stamina_regen = now

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

    def get_damage(self):
        if not self.attack_animation_played:
            return 0
        if "slash" in self.current_animation:
            return self.slash_damage
        if "thrust" in self.current_animation:
            return self.thrust_damage
        return 0

    def get_slash_hitbox(self):
        """Wide arc in front of the player for slash attack."""
        attack_range = 70
        attack_width = 50
        if self.facing == "up":
            return pygame.Rect(self.hitbox.centerx - attack_width // 2, self.hitbox.top - attack_range, attack_width, attack_range)
        elif self.facing == "down":
            return pygame.Rect(self.hitbox.centerx - attack_width // 2, self.hitbox.bottom, attack_width, attack_range)
        elif self.facing == "left":
            return pygame.Rect(self.hitbox.left - attack_range, self.hitbox.centery - attack_width // 2, attack_range, attack_width)
        elif self.facing == "right":
            return pygame.Rect(self.hitbox.right, self.hitbox.centery - attack_width // 2, attack_range, attack_width)
        return self.hitbox

    def get_thrust_hitbox(self):
        """Narrow and long rect in front of the player for thrust attack."""
        attack_range = 100
        attack_width = 20
        if self.facing == "up":
            return pygame.Rect(self.hitbox.centerx - attack_width // 2, self.hitbox.top - attack_range, attack_width, attack_range)
        elif self.facing == "down":
            return pygame.Rect(self.hitbox.centerx - attack_width // 2, self.hitbox.bottom, attack_width, attack_range)
        elif self.facing == "left":
            return pygame.Rect(self.hitbox.left - attack_range, self.hitbox.centery - attack_width // 2, attack_range, attack_width)
        elif self.facing == "right":
            return pygame.Rect(self.hitbox.right, self.hitbox.centery - attack_width // 2, attack_range, attack_width)
        return self.hitbox

    def get_attack_hitbox(self):
        """Returns the appropriate attack hitbox based on current animation."""
        if "thrust" in self.current_animation:
            return self.get_thrust_hitbox()
        return self.get_slash_hitbox()

    def set_damage(self, damage):
        now = pygame.time.get_ticks()
        if now - self.last_hit_time >= self.invincibility_duration:
            self.hp -= damage
            self.last_hit_time = now
    def _check_wall_collision(self, walls, extend_down=False):
        """Kontroluje kolizi se zdmi. Pokud extend_down, zvětší hitbox dolů."""
        check_rect = self.hitbox
        if extend_down:
            check_rect = self.hitbox.inflate(0, self.wall_collision_extend_down)
            check_rect.top = self.hitbox.top  # extend only downward
        for wall in walls:
            if check_rect.colliderect(wall.rect):
                return True
        return False

if __name__ == "__main__":
    import pokus1