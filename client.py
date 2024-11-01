import socket
import argparse
from agent import AgentRandom
from agent_astar import AStarAgent
from agent_dfs import DFSAgent
import numpy as np
import struct
import json
from constants import Constants

def interpret_fov(fov : bytes, size : int):
    fov = fov.decode(Constants.ENCODING)
    # Replace semicolons and reformat the string
    fov = fov.replace(';', '], [')
    fov = f"np.array([{fov}])"
    return np.array(eval(fov), dtype=np.uint8)

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
field_of_view  = interpret_fov(field_of_view, agent.view_range)

# Client code snippet
while True:
    request = agent.create_request(field_of_view)
    sock.send(request)
    # Primim actualizările de la server
    try:
        response = sock.recv(Constants.MAX_SERVER_RESPONSE_SIZE)
        if not response:  # Verificăm dacă conexiunea este închisă
            print("Conexiunea cu serverul a fost închisă.")
            break
        response = json.loads(response)
        # print(response)
    except Exception as e:
        print(f"Eroare la primirea datelor: {e}")
        break

# Închidem conexiunea la final
sock.close()
