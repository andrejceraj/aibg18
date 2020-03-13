from random import randint


class Bot:
    def __init__(self):
        pass

    def get_move(self, table):
        pass


class RandomBot(Bot):
    def get_move(self, table):
        move = randint(0, 6)
        while table[0][move] != 0:
            move = randint(0, 6)
        return move
