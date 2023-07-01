import os.path
import random
import printer
import playerhandler
import model
import minimax


class Tictactoe:
    printer = None
    playerhandler = None
    minimax = None
    model = None
    def __init__(self):
        self.printer = printer.Printer()
        self.playerhandler = playerhandler.Playerhandler()
        self.minimax = minimax.Minimax()
        self.model = model.Model()

    def turn(self):  # function that checks whose turn it is and where they can place their symbol
        self.printer.printfield(self.model.field)
        if self.playerhandler.ai and not self.playerhandler.player1:
            self.printer.aicalc()
            best_move = self.minimax.minimax(self.model.field, not self.playerhandler.player1, self.playerhandler.player1_char, self.playerhandler.player2_char)
            self.printer.aimoved(best_move)
            self.model.do_move(best_move[1]//2, best_move[2]//2, self.playerhandler.player1, self.playerhandler.player1_char,
                               self.playerhandler.player2_char)
            # self.printer.printfield(self.model.field)


        else:
            while True:
                nextmove = self.printer.playermove(self.playerhandler.player1, self.playerhandler.player1_char,
                                                   self.playerhandler.player2_char)
                next_move_x, next_move_y = nextmove
                # return self.model.check_move(next_move_x, next_move_y, True)

                if self.model.check_move(next_move_x, next_move_y, True):
                    self.model.do_move(next_move_x, next_move_y, self.playerhandler.player1, self.playerhandler.player1_char, self.playerhandler.player2_char)
                    break
                    # self.playerhandler.player1 = not self.playerhandler.player1
                else:
                    self.printer.occupied()
                    self.printer.printfield(self.model.field)

        win = self.check_win(self.model.field, self.playerhandler.player1_char, self.playerhandler.player2_char)
        if win == (0, 0):
            self.model.savetosavestate()
            self.playerhandler.player1 = not self.playerhandler.player1
            self.turn()
        elif win == (1, 1):
            self.model.deletesavestate()
        elif win == (1, 0):
            self.model.deletesavestate()
        elif win == (0, 1):
            self.model.deletesavestate()
        self.printer.endmessage(win[0], win[1], self.playerhandler.ai)
        self.turn()


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

    # verbose = True

    def main(self):
        inp = None
        self.printer.welcomemessage()
        if self.model.checksavestate():
            inp = self.printer.checksavestate()
            while True:
                if inp == "n":
                    break

                if inp == "y":
                    self.model.loadsavestate()# self.tictactoe.checksavestateplayer()
                    spacecount = 0
                    for j in range(0, len(self.model.field)):
                        for k in range(0, len(self.model.field)):
                            if self.model.field[j][k] == " ":
                                spacecount += 1
                    if spacecount % 2 == 0:
                        self.playerhandler.player1 = False
                    break
        # self.printer.checkai()


        # inp = self.printer.invalidsavestate()

        # inp = self.printer.checkai()
        while True:
            checkai = self.printer.checkai()
            if checkai == 1:
                self.playerhandler.ai = True
                break
            elif checkai == 2:
                break
            elif checkai == 3:
                self.printer.invalidai()

        # printer.printfield(self.model.field)
        self.printer.startsplaying(self.playerhandler.player1, self.playerhandler.player1_char,
                                   self.playerhandler.player2_char)
        self.turn()
