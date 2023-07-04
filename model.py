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
                return False
        else:
            return True

