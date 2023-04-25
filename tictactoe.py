# first two player tictactoe then one player against ai
# Ich hab jetzt einfach mal ohne OOP(bzw MVC/MVP) angefangen.
# Ich denke es ist einfacher es erst so zu machen und dann einzuteilen.


field = [[" ", "|", " ", "|", " "],
         ["—", "+", "—", "+", "—"],
         [" ", "|", " ", "|", " "],
         ["—", "+", "—", "+", "—"],
         [" ", "|", " ", "|", " "]]

player1 = True  # bool that states which player is currently playing
player1_char = "X"
player2_char = "O"


def printer():  # function that prints the field

    print("  0   1   2", end="\n")
    for j in range(0, len(field)):
        print("0" if j == 0 else "1" if j == 2 else "2" if j == 4 else " ", end=" ")
        for k in range(0, len(field)):
            print(str(field[j][k]), end=" ")
        print("\n", end="")


def turn():  # function that checks whose turn it is and where they can place their symbol

    while True:
        next_move_x = int(input(
            f"Player {1 if player1 else 2}, please choose the x (horizontal) coordinates of your next move: "))
        if next_move_x in list(range(3)):  # TODO Implement check to see if move is legal
            break
        else:
            print("Please be sure to input a valid number (0-2). \nPlease try Again.")

    while True:
        next_move_y = int(input(
            f"Player {1 if player1 else 2}, please choose the y (vertical)   coordinates of your next move: "))
        if next_move_y in list(range(3)):  # TODO Implement check to see if move is legal
            break
        else:
            print("Please be sure to input a valid number (0-2). \nPlease try Again.")

    # it might be possible to compress the two above loops into one

    return check_move(next_move_x, next_move_y)


def do_move(x, y):
    global player1  # Tells do_move to look for the global var player1
    field[y][x] = (player1_char if player1 else player2_char)
    printer()
    # TODO implement win checker here
    player1 = not player1
    turn()


def check_move(x, y):
    # translate x and y coordinates to field coordinates
    x = int(x * 2)
    y = int(y * 2)
    if not field[y][x] == " ":
        print("Your given coordinates are already occupied. \nPlease Try again.\n")
        turn()
    else:
        do_move(x, y)


print("Willkommen zu Kat&Paul's TicTacToe:")
printer()
print("Player 1 (X) will start playing.")
turn()
