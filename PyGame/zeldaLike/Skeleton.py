import pygame
from settings import *
from Player import Player
import os
import random as rand
class Skeleton(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        # Load skeleton-specific animations
        self.load_animation_frames(os.path.join(SKELETON_SWORD_PATH_BASE))
        self.current_animation = "idle_down"
        self.image = self.animations[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.hitbox = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)  # smaller collision box
        self.hitbox.midbottom = self.rect.midbottom
        self.speed = 1
        self.hp = 50
        self.movement_decided = False
        self.decision_time = 0
        self.target_player = None  # Reference to the player to attack
        self.is_dead_for_500ms = False
        self.death_time = 0
        self.death_animation_played = False  # Ensure death animation plays only once


    def _handle_movement(self, keys, walls):
        detection_range = 80

        # Check if player is within detection range
        if self.target_player is not None:
            skeleton_pos = pygame.math.Vector2(self.hitbox.center)
            player_pos = pygame.math.Vector2(self.target_player.hitbox.center)
            distance = skeleton_pos.distance_to(player_pos)
        else:
            distance = float('inf')

        if distance <= detection_range:
            # Chase the player
            dx = player_pos.x - skeleton_pos.x
            dy = player_pos.y - skeleton_pos.y
            self.direction = pygame.math.Vector2(0, 0)
            if abs(dx) > abs(dy):
                self.direction.x = 1 if dx > 0 else -1
                self.facing = 'right' if dx > 0 else 'left'
            else:
                self.direction.y = 1 if dy > 0 else -1
                self.facing = 'down' if dy > 0 else 'up'
        else:
            # Random movement
            if not self.movement_decided:
                self.direction = pygame.math.Vector2(0, 0)
                move_choice = rand.choice(['up', 'down', 'left', 'right', 'idle'])
                if move_choice == 'up':
                    self.direction.y = -1
                    self.facing = 'up'
                elif move_choice == 'down':
                    self.direction.y = 1
                    self.facing = 'down'
                elif move_choice == 'left':
                    self.direction.x = -1
                    self.facing = 'left'
                elif move_choice == 'right':
                    self.direction.x = 1
                    self.facing = 'right'
                else:
                    self.direction.x = 0
                    self.direction.y = 0
                self.decision_time = pygame.time.get_ticks()
                self.movement_decided = True
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.decision_time > 2000:
                    self.movement_decided = False
        
        # Move X axis, check collision
        self.hitbox.x += self.direction.x * self.speed
        self.rect.center = self.hitbox.center
        if self._check_wall_collision(walls):
            self.hitbox.x -= self.direction.x * self.speed
            self.movement_decided = False

        # Move Y axis, check collision
        self.hitbox.y += self.direction.y * self.speed
        self.rect.center = self.hitbox.center
        if self._check_wall_collision(walls):
            self.hitbox.y -= self.direction.y * self.speed
            self.movement_decided = False

        self._update_movement_animation()
        self.rect.center = self.hitbox.center

    def _check_wall_collision(self, walls):
        """Kontroluje kolizi se zdmi a vraci True, pokud dojde ke kolizi."""
        if walls is None:
            return False
        for wall in walls:
            if self.hitbox.colliderect(wall.rect):
                return True
        return False
    
    def _handle_attack_animation(self, keys):
        if not self.enemy_in_range():
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

    def enemy_in_range(self):
        if self.target_player is None:
            return False
        attack_range = 75  # Define attack range
        skeleton_pos = pygame.math.Vector2(self.hitbox.center)
        player_pos = pygame.math.Vector2(self.target_player.hitbox.center)
        distance = skeleton_pos.distance_to(player_pos)
        # Face toward the player if in range
        if distance <= attack_range:
            dx = player_pos.x - skeleton_pos.x
            dy = player_pos.y - skeleton_pos.y
            if abs(dx) > abs(dy):
                self.facing = 'right' if dx > 0 else 'left'
            else:
                self.facing = 'down' if dy > 0 else 'up'
        return distance <= attack_range
    def _handle_attack(self, keys):
        if self.enemy_in_range() == False:
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

    
    def _frame_update(self):
        if not self.is_alive:
            # Stay frozen on the last death frame
            self.current_frame = len(self.animations["death"]) - 1
            self.image = self.animations["death"][self.current_frame]
            self.rect = self.image.get_rect(center=self.hitbox.center)
            return

        # For death animation: advance frame WITHOUT wrapping (stop at last frame)
        if self.current_animation == "death":
            now = pygame.time.get_ticks()
            if now - self.last_update > FRAME_CHANGE_DELAY:
                self.last_update = now
                if self.current_frame < len(self.animations["death"]) - 1:
                    self.current_frame += 1
            self.image = self.animations[self.current_animation][self.current_frame]
            self.rect = self.image.get_rect(center=self.hitbox.center)
            return

        super()._frame_update()

    def _check_death_animation_finished(self):
        if (
            self.current_animation == "death"
            and self.current_frame == len(self.animations["death"]) - 1
            and self.is_alive
        ):
            self.is_alive = False
            self.death_time = pygame.time.get_ticks() + 5400

        if not self.is_alive:
            self.__remove_dead_enemy()

    def __remove_dead_enemy(self):
        if pygame.time.get_ticks() >= self.death_time:
            self.kill()

if __name__ == "__main__":
    import pokus1
