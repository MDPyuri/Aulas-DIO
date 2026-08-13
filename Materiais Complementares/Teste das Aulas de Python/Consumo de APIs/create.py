import json
import requests

url = "https://pokeapi.co/api/v2/pokemon/decidueye"
response = requests.get(url)

# O corpo da resposta já é JSON, então usamos .json()
data = response.json()

with open("decidueye.json", "w") as file:
    json.dump(data, file, indent=2)
