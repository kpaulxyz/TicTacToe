class Playerhandler:

    player1 = None  # bool that states which player is currently playing
    player1_char = None
    player2_char = None
    ai = None


    def __init__(self):
        self.player1 = True  # bool that states which player is currently playing
        self.player1_char = "X"
        self.player2_char = "O"
        self.ai = False
    '''
    def getPlayer(self):
        return'''