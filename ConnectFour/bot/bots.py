from random import randint


chars = ["O", "X"]


class Bot(object):

	def __init__(self, name, player_id):

		self.name = str(name)
		self.id = str(chars[player_id])
		self.id_val = player_id

	def __str__(self):

		return "Player: " + self.name + ", ID: " + self.id

	def get_player_move(self):

		move = randint(0, 6) + 1
		print(self.name + " je odigrao " + str(move))
		return move


class RandomBot(Bot):
	pass
