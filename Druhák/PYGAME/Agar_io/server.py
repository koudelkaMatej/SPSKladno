import socket
import threading
import pickle
import random
import time
from settings import *

# Server configuration
HOST = '172.16.21.1'  # Localhost
PORT = 5555         # Port to listen on

# Initialize server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server started on {HOST}:{PORT}")

clients = []
players = {}
shared_blobs = {}  # Shared food for all players
blob_id_counter = 0

# Available colors for players
AVAILABLE_COLORS = [WHITE,BLACK ,RED ,GREEN,BLUE ,YELLOW,ORANGE ,PURPLE ,PINK]

used_colors = set()

def get_unique_color():
    """Get a unique color for a new player"""
    available = [color for color in AVAILABLE_COLORS if color not in used_colors]
    if available:
        color = random.choice(available)
        used_colors.add(color)
        return color
    else:
        # If all colors are used, return a random color
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

def return_color(color):
    """Return a color to the available pool when player disconnects"""
    if color in used_colors:
        used_colors.remove(color)

def generate_blob():
    """Generate a new food blob"""
    global blob_id_counter
    blob_id_counter += 1
    blob = {
        'id': blob_id_counter,
        'x': random.randint(10, 1200),  # Wider area than screen
        'y': random.randint(10, 1200),
        'radius': 5,
        'color': (144, 238, 144)  # LIGHT_GREEN
    }
    shared_blobs[blob_id_counter] = blob
    return blob

def remove_blob(blob_id):
    """Remove a blob when it's eaten"""
    if blob_id in shared_blobs:
        del shared_blobs[blob_id]

# Generate initial blobs
for _ in range(50):
    generate_blob()

# Periodically generate new blobs
def blob_generator():
    while True:
        time.sleep(2)  # Generate new blob every 2 seconds
        if len(shared_blobs) < 100:  # Keep maximum 100 blobs
            generate_blob()

# Start blob generation thread
blob_thread = threading.Thread(target=blob_generator, daemon=True)
blob_thread.start()

# Broadcast data to all clients
def broadcast(data):
    for client in clients[:]:  # Use slice copy to avoid modification during iteration
        try:
            # Serialize the data
            serialized_data = pickle.dumps(data)
            # Send the length first (4 bytes)
            message_length = len(serialized_data)
            client.send(message_length.to_bytes(4, byteorder='big'))
            # Then send the actual data
            client.send(serialized_data)
        except Exception as e:
            print(f"Error broadcasting to client: {e}")
            clients.remove(client)

# Handle individual client
def handle_client(client, addr):
    print(f"New connection: {addr}")
    
    # Assign unique color to new player
    player_color = get_unique_color()
    
    while True:
        try:
            # Receive data with a timeout to avoid blocking indefinitely
            client.settimeout(10.0)
            raw_data = client.recv(1024)
            
            # Check if client disconnected (empty data)
            if not raw_data:
                print(f"Client {addr} disconnected (empty data)")
                break
                
            data = pickle.loads(raw_data)
            
            # Handle different message types
            if 'type' in data:
                if data['type'] == 'player_update':
                    # Update player data with assigned color
                    player_data = data['data']
                    player_data['color'] = player_color
                    players[addr] = player_data
                elif data['type'] == 'blob_eaten':
                    # Remove eaten blob
                    blob_id = data['blob_id']
                    remove_blob(blob_id)
                    # Generate a new blob to replace the eaten one
                    generate_blob()
            else:
                # Legacy format - assume it's player data
                data['color'] = player_color
                players[addr] = data
            
            # Send game state to all clients
            game_state = {
                'players': players,
                'blobs': shared_blobs
            }
            broadcast(game_state)
            
        except socket.timeout:
            print(f"Timeout for client {addr}")
            break
        except (pickle.UnpicklingError, pickle.PickleError) as e:
            print(f"Pickle error from {addr}: {e}")
            continue
        except Exception as e:
            print(f"Connection lost: {addr} - Error: {e}")
            break
    
    # Cleanup when client disconnects
    if client in clients:
        clients.remove(client)
    if addr in players:
        return_color(players[addr].get('color'))  # Return color to pool
        del players[addr]
        game_state = {
            'players': players,
            'blobs': shared_blobs
        }
        broadcast(game_state)
    
    try:
        client.close()
    except:
        pass

# Accept new clients
def accept_clients():
    while True:
        client, addr = server.accept()
        print(f"Connected by {addr}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client, addr)).start()

# Start accepting clients
accept_thread = threading.Thread(target=accept_clients)
accept_thread.start()