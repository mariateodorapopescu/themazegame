import unittest
import numpy as np
from agent import Agent
from constants import Constants

class TestAgent(unittest.TestCase):

    def setUp(self):
        """Configurează o instanță a agentului pentru testare."""
        self.agent = Agent(view_range=2)  
        
    def test_choose_direction(self):
        """Testează logica de alegere a direcției."""
        # Creaza un camp de vedere cu diferite ziduri
        fov = np.array([
            [Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.PATH, Constants.PATH, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.PATH, Constants.WALL, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.PATH, Constants.PATH, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL],
        ])
        # Pozitia unde se afla agentul
        # Agentul se afla la (1, 1), care este un PATH
        # Verifică dacă direcția aleasă este validă (S, N, E)
        # Agentul poate merge spre Sud, Nord sau Est
        x, y = 1, 1  
        direction = self.agent._chooseDirection(x, y, fov)
        self.assertIn(direction, ["S", "N", "E"])  

    def test_modify_coordinates(self):
        """Testează logica de modificare a coordonatelor."""
        x, y = 2, 2  # Coordonațiile inițiale
        new_x, new_y = self.agent._modifyCoordinates(x, y, "N")
        # Verifică că mutarea spre Nord scade x cu 1
        self.assertEqual((new_x, new_y), (1, 2))  
        new_x, new_y = self.agent._modifyCoordinates(x, y, "S")
        # Verifică că mutarea spre Sud crește x cu 1
        self.assertEqual((new_x, new_y), (3, 2))  
        new_x, new_y = self.agent._modifyCoordinates(x, y, "W")
        # Verifică că mutarea spre Vest scade y cu 1
        self.assertEqual((new_x, new_y), (2, 1))  
        new_x, new_y = self.agent._modifyCoordinates(x, y, "E")
        # Verifică că mutarea spre Est crește y cu 1
        self.assertEqual((new_x, new_y), (2, 3))  

    def test_create_traveling_plan(self):
        """Testează logica de creare a planului de călătorie."""
        fov = np.array([
            [Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.PATH, Constants.PATH, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.PATH, Constants.PATH, Constants.PATH, Constants.WALL],
            [Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL],
        ])
        plan = self.agent._createTravelingPlan(fov)
        self.assertTrue(isinstance(plan, str))  
        # Verifica daca lungimea planului nu depaseste numărul de miscari permise
        self.assertLessEqual(len(plan), self.agent.movements)  

    def test_create_request(self):
        """Testează metoda de creare a cererii."""
        fov = np.array([
            [Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.PATH, Constants.PATH, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.PATH, Constants.PATH, Constants.WALL, Constants.WALL],
            [Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL, Constants.WALL],
        ])
        request = self.agent.create_request(fov)
        # Verifica daca cererea este în format bytes
        self.assertTrue(isinstance(request, bytes)) 

if __name__ == '__main__':
    unittest.main()

#python -m unittest discover