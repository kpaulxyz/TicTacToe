import os.path
import random

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
ai = False


# verbose = True

def printer():  # function that prints the field
    print("  0   1   2", end="\n")
    for j in range(0, len(field)):
        print("0" if j == 0 else "1" if j == 2 else "2" if j == 4 else " ", end=" ")
        for k in range(0, len(field)):
            print(str(field[j][k]), end=" ")
        print("\n", end="")


def turn():  # function that checks whose turn it is and where they can place their symbol
    if ai and not player1:
        print("Next move is being calculated...")
        best_move = minimax(field, not player1)
        print("AI moved to ", best_move[1], best_move[2])
        do_move(best_move[1], best_move[2])
        # check_move(best_move[0], best_move[1], False)
    else:
        while True:
            next_move_x = int(input(
                f"Player {1 if player1 else 2} ({player1_char if player1 else player2_char}), please choose the x ("
                f"horizontal) coordinates of your next move: "))
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

        return check_move(next_move_x, next_move_y, True)


def check_win(ifield):  # nothing 0, 0; draw 1, 1; win player1 1, 0; win player2 0, 1
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


def do_move(x, y):
    global player1
    field[y][x] = (player1_char if player1 else player2_char)
    printer()
    win = check_win(field)
    if win == (0, 0):
        f = open("savestate.py", "w")
        f.write("save = " + repr(field))
        f.close()
        player1 = not player1
        turn()
    elif win == (1, 1):
        print("It's a draw.")

    elif win == (1, 0):
        print("Player 1 won")
        if os.path.exists("savestate.py"):
            os.remove("savestate.py")
    elif win == (0, 1):
        print("Player 2 won")
        if os.path.exists("savestate.py"):
            os.remove("savestate.py")



def check_move(x, y, verbose):
    x = int(x * 2)
    y = int(y * 2)
    if not field[y][x] == " ":
        if verbose:
            print("Your given coordinates are already occupied. \nPlease Try again.\n")
        turn()
    else:
        do_move(x, y)


def minimax(current_field, is_maximizing):
    checkwin = check_win(current_field)
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
                score = minimax(current_field, not is_maximizing)[0]
                current_field[j][k] = " "

                if is_maximizing and score > best_score:
                    best_score = score
                    best_move = j, k
                elif not is_maximizing and score < best_score:
                    best_score = score
                    best_move = j, k

    if best_score == 0 and best_move == (0, 0): # is None:
        empty_cells = [(j, k) for j in range(0, len(current_field), 2) for k in range(0, len(current_field), 2) if
                       current_field[j][k] == " "]
        random.seed()
        random_move = random.choice(empty_cells)
        return 0, random_move[0], random_move[1]
    else:
        if best_move is None:
            return 0, -1, -1  # No available moves
        else:
            print('The next best move is:', best_move, "score: ", best_score)
            return best_score, best_move[1], best_move[0]


print("Welcome to Kat&Paul's TicTacToe:")

if os.path.isfile('./savestate.py'):
    inp = input("An older savestate has been found. Do you want to continue it? (y/n): ")

    while True:
        if inp == "n":
            break

        if inp == "y":
            field = save
            spacecount = 0
            for j in range(0, len(field)):
                for k in range(0, len(field)):
                    if field[j][k] == " ":
                        spacecount += 1
            if spacecount % 2 == 0:
                player1 = False
            break

        inp = input("That was not a valid input. Type y/n if you want to continue or not: ")

'''if input("Do you want to play against AI or local multiplayer? 1/2: ") == "1":
    ai = True'''
inp = input("Do you want to play against AI or local multiplayer? 1/2: ")
while True:
    if inp == "1":
        ai = True
        break
    elif inp == "2":
        break
    inp = input("That was not a valid input. Type 1/2 if you want to play against AI or local multiplayer: ")


printer()
print(f"Player {1 if player1 else 2} ({player1_char if player1 else player2_char}) will start playing.")
turn()

