import argparse
from api import get_board, make_move, get_moves, get_game_details
from misc import pprint, decide_move
from minimax import minimax
from board import Board
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--game", help="Game ID.")
parser.add_argument("--team", help="Team ID.")
parser.add_argument("--player", help="A player ID from the team.")
parser.add_argument("--apikey", help="The player's API Key.")
parser.add_argument("--first", action="store_true", help="Make the first move.")

args = parser.parse_args()
team = args.team
player = args.player
gameId = args.game
apikey = args.apikey


size, target =get_game_details(gameId, player, apikey)
b = Board(size,target)

if args.first:
	b.board = get_board(gameId, player, apikey)
	pprint(b.board)
	print("****************************************************")
	move = minimax(b, 2, True)[1]
	move = str(move[0]) + "," + str(move[1])
	print(make_move(gameId, team, player, apikey, move))

while True:
	moves = get_moves(gameId)

	if moves["code"] == "OK" and moves["moves"][-1]["teamId"] != team:
		b.board = np.array(get_board(gameId, player, apikey))
		if 0 not in b.board:
			print("The game is over!")
			break
		pprint(b.board)
		print("****************************************************")
		move = minimax(b, 2, True)[1]
		move = str(move[0]) + "," + str(move[1])

		response = make_move(gameId, team, player, apikey, move)

	else:
		continue
