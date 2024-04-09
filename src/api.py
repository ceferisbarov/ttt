import json
import requests
import http.client

def get_board(gameId, playerId, apikey):
	conn = http.client.HTTPSConnection("www.notexponential.com")
	payload = ''
	headers = {
	'x-api-key': apikey,
	'userId': playerId
	}

	conn.request("GET", f"/aip2pgaming/api/index.php?type=boardString&gameId={gameId}", payload, headers)
	res = conn.getresponse()
	data = res.read().decode("utf-8")
	data = json.loads(data)
	matrix = string_to_matrix(data["output"])
	# matrix = data["output"].split("\n")
	# matrix = [list(row) for row in matrix]

	return matrix

def make_move(gameId, teamId, playerId, apikey, move):
	url = "https://www.notexponential.com/aip2pgaming/api/index.php"

	payload = {'type': 'move',
	'gameId': gameId,
	'move': move,
	'teamId': teamId}
	files=[

	]
	headers = {
	'Content-Type': 'application/x-www-form-urlencoded',
	'x-api-key': apikey,
	'userId': playerId,
	'User-Agent': 'PostmanRuntime/7.37.0'
	}

	response = requests.request("POST", url, headers=headers, data=payload, files=files)

	return response

def get_moves(gameId):
	url = f"https://www.notexponential.com/aip2pgaming/api/index.php?type=moves&gameId={gameId}&count=1"

	payload = {}
	headers = {
	'x-api-key': '09837de54294dd255c02',
	'userId': '3624',
    'User-Agent': 'PostmanRuntime/7.37.0'
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	return json.loads(response.text)


def string_to_matrix(matrix_string):
    rows = matrix_string.strip().split('\n')
    matrix = []
    for row in rows:
        matrix.append([0 if c == '-' else 1 if c == 'O' else -1 for c in row])
    return matrix

def get_game_details(gameId, userId, apikey):
	url = f"https://www.notexponential.com/aip2pgaming/api/index.php?type=gameDetails&gameId={gameId}"

	payload = {}
	headers = {
		'x-api-key': apikey,
		'userId': userId,
		'User-Agent': 'PostmanRuntime/7.37.0'
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	details = json.loads(response.text)

	details = json.loads(details["game"])
	print(details)
	return int(details["boardsize"]), int(details["target"])
