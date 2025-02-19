# tests/test_game.py

import unittest
from longest_word.game import Game # import the Game class

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = Game() # setup
        grid = game.grid # exercise

        # verify if the grid is a list of 9 elements
        self.assertIsInstance(grid, list) # gird must be a list
        self.assertEqual(len(grid), 9) # grid must have 9 elements
        for letter in grid:
            self.assertTrue(letter.isalpha())  # Ensure it's a letter
            self.assertTrue(letter.isupper())  # Ensure it's uppercase

        # Teardown is not needed here because there are no resources to release or cleanup actions to perform after the test.
    def test_is_valid(self):
        game = Game()
        game.grid = ['B', 'A', 'R', 'O', 'Q', 'U', 'E', 'X', 'Y']
        self.assertTrue(game.is_valid('BAROQUE'))
        self.assertFalse(game.is_valid('BAROQUES'))

if __name__ == '__main__':
    unittest.main()
