import requests

URL = 'https://pokeapi.co/api/v2/pokemon/ditto'
r = requests.get(URL)
dados = r.json()
print(type(dados))
print(dados.keys())