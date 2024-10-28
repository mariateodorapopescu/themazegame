import numpy as np
from constants import Constants
import json
import heapq

class AStarAgent:
    def __init__(self, view_range=5): 
        self.RC_points = 10
        self.view_range = view_range
        self.movements = 10

    def _heuristic(self, a, b):
        # Folosim distanța Manhattan ca euristică pentru algoritmul A*
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _get_neighbors(self, x, y, field_of_view):
        neighbors = []
        if x > 0 and field_of_view[x - 1][y] != Constants.WALL:
            neighbors.append((x - 1, y, "N"))
        if x < field_of_view.shape[0] - 1 and field_of_view[x + 1][y] != Constants.WALL:
            neighbors.append((x + 1, y, "S"))
        if y > 0 and field_of_view[x][y - 1] != Constants.WALL:
            neighbors.append((x, y - 1, "W"))
        if y < field_of_view.shape[1] - 1 and field_of_view[x][y + 1] != Constants.WALL:
            neighbors.append((x, y + 1, "E"))
        return neighbors

    def _a_star(self, start, goal, field_of_view):
        open_list = []
        heapq.heappush(open_list, (0, start))
        came_from = {}
        cost_so_far = {start: 0}

        while open_list:
            current_priority, current = heapq.heappop(open_list)
            # _, current = heapq.heappop(open_list)

            if current == goal:
                # Reconstruim calea de la start la țintă
                path = []
                while current in came_from:
                    prev = came_from[current]
                    if prev[0] < current[0]:
                        path.append("S")  # Mergem spre Sud
                    elif prev[0] > current[0]:
                        path.append("N")  # Mergem spre Nord
                    elif prev[1] < current[1]:
                        path.append("E")  # Mergem spre Est
                    elif prev[1] > current[1]:
                        path.append("W")  # Mergem spre Vest
                    current = prev
                path.reverse()  # Răsturnăm calea pentru a o obține de la start la țintă
                return path

            # Explorăm vecinii
            for neighbor_x, neighbor_y, direction in self._get_neighbors(current[0], current[1], field_of_view):
                new_cost = cost_so_far[current] + 1
                next_node = (neighbor_x, neighbor_y)
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self._heuristic(goal, next_node)
                    heapq.heappush(open_list, (priority, next_node))
                    came_from[next_node] = current

        return []  # Returnăm o listă goală dacă nu se găsește nicio cale

    def _find_goal(self, field_of_view):
        # Localizăm ieșirea în câmpul de vedere
        goal = np.where(field_of_view == Constants.EXIT)
        if goal[0].size > 0:
            return goal[0][0], goal[1][0]
        return None

    def create_request(self, field_of_view):
        start = (self.view_range, self.view_range)  # Agentul este mereu în centru
        goal = self._find_goal(field_of_view)
        if not goal:
            return bytes(json.dumps({"input": ""}), 'utf-8')  # Nu a găsit o țintă, trimite cerere goală

        path = self._a_star(start, goal, field_of_view)
        directions = ''.join(path[:self.movements])  # Limităm numărul de mișcări
        return bytes(json.dumps({"input": directions}), 'utf-8')
    