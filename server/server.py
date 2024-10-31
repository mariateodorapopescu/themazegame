import numpy as np
import socket
from CustomThread import CustomThread
from DFSGenerator import DFSGenerator
import sys
import os

sys.path.append(os.path.abspath('../'))
from constants import Constants
from maze import Maze

TIMEOUT_REQUEST = 1.0
MAX_CLIENTS_NUMBER = 2
SIZE = (7, 7)
ORIGIN = (0, 0)
SEED = 36

# this is the function for communication between agent and server
def main_communication(my_sock : socket, maze : Maze, idx : int):
    fov = maze.get_field_of_view(ORIGIN[0], ORIGIN[1], 3)
    fov = bytes(fov.flatten())
    my_sock.send(fov) #need to convert to bytes so i can send it to socket
    while True:
        try:
            output = my_sock.recv(256)
        except socket.timeout as err:
            return False
        if output == b'':
            print("Socket was closed by client server still up")
            return False
        print(output)
    return True

# ORIGIN is the place where the agent will initially start searching
generator : DFSGenerator = DFSGenerator(SIZE, SEED, ORIGIN) 
maze = generator.carve_maze()
maze.write_maze_to_file("../da.png")
maze.save_layout_maze()
maze.write_to_output()
print()

# server is waiting for connections
s = socket.create_server(Constants.ADDR, family=socket.AF_INET, reuse_port=True)
thread_list = []
idx = 0

# if connection found create a separate thread and socket, and make communication 
# between the two of them in paralell, no longer listen after the server got
# MAX_CLIENTS_NUMBER connections
while True:
    sock, _ = s.accept()
    sock.settimeout(TIMEOUT_REQUEST)
    thread = CustomThread(target=main_communication, args=(sock, maze, idx))
    thread_list.append(thread)
    thread.start()
    idx += 1 
    if (idx == MAX_CLIENTS_NUMBER):
        break

# we are waiting for the thread output to tell us if the agent got succesfully out of the maze
#for idx in range(len(thread_list)):
#    thread : CustomThread = thread_list[idx]
#    result = thread.join()
#    print(result)

# Wait for threads to finish and get results
for thread in thread_list:
    result = thread.join()
    print(result)
s.close()

