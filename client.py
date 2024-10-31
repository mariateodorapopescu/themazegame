import socket
import argparse
from agent import AgentRandom
from agent_astar import AStarAgent
from agent_dfs import DFSAgent
import numpy as np
import struct
from constants import Constants

def interpret_fov(fov : bytes, size : int):
    fov = fov.decode("utf-8")
    print(fov)
    return ""

# Testăm parsarea de argumente
parser = argparse.ArgumentParser(description='Client pentru agent')
parser.add_argument('--agent', choices=['astar', 'dfs', 'random'], default='astar', help='Tipul agentului de utilizat')
args = parser.parse_args()

# Creăm un socket și ne conectăm la server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(True)
sock.connect(Constants.ADDR)

# Folosim agentul specificat pentru navigare
if args.agent == 'astar':
    agent = AStarAgent(view_range=3)  # Agent A*
if args.agent == 'random':
    agent = AgentRandom(view_range=3)
else:
    agent = DFSAgent(view_range=3)  # Agent DFS

# Primim câmpul de vedere de la server
field_of_view = sock.recv(Constants.MAX_SERVER_RESPONSE_SIZE)
field_of_view = interpret_fov(field_of_view, agent.view_range)
print("Câmpul de vedere primit:")
print(field_of_view)
exit(1)

# Client code snippet
while True:
    request = agent.create_request(field_of_view)
    sock.send(request)

    # Primim actualizările de la server
    try:
        field_of_view = sock.recv(Constants.MAX_SERVER_RESPONSE_SIZE)
        if not field_of_view:  # Verificăm dacă conexiunea este închisă
            print("Conexiunea cu serverul a fost închisă.")
            break
        field_of_view = interpret_fov(field_of_view, agent.view_range)
        print("Câmpul de vedere actualizat:")
        print(field_of_view)
    except Exception as e:
        print(f"Eroare la primirea datelor: {e}")
        break

# Închidem conexiunea la final
sock.close()
