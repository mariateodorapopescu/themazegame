import socket
import argparse
from agent import AgentRandom
from agent_astar import AStarAgent
from agent_dfs import DFSAgent
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import Constants

class Client():
    def __init__(self, agent, addr):
        self.agent = agent
        self.addr = addr
        # Creăm un socket și ne conectăm la server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(True)
        self.sock.connect(self.addr)   
        # Primim câmpul de vedere de la server
        self.first_fov = self.sock.recv(Constants.MAX_SERVER_RESPONSE_SIZE)          
        
    def communicate(self):
        self.agent.create_initial_map(self.first_fov)
        while True:
            request = self.agent.create_request()
            self.sock.send(request)
            # Primim actualizările de la server
            try:
                response = self.sock.recv(Constants.MAX_SERVER_RESPONSE_SIZE)
                if not response:  # Verificăm dacă conexiunea este închisă
                    print("Conexiunea cu serverul a fost închisă.")
                    break
                self.agent.interpret_response(json.loads(response))
            except Exception as e:
                print(f"Eroare la primirea datelor: {e}")
                self.sock.close()
                break


# Testăm parsarea de argumente
parser = argparse.ArgumentParser(description='Client pentru agent')
parser.add_argument('--agent', choices=['astar', 'dfs', 'random'], default='astar', help='Tipul agentului de utilizat')
args = parser.parse_args()

# Folosim agentul specificat pentru navigare
if args.agent == 'astar':
    agent = AStarAgent(view_range=3)  # Agent A*
if args.agent == 'random':
    agent = AgentRandom(view_range=3)
else:
    agent = DFSAgent(view_range=3)  # Agent DFS

client : Client = Client(agent, Constants.ADDR)
client.communicate()
