import unittest
import numpy as np

from server.maze import Maze

class TestMazeFieldOfView(unittest.TestCase):
    
    def setUp(self):
        # Initialize a small test maze for easy visualization, 3x3 cells
        # This will result in a final matrix of 7x7 (each cell + walls)
        self.maze = Maze(3, 3, seed=42)
        self.maze.save_layout_maze()
    
    def test_centered_field_of_view(self):
        # Agent in center (1,1) of a 3x3 maze with a field size of 1 (5x5 view)
        view = self.maze.get_field_of_view(3, 3, field_size=1)
        self.assertEqual(view.shape, (3, 3), "Field of view should be 3x3.")
        # Assert that view is centered with layout of agent surroundings
    
    def test_field_of_view_at_border_top_left(self):
        # Top-left corner (0,0) with field size 1 (5x5 view should crop to 3x3 at borders)
        view = self.maze.get_field_of_view(0, 0, field_size=1)
        self.assertEqual(view.shape, (3, 3), "Field of view at top-left should be 3x3.")
    
    def test_field_of_view_at_border_bottom_right(self):
        # Bottom-right corner (2,2) with field size 1 (5x5 view should crop to 3x3 at borders)
        view = self.maze.get_field_of_view(6, 6, field_size=1)
        self.assertEqual(view.shape, (3, 3), "Field of view at bottom-right should be 3x3.")
    
    def test_variable_field_of_view_expansion(self):
        # Testing field of view expansion (X-RAY example, field size 2 for 7x7 view)
        view = self.maze.get_field_of_view(3, 3, field_size=2)
        self.assertEqual(view.shape, (5, 5), "Expanded field of view should be 5x5.")

    def test_variable_field_of_view_contraction(self):
        # Testing field of view contraction (Fog tile, field size 0 for 3x3 view)
        view = self.maze.get_field_of_view(3, 3, field_size=0)
        self.assertEqual(view.shape, (1, 1), "Contracted field of view should be 1x1.")

if __name__ == '__main__':
    unittest.main()
