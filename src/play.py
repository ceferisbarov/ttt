import argparse
from api import get_board, make_move, get_moves
from misc import pprint, decide_move

parser = argparse.ArgumentParser()
parser.add_argument("--game", help="Game ID.")
parser.add_argument("--team", help="Team ID.")
parser.add_argument("--player", help="A player ID from the team.")
parser.add_argument("--first", action="store_true", help="Make the first move.")

args = parser.parse_args()
team = args.team
player = args.player
gameId = args.game

if args.first:
	matrix = get_board(gameId)
	pprint(matrix)
	print("****************************************************")
	move = decide_move(matrix)
	print(make_move(gameId, team, player, move))

while True:
	moves = get_moves(gameId)

	if moves["code"] == "OK" and moves["moves"][-1]["teamId"] != team:
		matrix = get_board(gameId)
		pprint(matrix)
		print("****************************************************")
		move = decide_move(matrix)
		make_move(gameId, team, player, move)
