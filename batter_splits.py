import requests
req = requests.get('http://api.sportradar.us/mlb/trial/v6.5/en/seasons/2018/REG/teams/aa34e0ed-f342-4ec6-b774-c79b47b60e2d/splits.json?api_key=yn8ctwj7h8nssg3tdyagskfe')
print(req.json())