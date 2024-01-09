import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json

with open('4pawn.json', "r") as f:
	ttable = json.load(f)

def test_len():
	assert len(ttable) == 20286
	print(len(ttable))

def test_ex1():
	assert ".........p.P....W" in ttable
	assert ttable[".........p.P....W"] == -1
	print(ttable[".........p.P....W"])

def test_ex2():
	assert ".........PpP....W" in ttable
	assert ttable[".........PpP....W"] == -1
	print(ttable[".........PpP....W"])

def test_ex3():
	assert ".........P.p....W" in ttable
	assert ttable[".........P.p....W"] == -1
	print(ttable[".........P.p....W"]) 

def test_ex4():
	assert "..........pp....W" in ttable
	assert ttable["..........pp....W"] == -1
	print(ttable["..........pp....W"]) 

def test_soln():
	assert "pppp........PPPPW" in ttable
	assert ttable["pppp........PPPPW"] == 1
	print(ttable["pppp........PPPPW"])

if __name__ == '__main__':
	test_len()
	test_ex1()
	test_ex2()
	test_ex3()
	test_ex4()
	test_soln()

