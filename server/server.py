import numpy as np
import socket
from CustomThread import CustomThread
from DFSGenerator import DFSGenerator
from agent_astar import AStarAgent

import sys
import os
import json
import getch

sys.path.append(os.path.abspath('../'))
from constants import Constants
from maze import Maze
from viewer import Viewer


TIMEOUT_REQUEST = 1.0
MAX_CLIENTS_NUMBER = 2
SIZE = (10, 10)
ORIGIN = (0, 0)
SEED = 36


def get_fov_as_string(fov : np.array):
    out = np.array_str(fov)
    out = out.replace('[', '')
    out = out.replace(']', '')
    out = out.replace("  ", '')
    out = out.replace('\n ', ';')
    out = out.replace(' ', ', ')
    out = out.replace(';', '; ')
    return "[" + out + "]"
    
    
def create_reply_back(chain_of_commands : str, result : np.array, fov_list : list):
    dictionary = {}
    last_view_of_agent = fov_list[0]
    for i, status in enumerate(result):
        if (status == Constants.SUCCESS):
            dictionary["command" + str(i + 1)] = {
                "name": chain_of_commands[i],
                "successful": str(Constants.SUCCESS),
                "view": get_fov_as_string(fov_list[i])
            }
            last_view_of_agent = fov_list[i]
        if (status == Constants.FAIL):
            dictionary["command" + str(i + 1)] = {
                "name": chain_of_commands[i],
                "successful": str(Constants.FAIL),
                "view": get_fov_as_string(last_view_of_agent)
            }
    return json.dumps(dictionary)

# this is the function for communication between agent and server
def main_communication(my_sock : socket, maze : Maze):
    agent_x, agent_y = ORIGIN
    height, width = maze.layout.shape
    view_range = Constants.INITIAL_VIEW_RANGE
    fov = maze.get_field_of_view(agent_x, agent_y, view_range)
    #need to convert to bytes so i can send it to socket
    my_sock.send(bytes(get_fov_as_string(fov), encoding=Constants.ENCODING)) 

    while True:
        try:
            output = my_sock.recv(256).decode(Constants.ENCODING)
            request_object = json.loads(output)
           
            chain_of_commands : str = request_object["input"]
            results = np.zeros(shape=(len(chain_of_commands),))
            fov_list = [maze.get_field_of_view(agent_x, agent_y, view_range)]

            for idx, letter in enumerate(chain_of_commands):
                if (letter == "N"):
                    if (agent_x == 0):
                        break
                    agent_x = agent_x - 1
                if (letter == "S"):
                    if (agent_x == height - 1):
                        break
                    agent_x = agent_x + 1
                if (letter == "W"):
                    if (agent_y == 0):
                        break
                    agent_y = agent_y - 1
                if (letter == "E"):
                    if (agent_y == width - 1):
                        break
                    agent_y = agent_y + 1
                results[idx] = Constants.SUCCESS
                fov_list.append(maze.get_field_of_view(agent_x, agent_y, view_range))
            dictionary = create_reply_back(chain_of_commands, results, fov_list)
            my_sock.send(bytes(dictionary, Constants.ENCODING))
                
        except socket.timeout as err:
            return False
        if output == b'':
            print("Socket was closed by client server still up")
            return False
        print(output)
        # getch.getch()
    return True


# MAZE GENERATION

# ORIGIN is the place where the agent will initially start searching
maze = Maze(SIZE[0], SIZE[1], SEED)
generator : DFSGenerator = DFSGenerator(maze, SIZE, ORIGIN)
#generator : DFSGenerator = DFSGenerator(SIZE, SEED, ORIGIN) 
maze = generator.carve_maze()
maze.generate_start_end_points()
maze.write_maze_to_file("../maze.png")
#maze.save_layout_maze()
maze.write_to_output()
print()

# AGENTS
#agent = AStarAgent(view_range=5)

# VIEWER
viewer = Viewer(maze)
#viewer = Viewer(maze, "../maze.png")
viewer.run()

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
    thread = CustomThread(target=main_communication, args=(sock, maze))
    thread_list.append(thread)
    thread.start()
    idx += 1 
    if (idx == MAX_CLIENTS_NUMBER):
        break

# Wait for threads to finish and get results
for thread in thread_list:
    result = thread.join()
    print(result)
s.close()

