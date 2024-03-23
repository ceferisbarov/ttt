import json
import requests
import http.client

def get_board(gameId):
	conn = http.client.HTTPSConnection("www.notexponential.com")
	payload = ''
	headers = {
	'x-api-key': '09837de54294dd255c02',
	'userId': '3624'
	}

	conn.request("GET", f"/aip2pgaming/api/index.php?type=boardString&gameId={gameId}", payload, headers)
	res = conn.getresponse()
	data = res.read().decode("utf-8")
	data = json.loads(data)

	matrix = data["output"].split("\n")
	matrix = [list(row) for row in matrix]

	return matrix

def make_move(gameId, teamId, playerId, move):
	url = "https://www.notexponential.com/aip2pgaming/api/index.php"

	payload = {'type': 'move',
	'gameId': gameId,
	'move': move,
	'teamId': teamId}
	files=[

	]
	headers = {
	'Content-Type': 'application/x-www-form-urlencoded',
	'x-api-key': '09837de54294dd255c02',
	'userId': playerId,
	'User-Agent': 'PostmanRuntime/7.37.0'
	}

	response = requests.request("POST", url, headers=headers, data=payload, files=files)

	return response.text

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
