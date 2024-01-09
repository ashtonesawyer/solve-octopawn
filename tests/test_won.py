import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import octopawn as octo

def test_wWin():
	b = octo.Board("..P.p...P.....P.B")
	assert b.won("W") == True
