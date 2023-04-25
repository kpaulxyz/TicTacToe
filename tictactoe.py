# first two player tictactoe then one player against ai
# Ich hab jetzt einfach mal ohne OOP(bzw MVC/MVP) angefangen.
# Ich denke es ist einfacher es erst so zu machen und dann einzuteilen.


field = [[" ", "|", " ", "|", " "],
         ["—", "+", "—", "+", "—"],
         [" ", "|", " ", "|", " "],
         ["—", "+", "—", "+", "—"],
         [" ", "|", " ", "|", " "]]


def printer():  # function that prints the field

    print("  0   1   2", end="\n")
    for j in range(0, len(field)):
        print("0" if j == 0 else "1" if j == 2 else "2" if j == 4 else " ", end=" ")
        for k in range(0, len(field)):
            print(str(field[j][k]), end=" ")
        print("\n", end="")


def turn():  # function that checks whoose turn it is and where they can place their symbol
    print("penis")


player1_char = "X"
player2_char = "O"

print("Willkommen zu Kat&Paul's TicTacToe:")

printer()


# ssh push test