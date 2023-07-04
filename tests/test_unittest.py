from model import Model
import os.path
from unittest.mock import Mock
import unittest
import tictactoe
from model import Model
from playerhandler import Playerhandler
from minimax import Minimax

from unittest.mock import patch


class MockModel:
    def check_move(self, x, y, verbose):
        return True

    def do_move(self, x, y, player1, player1_char, player2_char):
        pass


class MockPrinter:
    # Define mock methods here that mimic the behavior of the Printer class...
    def printfield(self, ifield):
        pass  # Mock methods do nothing

    def occupied(self):
        pass

    def aicalc(self):
        pass

    def aimoved(self, best_moev):
        pass

    def playermove(self, player1, player1_char, player2_char):
        next_move = (0, 1)
        return next_move


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = tictactoe.Tictactoe()
        self.printer = MockPrinter()
        self.model = MockModel()
    """
    def test_turn(self):

        # Test case 1: Player 1's turn, human player
        player1_char = "X"
        player2_char = "O"
        player1 = True
        ai = False
        win = (1, 0)
        field = [['O', '|', ' ', '|', 'X'],
                 ['—', '+', '—', '+', '—'],
                 [' ', '|', 'O', '|', 'X'],
                 ['—', '+', '—', '+', '—'],
                 ['O', '|', ' ', '|', ' ']]

        # Mock the playermove method to return the desired next move
        self.printer.playermove = lambda player, char1, char2: (1, 1)
        #self.game.turn()
        with patch('builtins.input', side_effect=['2', '2']):
            self.game.turn()
        self.assertEqual(field[4][4], player1_char)  # Player 1's move should be recorded

        '''
        # Test case 2: Player 2's turn, AI player
        self.playerhandler.player1 = False
        self.playerhandler.ai = True
        self.model.field = [[' ', '|', 'O', '|', 'X'],
                            ['—', '+', '—', '+', '—'],
                            ['O', '|', 'X', '|', 'X'],
                            ['—', '+', '—', '+', '—'],
                            ['O', '|', ' ', '|', ' ']]

        # Mock the aicalc method to return the desired best move
        self.printer.aicalc = lambda: None
        self.minimax.minimax = lambda field, player, char1, char2: (1, 0, 0)  # Mock the best move
        self.turn()
        self.assertEqual(self.model.field[0][1], self.playerhandler.player1_char)  # AI's move should be recorded
        '''
"""

    def test_check_win(self) -> None:
        player1_char = 'X'
        player2_char = 'O'

        # Testing player 1 win condition
        field = [["X", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 ["X", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 ["X", "|", " ", "|", " "]]

        result = self.game.check_win(field, player1_char, player2_char)
        self.assertEqual(result, (1, 0))

        # Testing player 2 win condition
        field = [["O", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 ["O", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 ["O", "|", " ", "|", " "]]

        result = self.game.check_win(field, player1_char, player2_char)
        self.assertEqual(result, (0, 1))

        # Testing draw condition
        field = [["X", "|", "O", "|", "X"],
                 ["—", "+", "—", "+", "—"],
                 ["X", "|", "O", "|", "O"],
                 ["—", "+", "—", "+", "—"],
                 ["O", "|", "X", "|", "X"]]

        result = self.game.check_win(field, player1_char, player2_char)
        self.assertEqual(result, (1, 1))

        # Testing no win condition
        field = [[" ", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 [" ", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 [" ", "|", " ", "|", " "]]

        result = self.game.check_win(field, player1_char, player2_char)
        self.assertEqual(result, (0, 0))


def test_play_game(self):
    expected_result = True
    # Call the method you want to test
    result = self.tictactoe.play_game()
    # Add assertions to check the result
    self.assertEqual(result, expected_result)


class TestMinimax(unittest.TestCase):
    def setUp(self):
        self.minimax = Minimax()  # Create an instance of your Minimax class

    def test_minimax(self):
        current_field = [["X", "|", " ", "|", " "],
                         ["—", "+", "—", "+", "—"],
                         [" ", "|", "X", "|", " "],
                         ["—", "+", "—", "+", "—"],
                         ["O", "|", "O", "|", " "]]  # Set the current field state
        player1_char = 'X'
        player2_char = 'O'

        score, x, y = self.minimax.minimax(current_field, True, "X", "O")  # Call the minimax method
        expected_score = 1  # Adjust the expected score based on the game rules and the field state
        expected_x = 4  # Adjust the expected x-coordinate of the best move
        expected_y = 4  # Adjust the expected y-coordinate of the best move

        self.assertEqual(score, expected_score)  # Check if the score matches the expected value
        self.assertEqual(x, expected_x)  # Check if the x-coordinate of the best move matches the expected value
        self.assertEqual(y, expected_y)  # Check if the y-coordinate of the best move matches the expected value

        current_field = [["X", "|", "O", "|", "X"],
                         ["—", "+", "—", "+", "—"],
                         [" ", "|", "O", "|", ""],
                         ["—", "+", "—", "+", "—"],
                         ["O", "|", " ", "|", "X"]]  # Set the current field state
        player1_char = 'X'
        player2_char = 'O'

        score, x, y = self.minimax.minimax(current_field, True, "X", "O")  # Call the minimax method
        expected_score = 1  # Adjust the expected score based on the game rules and the field state
        expected_x = 2  # Adjust the expected x-coordinate of the best move
        expected_y = 4  # Adjust the expected y-coordinate of the best move

        self.assertEqual(score, expected_score)  # Check if the score matches the expected value
        self.assertEqual(x, expected_x)  # Check if the x-coordinate of the best move matches the expected value
        self.assertEqual(y, expected_y)  # Check if the y-coordinate of the best move matches the expected value

    def test_check_win(self) -> None:
        player1_char = 'X'
        player2_char = 'O'

        # Testing player 1 win condition
        field = [["X", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 ["X", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 ["X", "|", " ", "|", " "]]

        result = self.minimax.check_win(field, player1_char, player2_char)
        self.assertEqual(result, (1, 0))

        # Testing player 2 win condition
        field = [["O", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 ["O", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 ["O", "|", " ", "|", " "]]

        result = self.minimax.check_win(field, player1_char, player2_char)
        self.assertEqual(result, (0, 1))

        # Testing draw condition
        field = [["X", "|", "O", "|", "X"],
                 ["—", "+", "—", "+", "—"],
                 ["X", "|", "O", "|", "O"],
                 ["—", "+", "—", "+", "—"],
                 ["O", "|", "X", "|", "X"]]

        result = self.minimax.check_win(field, player1_char, player2_char)
        self.assertEqual(result, (1, 1))

        # Testing no win condition
        field = [[" ", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 [" ", "|", " ", "|", " "],
                 ["—", "+", "—", "+", "—"],
                 [" ", "|", " ", "|", " "]]

        result = self.minimax.check_win(field, player1_char, player2_char)
        self.assertEqual(result, (0, 0))


class TestModel(unittest.TestCase):
    def setUp(self) -> None:
        # self.model = model.Model()
        self.field = [[" ", "|", " ", "|", " "],
                      ["—", "+", "—", "+", "—"],
                      [" ", "|", " ", "|", " "],
                      ["—", "+", "—", "+", "—"],
                      [" ", "|", " ", "|", " "]]
        self.field2 = [["X", "|", " ", "|", " "],
                       ["—", "+", "—", "+", "—"],
                       [" ", "|", " ", "|", " "],
                       ["—", "+", "—", "+", "—"],
                       [" ", "|", " ", "|", " "]]
        self.model = Model()  # Create an instance of your Model class

    def tearDown(self):
        if os.path.isfile('./savestate.py'):
            os.remove("savestate.py")  # Remove the savestate file if it exists

    def test_loadsavestate(self):
        f = open("savestate.py", "w")  # Create a savestate file
        f.write('save = [["X", "|", " ", "|", " "],'
                '["—", "+", "—", "+", "—"],'
                '[" ", "|", " ", "|", " "],'
                '["—", "+", "—", "+", "—"],'
                '[" ", "|", " ", "|", " "]]')
        f.close()

        self.model.loadsavestate()  # Call the loadsavestate method
        expected_field = [["X", "|", " ", "|", " "],
                          ["—", "+", "—", "+", "—"],
                          [" ", "|", " ", "|", " "],
                          ["—", "+", "—", "+", "—"],
                          [" ", "|", " ", "|", " "]]
        self.assertEqual(self.model.field, expected_field)  # Check if the field matches the expected state

    def test_checksavestate(self):
        self.assertFalse(self.model.checksavestate())  # Check if savestate does not exist

        f = open("savestate.py", "w")  # Create a savestate file
        f.write('save = [["X", "|", " ", "|", " "],'
                '["—", "+", "—", "+", "—"],'
                '[" ", "|", " ", "|", " "],'
                '["—", "+", "—", "+", "—"],'
                '[" ", "|", " ", "|", " "]]')
        f.close()

        self.assertTrue(self.model.checksavestate())  # Check if savestate exists

    def test_savetosavestate(self):
        self.model.field = [["X", "|", " ", "|", " "],
                            ["—", "+", "—", "+", "—"],
                            [" ", "|", " ", "|", " "],
                            ["—", "+", "—", "+", "—"],
                            [" ", "|", " ", "|", " "]]  # Set the field to a specific state

        self.model.savetosavestate()  # Call the savetosavestate method

        f = open("savestate.py", "r")  # Read the content of the savestate file
        content = f.read()
        f.close()

        expected_content = "save = [['X', '|', ' ', '|', ' ']," \
                           " ['—', '+', '—', '+', '—'], [' ', '|', ' ', '|', ' ']," \
                           " ['—', '+', '—', '+', '—'], [' ', '|', ' ', '|', ' ']]"
        self.assertEqual(content, expected_content)  # Check if the content matches the expected value

    def test_deletesavestate(self):
        f = open("savestate.py", "w")  # Create a savestate file
        f.close()

        self.model.deletesavestate()  # Call the deletesavestate method

        self.assertFalse(os.path.isfile('./savestate.py'))  # Check if the savestate file does not exist

    def test_check_move(self):
        model = Model()  # Create an instance of your Model class
        self.assertEqual(model.check_move(0, 0, True), True)

    def test_do_move(self):
        model = Model()  # Create an instance of your Model class
        model.do_move(0, 0, True, "X", "O")  # Call the do_move method
        expected_field = [["X", "|", " ", "|", " "],
                          ["—", "+", "—", "+", "—"],
                          [" ", "|", " ", "|", " "],
                          ["—", "+", "—", "+", "—"],
                          [" ", "|", " ", "|", " "]]
        self.assertEqual(model.field, expected_field)


if __name__ == '__main__':

    unittest.main()
    f = open("savestate.py", "r")  # Read the content of the savestate file
    f.write("save = [['X', '|', ' ', '|', ' '], "
            "['—', '+', '—', '+', '—'], [' ', '|', ' ', '|', ' '], "
            "['—', '+', '—', '+', '—'], [' ', '|', ' ', '|', ' ']]")
    f.close()
