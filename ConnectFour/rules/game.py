import sys
import time

from rules.game import *
from bot.bot_factories import BotFactory
from rules.table import *


class Connect4(object):

	def __init__(self, players, row_size=6, col_size=7):

		self.players = players
		self.table = Table(row_size, col_size)

	def __str__(self):

		return "Game: Connect4\nPlayers: " + str(self.players[0]) + ", " + str(self.players[1])

	def start_game(self):

		turn = 0	
		print(self)
		
		while True:

			print(self.table)
			player = self.players[turn % 2]

			move = player.get_player_move(self.table) - 1
			self.table.insert(player, move)

			if self.table.check_win(move):
				break

			turn += 1

		print(self.table)
		print("Winner is " + str(self.players[turn % 2]))


def main(bot_type1, player_name1, bot_type2, player_name2):
	bot1 = BotFactory.create_bot(bot_type=bot_type1, player_name=player_name1, player_id=0)
	bot2 = BotFactory.create_bot(bot_type=bot_type2, player_name=player_name2, player_id=1)

	game = Connect4(players=[bot1, bot2])
	game.start_game()

if __name__ == '__main__':
	bot_type1, player_name1, bot_type2, player_name2 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
	main(bot_type1, player_name1, bot_type2, player_name2)
