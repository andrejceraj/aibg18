from bot.bots import RandomBot
from rules.game_end import *


class Game:
    def __init__(self, players):
        self.rows = 6
        self.cols = 7

        self.turn = 0
        self.moves = []
        self.current_turn = (0, 0)

        self.table = []
        for i in range(self.rows):
            self.table.append([0] * self.cols)

        self.players = players

    def check_game_end(self):
        if self.table[self.current_turn[0]][self.current_turn[1]] == 0:
            return False

        if check_vertical(self.table, self.current_turn):
            return 1
        elif check_horizontal(self.table, self.current_turn):
            return 1
        elif check_diagonal(self.table, self.current_turn):
            return 1
        elif is_table_filled(self.table):
            return -1
        return 0

    def run(self):
        game_ended = self.check_game_end()
        while not game_ended:
            move = self.players[self.turn % 2].get_move(self.table)
            self.moves.append(move)
            self.current_turn = self.insert_move(move)
            self.turn += 1
            game_ended = self.check_game_end()

            self.print_board()

        if game_ended == 1:
            return self.turn % 2
        else:
            return -1

    def insert_move(self, move):
        curr_row = self.rows - 1
        while self.table[curr_row][move] != 0:
            curr_row -= 1
        self.table[curr_row][move] = self.turn % 2 + 1
        current_turn = (curr_row, move)
        return current_turn

    def print_board(self):
        print("\nPlayer " + str(self.turn % 2 + 1) + " played move " + str(self.current_turn[1]))
        print("-" * 30)
        for i in range(self.rows):
            for j in range(self.cols):
                print(" | " + str(self.table[i][j]), end='')
            print(" |")
        print("-" * 30)
        for i in range(7):
            print(" | " + str(i), end="")
        print(" |\n" + "-" * 30 + "\n")


def main():
    p1 = RandomBot()
    p2 = RandomBot()
    game = Game([p1, p2])
    winner = game.run()
    if winner != -1:
        print("Winner is player " + str(winner + 1))
    else:
        print("The game ended in a draw")


if __name__ == '__main__':
    main()