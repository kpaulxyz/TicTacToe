import tictactoe
import random


class Minimax:

    def minimax(self, current_field, is_maximizing, player1_char, player2_char, alpha=float('-inf'),
                beta=float('inf')):
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
                    score = self.minimax(current_field, not is_maximizing, player1_char, player2_char, alpha, beta)[
                        0]
                    current_field[j][k] = " "

                    if is_maximizing and score > best_score:
                        best_score = score
                        best_move = j, k
                        alpha = max(alpha, best_score)
                        if alpha >= beta:
                            break
                    elif not is_maximizing and score < best_score:
                        best_score = score
                        best_move = j, k
                        beta = min(beta, best_score)
                        if alpha >= beta:
                            break

            if alpha >= beta:
                break

        if best_move is None:
            return 0, -1, -1  # No available moves
        else:
            return best_score, best_move[1], best_move[0]

    def check_win(self, ifield, player1_char, player2_char):
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
