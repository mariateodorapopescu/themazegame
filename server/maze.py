import numpy as np
import struct
import cv2
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import Constants
import cv2
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import Constants

class MazeCell:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.value = 0
        self.N = 0
        self.S = 0
        self.W = 0
        self.E = 0
    
    def breakWall(self, other : "MazeCell"):
        if self.x == other.x:
            if (self.y == other.y + 1):
                self.W = 1
                other.E = 1
                return self, other
            if (self.y + 1 == other.y):
                self.E = 1
                other.W = 1
                return self, other
        if self.y == other.y:
            if (self.x == other.x + 1):
                self.N = 1
                other.S = 1
                return self, other
            if (self.x + 1 == other.x):
                self.S = 1
                other.N = 1
                return self, other


class Maze:
    def __init__(self, width: int, height: int, seed : int):
        self.width = width
        self.height = height
        self.seed = seed
        self.matrix = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(MazeCell(i, j))
            self.matrix.append(row)
        self.layout = np.zeros(shape=(2, 1), dtype=np.uint8)

    def getCell(self, x : int, y : int):
        return self.matrix[x][y]

    # transforma din matrice de MatriCell -> in matrice obisnuita de numere de tip uint8
    def _computeFinalMatrix(self):
        m = np.zeros(shape=(2 * self.height + 1, 2 * self.width + 1), dtype=np.uint8)
        for i in range(self.height):
            for j in range(self.width):
                cell : MazeCell = self.matrix[i][j]
                m[i * 2 + 1][j * 2 + 1] = cell.value  # Setăm valoarea celulei curente

                m[i * 2 + 1][j * 2 + 2] += cell.E  # Dreapta
                m[i * 2 + 1][j * 2] += cell.W      # Stânga
                m[i * 2][j * 2 + 1] += cell.N      # Sus
                m[i * 2 + 2][j * 2 + 1] += cell.S  # Jos

        # Aplicăm transformarea doar pe celulele care nu reprezintă intrarea (64) și ieșirea (182)
        m = np.where((m != 64) & (m != 182), (m > 0) * 255, m)
        
        # Eliminăm marginile suplimentare din matricea finală
        m = np.delete(m, [0, -1], axis=1)
        return np.delete(m, [0, -1], axis=0)
        
    
    def write_maze_to_file(self, file_name: str):
        cv2.imwrite(file_name, self._computeFinalMatrix())
    
    def write_to_output(self):
        print(self._computeFinalMatrix())

    def save_layout_maze(self):
        self.layout = np.array(self._computeFinalMatrix(), dtype=np.uint8)
    
    # agentul este in pozitia (x, y), functia returneaza o matrice cu o parte din
    # labirint, adica field_size elemente in jurul lui
    def get_field_of_view(self, x : int, y : int, field_size):
        height, width = self.layout.shape
        output = np.zeros(shape=(2 * field_size + 1, 2 * field_size + 1), dtype=np.uint8)
        output_x_start_idx = 0 if (x - field_size >= 0) else field_size - x
        output_y_start_idx = 0 if (y - field_size >= 0) else field_size - y
        output_x_end_idx = 2 * field_size + 1 if (x + field_size <= height - 1) else 2 * field_size + 1 - (x + field_size +1 - height) 
        output_y_end_idx = 2 * field_size + 1 if (y + field_size <= width - 1) else 2 * field_size + 1  - (y + field_size + 1 - width)
        for i in range(output_x_start_idx, output_x_end_idx):
            for j in range(output_y_start_idx, output_y_end_idx):
                    output[i][j] = self.layout[x - field_size + i][y - field_size + j]
        return output


    # vreau sa generez un start si un end point in labirint
    # The minimum rectangular path from the entrance to the exit
    # must cover at least 50% of the total rectangular area of the maze.

    def generate_start_end_points(self):
        height = self.height
        width = self.width

        # Calculăm aria minimă necesară (50% din aria totală)
        min_area_coverage = 0.5 * height * width

        while True:
            # Generăm aleator coordonatele pentru start și end
            start_x, start_y = np.random.randint(0, height), np.random.randint(0, width)
            end_x, end_y = np.random.randint(0, height), np.random.randint(0, width)

            # Calculăm aria dreptunghiului dintre cele două puncte
            rect_area = abs(end_x - start_x + 1) * abs(end_y - start_y + 1)

            # Verificăm dacă aria acoperă cel puțin 50% din aria totală a labirintului
            if rect_area >= min_area_coverage:
                # Setăm valoarea pentru intrare și ieșire
                self.matrix[start_x][start_y].value = Constants.ENTRANCE
                self.matrix[end_x][end_y].value = Constants.EXIT
                break  # Ieșim din buclă dacă am găsit un start și end corespunzător
    
    def valid_postion(self, x : int, y : int):
        if (x < 0 or x > self.height - 1):
            return False
        if (y < 0 or y > self.width - 1):
            return False
        return self.layout[x][y] != Constants.WALL
    
    def adapt_agent_postion(self, x : int , y : int, command : str):
        if (command == "N"):
            if (self.valid_postion(x - 1, y)):
                return x - 1, y, Constants.SUCCESS
        if (command == "S"):
            if (self.valid_postion(x + 1, y)):
                return  x + 1, y, Constants.SUCCESS
        if (command == "W"):
            if (self.valid_postion(x, y - 1)):
                return x, y - 1, Constants.SUCCESS
        if (command == "E"):
            if (self.valid_postion(x, y + 1)):
                return x, y + 1, Constants.SUCCESS        
        return x, y, Constants.FAIL