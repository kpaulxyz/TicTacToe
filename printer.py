# Das hier ist die View

class Printer:
    def printfield(self, ifield):  # function that prints the field
        print("  0   1   2", end="\n")
        for j in range(0, len(ifield)):
            print("0" if j == 0 else "1" if j == 2 else "2" if j == 4 else " ", end=" ")
            for k in range(0, len(ifield)):
                print(str(ifield[j][k]), end=" ")
            print("\n", end="")


    def occupied(self):
        print("Your given coordinates are already occupied. \nPlease Try again.\n")

    def aicalc(self):
        print("Next move is being calculated...")

    def aimoved(self, best_move):
        print("AI moved to ", best_move[1] // 2, best_move[2] // 2)

    def playermove(self, player1, player1_char, player2_char):
        while True:
            next_move_x = int(input(f"Player {1 if player1 else 2} ({player1_char if player1 else player2_char}), "
                                    f"please choose the x (horizontal) coordinates of your next move: "))
            if next_move_x in list(range(3)):
                break
            else:
                print("Please be sure to input a valid number (0-2). \nPlease try Again.")

        while True:
            next_move_y = int(input(
                f"Player {1 if player1 else 2} ({player1_char if player1 else player2_char}), please choose the y ("
                f"vertical)   coordinates of your next move: "))
            if next_move_y in list(range(3)):
                break
            else:
                print("Please be sure to input a valid number (0-2). \nPlease try Again.")

        next_move = (next_move_x, next_move_y)
        return next_move

    def welcomemessage(self):
        print("Welcome to Kat&Paul's TicTacToe:")

    def checksavestate(self):
        return input("An older savestate has been found. Do you want to continue it? (y/n): ")

    def invalidsavestate(self):
        return input("That was not a valid input. Type y/n if you want to continue or not: ")

    def checkai(self):
        inp = input("Do you want to play against AI or local multiplayer? 1/2: ")


        while True:
            if inp == "1":
                return 1
                break
            elif inp == "2":
                return 2
                break
            return 3

    def invalidai(self):
        print("That was not a valid input. Please try again. ")
        # return 0
        # return input("That was not a valid input. Type 1/2 if you want to play against AI or local multiplayer: ")

    def startsplaying(self, player1, player1_char, player2_char):
        print(f"Player {1 if player1 else 2} ({player1_char if player1 else player2_char}) will start playing.")


    def endmessage(self,i, j, ai):
        if i == 1 and j == 1:
            print("Its a draw.")
        if i == 1 and j == 0:
            print("Player 1 won.")
        if i == 0 and j == 1 and ai:
            print("AI won.")
        if i == 0 and j == 1 and not ai:
            print("Player 2 won.")

