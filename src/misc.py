import random

def pprint(matrix):
	for row in matrix:
		if len(row) == 0:
			continue
		for el in row:
			print(el, end=" ")
		print("\n")
	print()

def decide_move(matrix):
	x = random.choice(range(len(matrix)))
	y = random.choice(range(len(matrix)))
	move = f"{x},{y}"

	return move
