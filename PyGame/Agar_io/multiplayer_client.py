import pygame
import socket
import pickle
import threading
from settings import *
from Player import Player
from Blob import Blob
from circle_overlap_percentage import circle_overlap_percentage

class MultiplayerClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = '172.16.21.1'
        self.server_port = 5555
        self.connected = False
        self.other_players = {}
        self.my_player_data = None
        
    def connect_to_server(self):
        try:
            self.client.connect((self.server_ip, self.server_port))
            self.connected = True
            print(f"Connected to server {self.server_ip}:{self.server_port}")
            # Start receiving thread
            receive_thread = threading.Thread(target=self.receive_data)
            receive_thread.daemon = True
            receive_thread.start()
            return True
        except Exception as e:
            print(f"Failed to connect to server: {e}")
            return False
    
    def send_player_data(self, player):
        if self.connected:
            try:
                player_data = {
                    'x': player.x,
                    'y': player.y,
                    'radius': player.radius,
                    'color': player.color
                }
                self.client.send(pickle.dumps(player_data))
                self.my_player_data = player_data
            except Exception as e:
                print(f"Error sending data: {e}")
                self.connected = False
    
    def receive_data(self):
        while self.connected:
            try:
                data = pickle.loads(self.client.recv(1024))
                # Filter out own player data
                self.other_players = {addr: player_data for addr, player_data in data.items() 
                                    if player_data != self.my_player_data}
            except Exception as e:
                print(f"Error receiving data: {e}")
                self.connected = False
                break
    
    def disconnect(self):
        if self.connected:
            self.client.close()
            self.connected = False

def kdoCoZere(hrac_group, jidlo_group):
    for hrac in hrac_group:
        for jidlo in jidlo_group:
            overlap = circle_overlap_percentage(hrac.x, hrac.y, hrac.radius, jidlo.x, jidlo.y, jidlo.radius)
            if overlap > 90:
                if hrac.radius >= jidlo.radius+5:
                    hrac.radius += int(jidlo.radius * 0.2)
                    hrac.image = pygame.Surface((hrac.radius * 2, hrac.radius * 2), pygame.SRCALPHA)
                    hrac.image.fill((0, 0, 0, 0))
                    pygame.draw.circle(hrac.image, hrac.color, (hrac.radius, hrac.radius), hrac.radius)
                    jidlo_group.remove(jidlo)
                elif jidlo.radius >= hrac.radius+5:
                    jidlo.radius += int(hrac.radius * 0.2)
                    jidlo.image = pygame.Surface((jidlo.radius * 2, jidlo.radius * 2), pygame.SRCALPHA)
                    jidlo.image.fill((0, 0, 0, 0))
                    pygame.draw.circle(jidlo.image, jidlo.color, (jidlo.radius, jidlo.radius), jidlo.radius)
                    print("sezral jsem", hrac.color)
                    hrac_group.remove(hrac)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Agar.io Multiplayer Client")
    clock = pygame.time.Clock()
    
    # Initialize multiplayer client
    client = MultiplayerClient()
    if not client.connect_to_server():
        print("Failed to connect to server. Exiting...")
        return
    
    # Initialize player
    player_colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, WHITE, BLACK]
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_START_SIZE, player_colors.pop())
    player_group = pygame.sprite.Group()
    player_group.add(player)
    
    # Initialize game objects
    blob_group = pygame.sprite.Group()
    other_players_group = pygame.sprite.Group()
    
    # Blob generation timer
    GENERATE_BLOBS = pygame.USEREVENT + 1
    pygame.time.set_timer(GENERATE_BLOBS, 5000)
    
    scroolx_speed = PLAYER_SPEED
    scrooly_speed = PLAYER_SPEED
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == GENERATE_BLOBS:
                for i in range(5):
                    blob_group.add(Blob())
        
        # Clear screen
        screen.fill(PINK)
        
        # Get mouse position and update player
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_group.update(mouse_x, mouse_y)
        
        # Send player data to server
        client.send_player_data(player)
        
        # Update other players from server data
        other_players_group.empty()
        for addr, player_data in client.other_players.items():
            other_player = Player(player_data['x'], player_data['y'], 
                                player_data['radius'], player_data['color'])
            other_players_group.add(other_player)
        
        # Handle scrolling
        if mouse_x < 100:
            for sprite in list(player_group.sprites()) + list(other_players_group.sprites()) + list(blob_group.sprites()):
                sprite.rect.centerx += scroolx_speed
                sprite.x += scroolx_speed
        elif mouse_x > SCREEN_WIDTH - 100:
            for sprite in list(player_group.sprites()) + list(other_players_group.sprites()) + list(blob_group.sprites()):
                sprite.rect.centerx -= scroolx_speed
                sprite.x -= scroolx_speed
                
        if mouse_y < 100:
            for sprite in list(player_group.sprites()) + list(other_players_group.sprites()) + list(blob_group.sprites()):
                sprite.rect.centery += scrooly_speed
                sprite.y += scrooly_speed
        elif mouse_y > SCREEN_HEIGHT - 100:
            for sprite in list(player_group.sprites()) + list(other_players_group.sprites()) + list(blob_group.sprites()):
                sprite.rect.centery -= scrooly_speed
                sprite.y -= scrooly_speed
        
        # Handle eating mechanics
        kdoCoZere(player_group, blob_group)
        kdoCoZere(other_players_group, blob_group)
        kdoCoZere(player_group, other_players_group)
        kdoCoZere(other_players_group, other_players_group)
        
        # Draw everything
        blob_group.draw(screen)
        player_group.draw(screen)
        other_players_group.draw(screen)
        
        # Display connection status
        font = pygame.font.Font(None, 36)
        status_text = "Connected" if client.connected else "Disconnected"
        status_color = GREEN if client.connected else RED
        text_surface = font.render(f"Status: {status_text}", True, status_color)
        screen.blit(text_surface, (10, 10))
        
        # Display player count
        player_count = len(client.other_players) + 1
        count_text = font.render(f"Players: {player_count}", True, WHITE)
        screen.blit(count_text, (10, 50))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    # Cleanup
    client.disconnect()
    pygame.quit()

if __name__ == "__main__":
    main()