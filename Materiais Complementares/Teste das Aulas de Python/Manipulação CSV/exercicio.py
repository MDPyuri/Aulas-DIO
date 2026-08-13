# Crie um arquivo chamado pokemons.csv com os dados (nome, tipo, estágio).
# Escreva um programa em Python que:
  # Abra o arquivo usando open()
  # Leia linha por linha
  # Exiba as características de uma única linha de forma personalizada.

import csv

pokemon = input("Qual pokémon você gostaria de conhecer?")

with open("pokemons.csv", "r") as file:
  read = csv.reader(file)

  for line in read:
    if line[0].strip().casefold() == pokemon:
      print(f"{line[0]} is a {line[1]} type pokemon on stage level {line[2]}.")
      break
  else:
    print("Pokémon não cadastrado :/")