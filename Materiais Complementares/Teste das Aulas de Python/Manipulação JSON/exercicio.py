# Crie um arquivo chamado pokemons.json com os dados (nome, tipo, estágio).
# Escreva um programa em Python que:
  # Abra o arquivo usando open()
  # Leia linha por linha
  # Exiba as características de uma única linha de forma personalizada.
import json

pokemon = input("Qual pokémon você gostaria de conhecer?").strip().casefold()

with open("pokemons.json", "r") as file:
  data = json.load(file)

  for item in data:
    name = item["name"].strip().casefold()
    if name == pokemon:
      print(f"{item['name']} is a {item['type']} type pokemon on stage level {item['stage']}.")
      break
  else:
    print("Pokémon não cadastrado :/")