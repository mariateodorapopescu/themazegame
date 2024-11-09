import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import Constants
import json 

# nu am un algoritm clar implementat aici, alegeam in mod random urmatoarea pozitie
# doar pentru a testa comunicarea client - server
# fiecare agent va implementa cate un algoritm diferit, poate va trebui de schimbat 
# numele clasei
class AgentRandom:
    def __init__(self, view_range = 5):
        self.RC_points = 10
        self.view_range = view_range
        self.movements = 10 # cat de multe comenzi are voie sa dea de o data  
        self.last_traveling_plan : list[str] = []
        self.local_map : np.array = []
        
        self.x = int(Constants.INITIAL_ESTIMATED_SIZE / 2) + 1
        self.y = int(Constants.INITIAL_ESTIMATED_SIZE / 2) + 1

    def create_initial_map(self, fov : bytes):
        fov : np.array = self.interpret_fov(fov)
        height, width = fov.shape
        self.local_map = np.zeros(shape=(Constants.INITIAL_ESTIMATED_SIZE,
                             Constants.INITIAL_ESTIMATED_SIZE))
        for i in range(height):
            for j in range(width):
                self.local_map[self.x - int(height / 2) + i][self.y - int(width / 2) + j] = fov[i][j]

    def _chooseDirection(self):
        current = []
        x = self.x
        y = self.y
        if (self.local_map[x + 1][y] != Constants.WALL):
            current.append("S")
        if (self.local_map[x - 1][y] != Constants.WALL):
            current.append("N")
        if (self.local_map[x][y - 1] != Constants.WALL):
            current.append("W")
        if (self.local_map[x][y + 1] != Constants.WALL):
            current.append("E")
        return np.random.choice(current)
    
    def _modifyCoordinates(self, letter):
        if (letter == "S"):
            return self.x + 1, self.y
        if (letter == "N"):
            return self.x - 1, self.y
        if (letter == "W"):
            return self.x, self.y - 1
        if (letter == "E"):
            return self.x, self.y + 1


    def _createTravelingPlan(self):
        directions = []
        for i in range(self.movements):
            direction = self._chooseDirection()
            directions.append(direction)
            self.x, self.y = self._modifyCoordinates(direction)
        return ''.join(directions)
    
    # trimite request la server respectand formatul specificat in enunt
    def create_request(self): 
        self.last_traveling_plan = self._createTravelingPlan()
        out = {"input": self.last_traveling_plan} 
        return bytes(json.dumps(out), Constants.ENCODING)
    
    def interpret_fov(self, fov : bytes):
        fov = fov.decode(Constants.ENCODING)
        # Replace semicolons and reformat the string
        fov = fov.replace(';', '], [')
        fov = f"np.array([{fov}])"
        return np.array(eval(fov), dtype=np.uint8)

    def _adapt_map_in_north(self, fov : np.array):
        height, width = fov.shape
        for i in range(width):
            self.local_map[self.x - int(height / 2) - 1][self.y - int(width / 2) + i] = fov[0][i]
    
    def _adapt_map_in_south(self, fov : np.array):
        height, width = fov.shape
        for i in range(width):
            self.local_map[self.x + int(height / 2) + 1][self.y - int(width / 2) + i] = fov[height - 1][i]
    
    def _adapt_map_in_west(self, fov : np.array):
        height, width = fov.shape
        for i in range(height):
            self.local_map[self.x - int(height / 2) + i][self.y - int(width / 2) - 1] = fov[i][0]

    def _adapt_map_in_east(self, fov : np.array):
        height, width = fov.shape
        for i in range(height):
            self.local_map[self.x - int(height / 2) + i][self.y + int(width / 2) + 1] = fov[i][width - 1]
    
    
    def _interpret_command_reply(self, conmmand_result):
        if(int(conmmand_result["successful"]) == Constants.SUCCESS):
            command_type = conmmand_result["name"]
            fov = self.interpret_fov(bytes(conmmand_result["view"], Constants.ENCODING))
            if (command_type == "N"):
                self._adapt_map_in_north(fov)
            if (command_type == "S"):
                self._adapt_map_in_south(fov)
            if (command_type == "W"):
                self._adapt_map_in_west(fov)
            if (command_type == "E"):
                self._adapt_map_in_east(fov)

    def interpret_response(self, response):
        for idx, _ in enumerate(self.last_traveling_plan):
            command_result = response["command" + str(idx + 1)]
            self._interpret_command_reply(command_result)