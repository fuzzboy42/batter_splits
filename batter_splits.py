import requests
req = requests.get('http://api.sportradar.us/mlb/trial/v6.5/en/seasons/2017/REG/standings.json?api_key=yn8ctwj7h8nssg3tdyagskfe')
#print(req.json())

data = req.json()
list_of_teams = []
#print(leagues)
for league in data['league']['season']['leagues']:
	for division in league['divisions']:
		for team in division['teams']:
			#print(team)
			list_of_teams.append(team)

print('List of teams: {0}'.format(list_of_teams))