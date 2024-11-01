import numpy as np
from constants import Constants
import json

class DFSAgent:
    def __init__(self, view_range=5):
        self.view_range = view_range
        self.path = []  # Path taken by the agent
        self.visited = set()  # Set to track visited cells
        self.move_history = []  # List to track the movement history
        self.last_traveling_plan : list[str] = [] 

    def _get_neighbors(self, x, y, field_of_view):
        neighbors = []
        # Check all four possible directions
        if x > 0 and field_of_view[x - 1][y] != Constants.WALL:  # North
            neighbors.append((x - 1, y))
        if x < field_of_view.shape[0] - 1 and field_of_view[x + 1][y] != Constants.WALL:  # South
            neighbors.append((x + 1, y))
        if y > 0 and field_of_view[x][y - 1] != Constants.WALL:  # West
            neighbors.append((x, y - 1))
        if y < field_of_view.shape[1] - 1 and field_of_view[x][y + 1] != Constants.WALL:  # East
            neighbors.append((x, y + 1))
        return neighbors

    def _update_and_display_maze(self, field_of_view, current):
        # Actualizează matricea cu poziția curentă a agentului
        display_maze = np.copy(field_of_view)  # Facem o copie a matricei
        display_maze[current] = Constants.AGENT  # Folosește o constantă pentru a marca agentul
        
        print("Matricea actualizată:")
        print(display_maze)  # Afișează matricea

    def _dfs(self, current, goal, field_of_view):
        if current in self.visited:
            return False  # Already visited this cell

        self.visited.add(current)  # Mark the current cell as visited
        self._update_and_display_maze(field_of_view, current)  # Update and display the maze
        self.move_history.append(current) # Append the current cell to the movement history

        if current == goal:
            return True  # Found the goal!

        # Get neighboring cells
        neighbors = self._get_neighbors(current[0], current[1], field_of_view)

        for neighbor in neighbors:
            if self._dfs(neighbor, goal, field_of_view):
                self.path.append(neighbor)  # Append path if the goal is found
                return True  # Backtrack if found

        return False  # Goal not found from this path

    def _find_goal(self, field_of_view):
        goal = np.where(field_of_view == Constants.EXIT)
        if goal[0].size > 0:
            return goal[0][0], goal[1][0]
        return None

    def create_request(self, field_of_view):
        start = (self.view_range, self.view_range)  # Start in the center
        goal = self._find_goal(field_of_view)
        if not goal:
            return bytes(json.dumps({"input": ""}), 'utf-8')  # No goal found

        self.path = []  # Reset path for new search
        self.visited = set()  # Reset visited cells
        self.move_history = []  # Reset movement history
        found = self._dfs(start, goal, field_of_view)
        print(found)
        if found:
            # Create a request based on the path found
            self.last_traveling_plan = self._convert_path_to_directions(start)
            print("Istoricul mutărilor:", self.move_history)
            return bytes(json.dumps({"input": self.last_traveling_plan}), 'utf-8')
        else:
            print("Nu s-a găsit o cale.")
            return bytes(json.dumps({"input": ""}), 'utf-8')  # No path found
        
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

    def _convert_path_to_directions(self, start):
        directions = []
        current = start
        for next_cell in self.path:
            if next_cell[0] < current[0]:
                directions.append("N")  # Move North
            elif next_cell[0] > current[0]:
                directions.append("S")  # Move South
            elif next_cell[1] < current[1]:
                directions.append("W")  # Move West
            elif next_cell[1] > current[1]:
                directions.append("E")  # Move East
            current = next_cell
        directions.reverse()  # Reverse the directions to go from start to goal
        return ''.join(directions)
    
    
