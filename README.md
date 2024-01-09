# Solving Octopawn
Ashton Sawyer

## Rules
Octopawn is a variation on [Hexapawn](https://en.wikipedia.org/wiki/Hexapawn) with 
4 pawns on each side of a 4x4
board. The pawns move as they do in chess: they may only move forward one square (even on their
first turn) unless they are moving diagonally to capture. A player wins by having their pawn
move to the other end of the board, or by leaving no legal moves for their opponent. 

## Description
I repurposed my negamax code from [Fourtic](https://github.com/ashtonesawyer/fourtic/tree/main)
in order to solve this. It runs quickly and seems to
be generating the move table accuarately, given that it has the correct amount of states and
shows a first-player win. 

The table showing all possible states is stored in `4pawn.json`

### Format
Each state is stored as a flattened representation of the board where `.` is a blank space,
`P` is a white pawn, `p` is a black pawn, and a final letter (either B or W) represents whose 
turn it is.


## Use
```
	python3 octopawn.py
```

## Tests
Automated tests were written for pytest
