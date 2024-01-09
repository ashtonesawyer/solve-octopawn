import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import octopawn as octo

def test_exBoard():
	b = octo.Board("PPPP........ppppW")

	board = [[".", ".", "p", "."],
			 ["p", ".", ".", "P"],
			 [".", ".", "p", "."],
			 ["P", "P", ".", "."]]

	b.board = board
	assert b.stringify() == "..p.p..P..p.PP..W"

def test_rand():
	b = octo.Board("PPPP........ppppW")

	board = [[".", ".", "p", "."],
			 ["p", "p", ".", "P"],
			 [".", ".", ".", "."],
			 ["P", "P", ".", "."]]

	b.board = board
	b.player = "B"
	assert b.stringify() == "..p.pp.P....PP..B"
