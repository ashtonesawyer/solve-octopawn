import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import octopawn as octo

def test_noMoves():
	b = octo.Board("....p..pP.pP..P.W")
	assert b.moves() == []

def test_oneMove():
	b = octo.Board("....p...P.pp..P.W")
	assert b.moves() == [((3, 2), (2, 3))]

def test_twoMoves():
	b = octo.Board("p....P..........W")
	assert b.moves() == [((1, 1), (0, 1)), ((1, 1), (0, 0))]
