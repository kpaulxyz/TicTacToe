from unittest.mock import Mock
import unittest
import tictactoe
from unittest.mock import patch


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
        # self.tictactoe = tictactoe.TicTacToe()
        # self.tictactoe.printer = MockPrinter()
        self.game = tictactoe.Tictactoe()
        self.game.printer = MockPrinter()

    @patch('builtins.input', side_effect=[0, 1])  # Mock user inputs 0 for x and 1 for y
    def test_turn(self, mock_input):
        # Initialize the field with empty spots
        self.game.ifield = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        player1 = True
        player1_char = "X"
        player2_char = "O"

        expected_result = (0, 1)
        #result = self.game.turn(player1, player1_char, player2_char)
        result = self.game.turn()

        self.assertEqual(result, expected_result)

    def test_check_win(self):
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


if __name__ == '__main__':
    unittest.main()
