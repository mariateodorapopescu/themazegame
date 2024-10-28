from maze import Maze, MazeCell
import sys
import os
# daca nu includ path-ul asa nu vede clasa Constants
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import Constants
import numpy as np

# https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10580178
# labirintul este generat prin intermediul unei parcurgeri DFS a intregii matrici de celule
# size : tuple -> size = (x, y)  x -> height si y -> width
class DFSGenerator:
    def __init__(self, size : tuple, seed : int, origin : tuple):
        self.maze = Maze(width=size[0], height=size[1], seed=seed)
        self.x = origin[0]
        self.y = origin[1]
        # vor fi stocate aici celule prin care a trecut, dar nu le-a explorat complet 
        self.queue = []
        # ce noduri au fost vizitate, nu are sens sa trecem prin ele de 2 ori
        self.visited = np.zeros(shape=(self.maze.height, self.maze.width)).astype(bool)


    # te afli intr-o anumita celula, te uiti in primul rand daca exista celula 
    # respectiva, (de exemplu daca se afla pe prima linie, nu exista nimic deasupra)
    # apoi se verifica daca celula respectiva a fost deja explorata, daca nu, aceasta
    # este adaugata in vector  
    def getUnvisitedCells(self, x : int, y: int):
        # parantezele va rog lasati-le, ca altfel se strica conditiile
        unvisited = []
        if (x != 0) and (not self.visited[x -1][y]):
            unvisited.append(self.maze.matrix[x - 1][y])

        if (y != 0) and (not self.visited[x][y - 1]):
            unvisited.append(self.maze.matrix[x][y - 1])
        
        if (x != (self.maze.height - 1)) and (not self.visited[x + 1][y]):
            unvisited.append(self.maze.matrix[x + 1][y])

        if (y != (self.maze.width - 1)) and (not self.visited[x][y + 1]) :
            unvisited.append(self.maze.matrix[x][y + 1])
        return unvisited
    

    # sa zicem ca sunt in vectorul cu posibile directii pe care poate 
    # merge agentul 3 variante, indicate de variabila number_cells,
    # x si y sunt pozitia curenta a agentului in labirint
    # se foloseste seed pentru a genera labirintul, este un simplu int,
    # care ajuta in formula de calcul a indexului urmatoarei celule care va fi aleasa   
    def chooseIndexRandom(self, x : int, y : int, number_cells : int):
        seed = self.maze.seed
        return (np.pow(seed, 2) + seed + np.pow(x, 2) + np.pow(y, 2)) % number_cells 
    
    def carve_maze(self):
        x = self.x
        y = self.y
        self.queue.append(self.maze.getCell(x, y))
        self.visited[x][y] = True
        self.maze.matrix[x][y].value = Constants.PATH  # are valoarea 255, 0 este pt zid
        while(self.queue.__len__() != 0):
            cell : MazeCell = self.queue[self.queue.__len__() - 1]
            surroundingCells = self.getUnvisitedCells(cell.x , cell.y)
            if surroundingCells.__len__() != 0:
                idx =  self.chooseIndexRandom(cell.x, cell.y, surroundingCells.__len__())
                new_cell : MazeCell = surroundingCells[idx]
                cell, new_cell = cell.breakWall(new_cell)
                self.queue.append(new_cell)
                self.visited[new_cell.x][new_cell.y] = True
                self.maze.matrix[new_cell.x][new_cell.y].value = Constants.PATH
            else :
                self.queue.pop()
        return self.maze
    


