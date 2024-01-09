import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import octopawn as octo

def test_valid():
	b = octo.Board(".P.P....pppppP..B")
	
	board = [[".", "P", ".", "P"],
			 [".", ".", ".", "."],
			 ["p", "p", "p", "p"],
			 ["p", "P", ".", "."]]

	assert b.board == board
	assert b.player == "B"	
