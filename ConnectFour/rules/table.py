EID = ""
TAB_SIZE = 14 # 6 for sublime


class Table(object):

	def __init__(self, row_size=6, col_size=7):

		self.row_size = row_size
		self.col_size = col_size
		self.moves = []

		self.table = list(list())
		self.init_table()

	def __str__(self):

		return self.view_table()

	def view_table(self):

		output = "|"

		for i in range(self.col_size):
			output += "|\t" + str(i + 1) + "\t|"
		output += "|\n"

		for i in reversed(range(self.row_size)):
			output += "-"* (((self.col_size + 1)*2)*self.col_size+2) + "\n"
			output += "|"

			for j in range(self.col_size):

				val = self.table[i][j] if not self.table[i][j] else self.table[i][j].id
				output += "|\t" + val + "\t|"
			output += "|\n"

		for i in range(self.col_size):
			output += "-"*(TAB_SIZE)
		output += "-"* (self.col_size + 1)*2 + "\n"

		return output

	def init_table(self):

		for i in range(self.row_size):
			self.table.append([])

		for i in range(self.row_size):
			for j in range(self.col_size):
				self.table[i].append(EID)

	# NOT USED
	def set_table(self, moves, players):

		for move in moves:
			self.insert(players[len(self.moves) % 2], move)
			check = self.check_win(move)
			
			if check:
				return check
		return False

	# NOT USED.. 
	def add_row(self):

		self.table.append([])

		self.row_size += 1

		for i in range(self.col_size):
			self.table[self.row_size - 1].append(EID)

	def insert(self, player, col):

		self.moves.append(col)

		for i in range(self.row_size):

			if not self.table[i][col]:
				self.table[i][col] = player
				return True

		return False

	def check_win(self, j):

		if len(self.moves) == self.row_size * self.col_size:
			return True

		for i in range(self.row_size):
			if not self.table[i][j]:
				return self.check_horizontal(i-1, j) or self.check_vertical(i-1, j) or self.check_vertical(i-1, j)

	def check_horizontal(self, i, j):

		W_limit = 0 if j < 3 else j - 3
		E_limit = self.col_size - 1 if j > 3 else j + 3

		cnt = 1
		val = self.table[i][j].id_val

		for k in reversed(range(W_limit, j)):
			if not self.table[i][k]:
				break

			if val == self.table[i][k].id_val:
				cnt += 1

		for k in range(j+1, E_limit):
			if not self.table[i][k]:
				break

			if val == self.table[i][k].id_val:
				cnt += 1

		return cnt >= 4

	def check_vertical(self, i, j):

		S_limit = 0 if i < 3 else i - 3

		cnt = 1
		val = self.table[i][j].id_val

		for k in reversed(range(S_limit, i)):
			if not self.table[k][j]:
				break
			if val == self.table[k][j].id_val:
				cnt += 1

		return cnt >= 4


	def check_diagonal(self, i, j):

		W_limit = 0 if j < 3 else j - 3
		E_limit = self.col_size - 1 if j > 3 else j + 4

		S_limit = 0 if i < 3 else i - 3

		lcnt = 1
		rcnt = 1

		val = self.table[i][j].id_val

		sw = True
		se = True
		nw = True
		ne = True

		for k in range(1, 4):

			w = j-k # > 0
			e = j+k # < col_size

			s = i-k # > 0
			n = i+k # < row_size

			if s >= 0:
				if w >= 0:
					if not self.table[s][w]:
						sw = False

					elif val == self.table[s][w].id_val and sw:
						lcnt += 1

				if e < self.col_size:
					if not self.table[s][e]:
						se = False
					elif val == self.table[s][e].id_val and se:
						rcnt += 1
					
			if n < self.row_size:
				if w >= 0:
					if not self.table[n][w]:
						nw = False

					elif val == self.table[n][w].id_val and nw:
						rcnt += 1

				if e < self.col_size:
					if not self.table[n][e]:
						ne = False
					elif val == self.table[n][e].id_val and ne:
						lcnt += 1

		return lcnt >= 4 or rcnt >= 4