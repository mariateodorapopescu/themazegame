import numpy as np
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
        self.map : np.array = []
        
        self.x = int(Constants.INITIAL_ESTIMATED_SIZE / 2)
        self.y = int(Constants.INITIAL_ESTIMATED_SIZE / 2)  

    def create_initial_map(self, fov):
        height, width = fov.shape
        self.map = np.zeros(shape=(Constants.INITIAL_ESTIMATED_SIZE,
                             Constants.INITIAL_ESTIMATED_SIZE))
        for i in range(height):
            for j in range(width):
                self.map[self.x - height + i][self.y - width + j] = fov[i][j]
        

    def _chooseDirection(self):
        current = []
        x = self.x
        y = self.y
        if (x < 2 * self.view_range):
            if (map[x + 1][y] != Constants.WALL):
                current.append("S")
        if (x > 0):
            if (map[x - 1][y] != Constants.WALL):
                current.append("N")
        if (y > 0):
            if (map[x][y - 1] != Constants.WALL):
                current.append("W")
        if (y < 2 * self.view_range):
            if (map[x][y + 1] != Constants.WALL):
                current.append("E")
        return np.random.choice(current)
    
    def _modifyCoordinates(self, x : int, y : int, letter):
        if (letter == "S"):
            return x + 1, y
        if (letter == "N"):
            return x - 1, y
        if (letter == "W"):
            return x, y- 1
        if (letter == "E"):
            return x, y + 1


    def _createTravelingPlan(self, field_of_view: np.array):
        directions = []
        for i in range(self.movements):
            direction = self._chooseDirection()
            directions.append(direction)
            self.x, self.y = self._modifyCoordinates(direction)
        return ''.join(directions)
    
    # trimite request la server respectand formatul specificat in enunt
    def create_request(self, field_of_view): 
        self.last_traveling_plan = self._createTravelingPlan(field_of_view)
        out = {"input": self.last_traveling_plan} 
        return bytes(json.dumps(out), Constants.ENCODING)
    
    def interpret_fov(self, fov : bytes):
        fov = fov.decode(Constants.ENCODING)
        # Replace semicolons and reformat the string
        fov = fov.replace(';', '], [')
        fov = f"np.array([{fov}])"
        return np.array(eval(fov), dtype=np.uint8)
    
    
    def interpret_response(self, response):
        print(len(self.last_traveling_plan))
        for idx, command in enumerate(self.last_traveling_plan):
            result = response["command" + str(idx + 1)]
            print(idx, result)
            print()