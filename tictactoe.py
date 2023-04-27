# first two player tictactoe then one player against ai
# Ich hab jetzt einfach mal ohne OOP(bzw MVC/MVP) angefangen.
# Ich denke es ist einfacher es erst so zu machen und dann einzuteilen.
import os.path
if os.path.isfile('./savestate.py'):
    from savestate import save


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
        if next_move_x in list(range(3)):
            break
        else:
            print("Please be sure to input a valid number (0-2). \nPlease try Again.")

    while True:
        next_move_y = int(input(
            f"Player {1 if player1 else 2}, please choose the y (vertical)   coordinates of your next move: "))
        if next_move_y in list(range(3)):
            break
        else:
            print("Please be sure to input a valid number (0-2). \nPlease try Again.")

    # it might be possible to compress the two above loops into one

    return check_move(next_move_x, next_move_y)


def check_win():
    # a
    for j in range(0, len(field), 2):
        if field[j][0] == field[j][2] == field[j][4] == (player1_char if player1 else player2_char):
            return True
        elif field[0][j] == field[2][j] == field[4][j] == (player1_char if player1 else player2_char):
            return True
    if field[0][0] == field[2][2] == field[4][4] == (player1_char if player1 else player2_char):
        return True
    elif field[0][4] == field[2][2] == field[4][0] == (player1_char if player1 else player2_char):
        return True
    else:
        return False


def do_move(x, y):
    global player1  # Tells do_move to look for the global var player1
    field[y][x] = (player1_char if player1 else player2_char)
    printer()
    if not check_win():
        f = open("savestate.py", "w")
        f.write("save = " + repr(field))
        f.close()
        player1 = not player1
        turn()
    else:
        print(f"Player {1 if player1 else 2} won")
        if os.path.exists("savestate.py"):
            os.remove("savestate.py")


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

if os.path.isfile('./savestate.py'):
    inp = None
    while inp != ("y" or "n"):
        inp = input("An older savestate has been found. Do you want to continue it? (y/n): ")
    if inp == "y":
        field = save
        '''try:
            field = save
        except SyntaxError:
            pass'''



printer()
print("Player 1 (X) will start playing.")
turn()
