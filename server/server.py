import numpy as np
import socket
from CustomThread import CustomThread
from DFSGenerator import DFSGenerator
from viewer import Viewer
from maze import Maze

import sys
import os
import json
import getch

sys.path.append(os.path.abspath('../client'))
from client.agent_astar import AStarAgent
from constants import Constants

class Server():
    def __init__(self, timeout, max_clients_number : int, path_to_write : str, view_range : int):
        self.maze = None
        self.timeout = timeout
        self.max_clients_number = max_clients_number
        self.view_range = view_range
        self.path_to_write = path_to_write
        self.origin = None
        self.size = None
        self.seed = None

    def generate_maze(self, size : tuple[int, int], origin : tuple[int, int], seed : int):
        if (self.maze == None):
            maze = Maze(size[0], size[1], seed)
            generator : DFSGenerator = DFSGenerator(maze, size, origin)
            maze = generator.carve_maze()
            maze.save_layout_maze()
            maze.write_maze_to_file(self.path_to_write)
            self.origin = origin
            self.size = size
            self.seed = seed
            self.maze = maze
        else:
            print("Maze is already generated in this server.")
        
    def launch_viewer(self):
        if not self.maze == None:
            # VIEWER
            viewer = Viewer(self.maze)
            viewer.run()

    def wait_for_incoming_connections(self, address : tuple):
        # server is waiting for connections
        s = socket.create_server(address, family=socket.AF_INET, reuse_port=True)
        thread_list = []
        idx = 0
        # if connection found create a separate thread and socket, and make communication 
        # between the two of them in paralell, no longer listen after the server got
        # MAX_CLIENTS_NUMBER connections
        while True:
            sock, _ = s.accept()
            sock.settimeout(self.timeout)
            # LASATI VIRGULA ACOLO, TREBUIE LASAT SA CREADA INTERPRETORUL CA SUNT 2 PARAMETRII
            # adica (sock, None)
            thread = CustomThread(target=self._main_communication, args=(sock,))
            thread_list.append(thread)
            thread.start()
            idx += 1 
            if (idx == self.max_clients_number):
                break
        # Wait for threads to finish and get results
        for thread in thread_list:
            result = thread.join()
            print(result)
        s.close()

    # this is the function for communication between agent and server
    def _main_communication(self, my_sock : socket):
        agent_x, agent_y = self.origin
        fov = self.maze.get_field_of_view(agent_x, agent_y, self.view_range)
        #need to convert to bytes so i can send it to socket
        my_sock.send(bytes(get_fov_as_string(fov), encoding=Constants.ENCODING)) 

        while True:
            try:
                output = my_sock.recv(256).decode(Constants.ENCODING)
                request_object = json.loads(output)

                chain_of_commands : str = request_object["input"]
                results = np.zeros(shape=(len(chain_of_commands),))
                fov_list = [self.maze.get_field_of_view(agent_x, agent_y, self.view_range)]

                for idx, command in enumerate(chain_of_commands):
                    agent_x, agent_y, results[idx] = self.maze.adapt_agent_postion(agent_x, agent_y, command)
                    fov_list.append(self.maze.get_field_of_view(agent_x, agent_y, self.view_range))

                dictionary = create_reply_back(chain_of_commands, results, fov_list)
                my_sock.send(bytes(dictionary, Constants.ENCODING))

            except socket.timeout as err:
                return False
            if output == b'':
                print("Socket was closed by client server still up")
                return False
            print(output)

    

    


            
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
=======
>>>>>>> 7c1e434 (small changes)


TIMEOUT_REQUEST = 1.0
MAX_CLIENTS_NUMBER = 2
SIZE = (10, 10)
ORIGIN = (0, 0)
SEED = 36
server : Server = Server(TIMEOUT_REQUEST, MAX_CLIENTS_NUMBER, "./maze.png", Constants.INITIAL_VIEW_RANGE)
server.generate_maze(SIZE, ORIGIN, SEED)
# DO NOT RUN IT YET !!!!
# server.launch_viewer()
server.wait_for_incoming_connections(Constants.ADDR)



