import requests

URL = 'https://swapi.dev/api/people/1'
r = requests.get(URL)
dados = r.json()
print(dados.get('name'))