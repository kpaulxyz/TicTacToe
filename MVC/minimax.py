import tictactoe
import random


class Minimax:

    def minimax(self, current_field, is_maximizing, player1_char, player2_char):
        checkwin = self.check_win(current_field, player1_char, player2_char)
        if checkwin == (1, 1):  # Draw
            return 0, 0, 0
        if checkwin == (1, 0):  # Player wins
            return -1, 0, 0
        if checkwin == (0, 1):  # AI wins
            return 1, 0, 0

        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = None

        for j in range(0, len(current_field), 2):
            for k in range(0, len(current_field), 2):
                if current_field[j][k] == " ":
                    current_field[j][k] = player1_char if not is_maximizing else player2_char
                    score = self.minimax(current_field, not is_maximizing, player1_char, player2_char)[0]
                    current_field[j][k] = " "

                    if is_maximizing and score > best_score:
                        best_score = score
                        best_move = j, k
                    elif not is_maximizing and score < best_score:
                        best_score = score
                        best_move = j, k

        if best_score == 0 and best_move == (0, 0):  # is None:
            empty_cells = [(j, k) for j in range(0, len(current_field), 2) for k in range(0, len(current_field), 2) if
                           current_field[j][k] == " "]
            random.seed()
            random_move = random.choice(empty_cells)
            return 0, random_move[0], random_move[1]
        else:
            if best_move is None:
                return 0, -1, -1  # No available moves
            else:
                # print('The next best move is:', best_move, "score: ", best_score)
                return best_score, best_move[1], best_move[0]

    def check_win(self, ifield, player1_char, player2_char):
        # nothing 0, 0; draw 1, 1; win player1 1, 0; win player2 0, 1
        for j in range(0, len(ifield), 2):
            if ifield[j][0] == ifield[j][2] == ifield[j][4] == player1_char:
                return 1, 0
            elif ifield[j][0] == ifield[j][2] == ifield[j][4] == player2_char:
                return 0, 1
            elif ifield[0][j] == ifield[2][j] == ifield[4][j] == player1_char:
                return 1, 0
            elif ifield[0][j] == ifield[2][j] == ifield[4][j] == player2_char:
                return 0, 1

        if ifield[0][0] == ifield[2][2] == ifield[4][4] == player1_char:
            return 1, 0
        elif ifield[0][0] == ifield[2][2] == ifield[4][4] == player2_char:
            return 0, 1
        elif ifield[0][4] == ifield[2][2] == ifield[4][0] == player1_char:
            return 1, 0
        elif ifield[0][4] == ifield[2][2] == ifield[4][0] == player2_char:
            return 0, 1
        elif all(ifield[j][k] != " " for j in range(len(ifield)) for k in range(len(ifield))):
            return 1, 1
        else:
            return 0, 0
