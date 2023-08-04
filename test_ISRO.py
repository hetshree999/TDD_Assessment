import unittest
from unittest.mock import patch
import ISRO

class TestClass(unittest.TestCase):
    def test_scenario(self):
        starting_position = (0,0,0)
        initial_direction = 'N'
        commands = ["f", "r", "u", "b", "l"]
        final_position, final_direction = ISRO.execute_commands(starting_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 1, -1))
        self.assertEqual(final_direction, 'W')

    def test_move_forward(self):
        starting_position = (0, 0, 0)
        initial_direction = 'N'
        commands = ["f", "f", "f"]
        final_position, final_direction = ISRO.execute_commands(starting_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 3, 0))
        self.assertEqual(final_direction, 'N')

    def test_turn_right(self):
        starting_position = (0, 0, 0)
        initial_direction = 'N'
        commands = ["r", "r", "r"]
        final_position, final_direction = ISRO.execute_commands(starting_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, 'W')

    def test_turn_up_and_down(self):
        starting_position = (0, 0, 0)
        initial_direction = 'N'
        commands = ["u", "d"]
        final_position, final_direction = ISRO.execute_commands(starting_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, 'U')    

if __name__ == '__main__':
    unittest.main()


