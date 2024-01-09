#!/usr/bin/python3

import json

ttable = {}

class Board(object):
	def __init__(self, board):
		self.player = "X"
		self.board = self.setup(board)
		assert(self.player == "W" or self.player == "B")
		return

	def stringify(self):
		"""Turn 2d board into string + first player"""
		s = ""
		for row in self.board:
			for space in row:
				s += space
		s += self.player

		assert(len(s) == 17)
		return s

	def setup(self, s):
		"""Turn board's string representation into 2d array + first player"""
		assert(len(s) == 17)
		board = []
		for i in range(4):
			row = []
			for j in range(4):
				row += [s[4*i+j]]
			board += [row]

		self.player = s[-1]
		return board

	def moves(self):
		"""
		Get all possible moves for a given position

		:return: ((start_i, start_j), (end_i, end_j))
		"""
		moves = []
		for i in range(4):
			for j in range(4):
				if self.player == "W":
					if self.board[i][j] == "P":
						# can't move side-side or backwards
						if i == 0:
							continue
						if self.board[i-1][j] == ".":
							moves += [((i, j), (i-1, j))]
						if j < 3 and self.board[i-1][j+1] == "p":
							moves += [((i, j), (i-1, j+1))]
						if j > 0 and self.board[i-1][j-1] == "p":
							moves += [((i, j), (i-1, j-1))]
				else:
					if self.board[i][j] == "p":
						# can't move side-side or backwards
						if i == 4:
							continue
						if self.board[i+1][j] == ".":
							moves += [((i, j), (i+1, j))]
						if j < 3 and self.board[i+1][j+1] == "P":
							moves += [((i, j), (i+1, j+1))]
						if j > 0 and self.board[i+1][j-1] == "P":
							moves += [((i, j), (i+1, j-1))]
		return moves

	def won(self, player):
		"""Check if there's a pawn in winning rank"""
		for j in range(4):
			if player == "W":
				if self.board[0][j] == "P":
					return True
			else:
				if self.board[3][j] == "p":
					return True

	def move(self, move):
		"""Move pawn + update player"""
		((i,j), (k,l)) = move
		self.board[i][j] = "."
		self.board[k][l] = "P" if self.player == "W" else "p"

		self.player = "W" if self.player == "B" else "B"

	def negamax(self, player):
		"""Run full negamax with transposition table"""
		state = self.stringify()
		if state in ttable:
			return ttable[state]

		# need to check if opponent won bc "self.player" changes after move
		# and before check
		if self.won("W" if self.player == "B" else "B"):
			ttable[state] = -1
			return -1

		moves = self.moves()

		# if you have no moves, opponent wins
		if not moves:
			ttable[state] = -1
			return -1

		score = float("-inf")
		for move in moves:
			b = Board(state)
			b.move(move)
			s = b.negamax(b.player)
			if -s > score:
				score = -s

		ttable[state] = score	
		return score

	
def solve():
	print("Starting...")

	start = Board("pppp........PPPPW") #initial board state
	start.negamax("W")

	# save ttable to file
	jsonObj = json.dumps(ttable, indent=2)
	with open("4pawn.json", "w") as out:
		out.write(jsonObj)

	print("Finished Solving.")
	print("View results in 4pawn.json")
	print("Exiting...")
	print()
	print()

if __name__ == '__main__':
	solve()
