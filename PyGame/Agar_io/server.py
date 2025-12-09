import socket
import threading
import pickle

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

# Broadcast data to all clients
def broadcast(data):
    for client in clients:
        try:
            client.send(pickle.dumps(data))
        except:
            clients.remove(client)

# Handle individual client
def handle_client(client, addr):
    print(f"New connection: {addr}")
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
            players[addr] = data
            broadcast(players)
        except socket.timeout:
            print(f"Timeout for client {addr}")
            break
        except (pickle.UnpicklingError, pickle.PickleError) as e:
            print(f"Pickle error from {addr}: {e}")
            # Continue to try receiving more data instead of breaking
            continue
        except Exception as e:
            print(f"Connection lost: {addr} - Error: {e}")
            break
    
    # Cleanup when client disconnects
    if client in clients:
        clients.remove(client)
    if addr in players:
        del players[addr]
        broadcast(players)
    
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