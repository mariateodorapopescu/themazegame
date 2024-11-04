import unittest
import numpy as np

from server.maze import Maze

class TestMazeFieldOfView(unittest.TestCase):
    
    def setUp(self):
        # Initializează un labirint mic pentru teste ușor de vizualizat, 3x3 celule
        # Acest lucru va rezulta într-o matrice finală de 7x7 (fiecare celulă + pereți)
        self.maze = Maze(3, 3, seed=42)
        self.maze.save_layout_maze()  # Salvează configurația labirintului pentru a o folosi în teste
    
    def test_centered_field_of_view(self):
        # Agentul este poziționat în centru (1,1) al unui labirint 3x3 cu un field_size de 1 (vizualizare de 5x5)
        view = self.maze.get_field_of_view(3, 3, field_size=1)
        self.assertEqual(view.shape, (3, 3), "Field of view ar trebui să fie de 3x3.")
        # Verificăm că vizualizarea este centrată și include împrejurimile agentului
    
    def test_field_of_view_at_border_top_left(self):
        # Colțul de sus-stânga (0,0) cu field_size de 1 (vizualizarea 5x5 ar trebui să fie restricționată la 3x3 la margini)
        view = self.maze.get_field_of_view(0, 0, field_size=1)
        self.assertEqual(view.shape, (3, 3), "Field of view la marginea de sus-stânga ar trebui să fie 3x3.")
    
    def test_field_of_view_at_border_bottom_right(self):
        # Colțul de jos-dreapta (2,2) cu field_size de 1 (vizualizarea 5x5 ar trebui să fie restricționată la 3x3 la margini)
        view = self.maze.get_field_of_view(6, 6, field_size=1)
        self.assertEqual(view.shape, (3, 3), "Field of view la marginea de jos-dreapta ar trebui să fie 3x3.")
    
    def test_variable_field_of_view_expansion(self):
        # Testarea extinderii câmpului vizual (exemplu X-RAY, field_size de 2 pentru vizualizare de 7x7)
        view = self.maze.get_field_of_view(3, 3, field_size=2)
        self.assertEqual(view.shape, (5, 5), "Field of view extins ar trebui să fie 5x5.")

    def test_variable_field_of_view_contraction(self):
        # Testarea contracției câmpului vizual (exemplu de tile Fog, field_size de 0 pentru vizualizare de 3x3)
        view = self.maze.get_field_of_view(3, 3, field_size=0)
        self.assertEqual(view.shape, (1, 1), "Field of view contractat ar trebui să fie 1x1.")

if __name__ == '__main__':
    unittest.main()
