#Lê o arquivo pokemons.json
import json

with open("pokemons.json", "r") as file:
  data = json.load(file)

  for line in data:
    print(line)