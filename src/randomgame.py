import argparse
import random
from api import get_board, make_move, get_moves
from misc import pprint

parser = argparse.ArgumentParser()
parser.add_argument("--game", help="Game ID.")
parser.add_argument("--team1", help="Team 1 ID.")
parser.add_argument("--player1", help="A playr ID from team 1.")
parser.add_argument("--team2", help="Team 2 ID.")
parser.add_argument("--player2", help="A player ID from team 2.")

args = parser.parse_args()
team1, player1 = args.team1, args.player1
team2, player2 = args.team2, args.player2

gameId = args.game
if gameId is None:
	# Start a game
	pass

while True:
	moves = get_moves(gameId)
	matrix = get_board(gameId)
	pprint(matrix)
	print("****************************************************")

	if moves["code"] == "OK" and moves["moves"][-1]["teamId"] == team1:
		x = random.choice(range(len(matrix)))
		y = random.choice(range(len(matrix)))
		move = f"{x},{y}"

		make_move(gameId, team1, player1, move)
