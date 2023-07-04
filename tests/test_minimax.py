import unittest
from minimax import Minimax

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

if __name__ == '__main__':
    unittest.main()
