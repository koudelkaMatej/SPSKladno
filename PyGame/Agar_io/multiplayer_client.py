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
        self.shared_blobs = {}
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
                # Send with new message format
                message = {
                    'type': 'player_update',
                    'data': player_data
                }
                self.client.send(pickle.dumps(message))
                self.my_player_data = player_data
            except Exception as e:
                print(f"Error sending data: {e}")
                self.connected = False
    
    def send_blob_eaten(self, blob_id):
        """Notify server that a blob was eaten"""
        if self.connected:
            try:
                message = {
                    'type': 'blob_eaten',
                    'blob_id': blob_id
                }
                self.client.send(pickle.dumps(message))
            except Exception as e:
                print(f"Error sending blob eaten: {e}")
    
    def receive_data(self):
        while self.connected:
            try:
                # First, receive the length of the message (4 bytes)
                raw_msglen = self.recv_all(4)
                if not raw_msglen:
                    break
                msglen = int.from_bytes(raw_msglen, byteorder='big')
                
                # Then receive the actual message
                raw_data = self.recv_all(msglen)
                if not raw_data:
                    break
                    
                data = pickle.loads(raw_data)
                
                if 'players' in data and 'blobs' in data:
                    # New format with game state
                    all_players = data['players']
                    self.shared_blobs = data['blobs']
                    
                    # Filter out own player data
                    self.other_players = {addr: player_data for addr, player_data in all_players.items() 
                                        if player_data.get('x') != self.my_player_data.get('x') or 
                                           player_data.get('y') != self.my_player_data.get('y')}
                else:
                    # Legacy format - just players
                    self.other_players = {addr: player_data for addr, player_data in data.items() 
                                        if player_data != self.my_player_data}
                    
            except Exception as e:
                print(f"Error receiving data: {e}")
                self.connected = False
                break
    
    def recv_all(self, n):
        """Helper method to receive exactly n bytes"""
        data = bytearray()
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data
    
    def disconnect(self):
        if self.connected:
            self.client.close()
            self.connected = False

def kdoCoZere(hrac_group, jidlo_group, client=None):
    eaten_blobs = []
    for hrac in hrac_group:
        for jidlo in jidlo_group:
            overlap = circle_overlap_percentage(hrac.x, hrac.y, hrac.radius, jidlo.x, jidlo.y, jidlo.radius)
            if overlap > 90:
                if hrac.radius >= jidlo.radius+5:
                    hrac.radius += int(jidlo.radius * 0.2)
                    hrac.image = pygame.Surface((hrac.radius * 2, hrac.radius * 2), pygame.SRCALPHA)
                    hrac.image.fill((0, 0, 0, 0))
                    pygame.draw.circle(hrac.image, hrac.color, (hrac.radius, hrac.radius), hrac.radius)
                    eaten_blobs.append(jidlo)
                elif jidlo.radius >= hrac.radius+5:
                    jidlo.radius += int(hrac.radius * 0.2)
                    jidlo.image = pygame.Surface((jidlo.radius * 2, jidlo.radius * 2), pygame.SRCALPHA)
                    jidlo.image.fill((0, 0, 0, 0))
                    pygame.draw.circle(jidlo.image, jidlo.color, (jidlo.radius, jidlo.radius), jidlo.radius)
                    print("sezral jsem", hrac.color)
                    hrac_group.remove(hrac)
    
    # Remove eaten blobs and notify server if client is provided
    for blob in eaten_blobs:
        jidlo_group.remove(blob)
        if client and hasattr(blob, 'blob_id'):
            client.send_blob_eaten(blob.blob_id)

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
    
    # Initialize player (color will be assigned by server)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_START_SIZE, WHITE)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    
    # Initialize game objects
    blob_group = pygame.sprite.Group()
    other_players_group = pygame.sprite.Group()
    
    # Camera offset for smooth scrolling
    camera_x = 0
    camera_y = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(PINK)
        
        # Get mouse position and update player
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Convert mouse position to world coordinates
        world_mouse_x = mouse_x - camera_x
        world_mouse_y = mouse_y - camera_y
        
        # Update player with world coordinates
        direction_x = world_mouse_x - player.x
        direction_y = world_mouse_y - player.y
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if distance >= 3.6:
            direction_x /= distance
            direction_y /= distance
            speed = 5
            player.x += direction_x * speed
            player.y += direction_y * speed
        
        # Update camera to follow player
        target_camera_x = SCREEN_WIDTH // 2 - player.x
        target_camera_y = SCREEN_HEIGHT // 2 - player.y
        
        # Smooth camera movement
        camera_x += (target_camera_x - camera_x) * 0.1
        camera_y += (target_camera_y - camera_y) * 0.1
        
        # Send player data to server
        client.send_player_data(player)
        
        # Update other players from server data
        other_players_group.empty()
        for addr, player_data in client.other_players.items():
            other_player = Player(player_data['x'], player_data['y'], 
                                player_data['radius'], player_data['color'])
            # Apply camera offset for rendering
            other_player.rect.center = (player_data['x'] + camera_x, player_data['y'] + camera_y)
            other_players_group.add(other_player)
        
        # Update blobs from server data
        blob_group.empty()
        for blob_id, blob_data in client.shared_blobs.items():
            blob = Blob(blob_data['x'], blob_data['y'], blob_data['radius'], blob_data['color'])
            blob.blob_id = blob_id  # Store the blob ID for server communication
            # Apply camera offset for rendering
            blob.rect.center = (blob_data['x'] + camera_x, blob_data['y'] + camera_y)
            blob_group.add(blob)
        
        # Apply camera offset to main player for rendering
        player.rect.center = (player.x + camera_x, player.y + camera_y)
        
        # Handle eating mechanics with server notification
        kdoCoZere(player_group, blob_group, client)
        kdoCoZere(other_players_group, blob_group, client)
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
        
        # Display blob count
        blob_count = len(client.shared_blobs)
        blob_text = font.render(f"Food: {blob_count}", True, WHITE)
        screen.blit(blob_text, (10, 90))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    # Cleanup
    client.disconnect()
    pygame.quit()

if __name__ == "__main__":
    main()