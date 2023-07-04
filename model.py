import os.path
if os.path.isfile("./savestate.py"):
    from savestate import save

class Model:
    field = None
    def __init__(self):
        self.field = [[" ", "|", " ", "|", " "],
                      ["—", "+", "—", "+", "—"],
                      [" ", "|", " ", "|", " "],
                      ["—", "+", "—", "+", "—"],
                      [" ", "|", " ", "|", " "]]



    def do_move(self, x, y, player1, player1_char, player2_char):
        self.field[y*2][x*2] = (player1_char if player1 else player2_char)
        # printer()
        # win = check_win(field)
        # if win == (0, 0):
        # savetosavestate
        """player1 = not player1
        turn() controller"""
        '''elif win == (1, 1):
        elif win == (1, 0):
        elif win == (0, 1):
            '''

    def loadsavestate(self):
        if os.path.isfile('./savestate.py'):
            from savestate import save
            self.field = save

    def checksavestate(self):
        if os.path.isfile('./savestate.py'):
            return True
        return False

    def savetosavestate(self):
                f = open("savestate.py", "w")
                f.write("save = " + repr(self.field))
                f.close()

    def deletesavestate(self):
        os.remove("savestate.py")


    def check_move(self, x, y, verbose):

        x = int(x * 2)
        y = int(y * 2)
        if not self.field[y][x] == " ":
            if verbose:
                # self.printer.occupied()
                return False
        else:
            return True
        # else:
        #    do_move(x, y)
