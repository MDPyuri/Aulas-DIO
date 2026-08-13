import requests

# Consultando dados de determinado pokémon
url = "https://pokeapi.co/api/v2/pokemon/decidueye"
response = requests.get(url)

print(response.status_code)
test = response.json()

if response.status_code == 200:
    data = response.json()
    print("Nome:", data["name"])
    print("Altura:", data["height"])
    print("Peso:", data["weight"])
    print("Tipos:", [t["type"]["name"] for t in data["types"]])
else:
    print("Erro na requisição:", response.status_code)
