#Cria o arquivo JSON com base na lista "data"
import json

data = [
  {
    "name": "Bulbasaur",
    "type": "Grass",
    "stage": 1
  },
  {
    "name": "Ivysaur",
    "type": "Grass",
    "stage": 2
  },
  {
    "name": "Venusaur",
    "type": "Grass",
    "stage": 3
  },
  {
    "name": "Charmander",
    "type": "Fire",
    "stage": 1
  },
  {
    "name": "Charmeleon",
    "type": "Fire",
    "stage": 2
  },
  {
    "name": "Charizard",
    "type": "Fire",
    "stage": 3
  }
]

with open("pokemons.json", "w") as file:
  json.dump(data, file, indent=2)