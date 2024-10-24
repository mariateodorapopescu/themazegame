import socket
import argparse
from agent import Agent
import numpy as np
import struct
from constants import Constants

def interpret_fov(fov : bytes, size : int):
    value = np.frombuffer(fov, dtype=np.uint8)
    value = value.reshape((2 * size + 1, 2  * size + 1))
    return value

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('--id', action="store", dest='id', default=0)
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(True)
sock.connect(Constants.ADDR)
agent = Agent(3)
field_of_view = sock.recv(Constants.MAX_SERVER_RESPONSE_SIZE)
field_of_view = interpret_fov(field_of_view, agent.view_range)
print(field_of_view)
# while True:
#     sock.send(agent.create_request(field_of_view))
#     field_of_view = sock.recv()

sock.close()
