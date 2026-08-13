#Cria o arquivo csv com base na lista "data"
import csv

data = [
  ["name", "type", "stage"],
  ["Bulbasaur", "Grass", "1"],
  ["Ivysaur", "Grass", "2"],
  ["Venusaur", "Grass", "3"],
  ["Charmander", "Fire", "1"],
  ["Charmeleon", "Fire", "2"],
  ["Charizard", "Fire", "3"],
  ["Squirtle", "Water", "1"],
  ["Wartortle", "Water", "2"],
  ["Blastoise", "Water", "3"],
  ["Pikachu", "Electric", "1"],
  ["Raichu", "Electric", "2"]
]

with open("pokemons.csv", "w", newline="") as file:
  writer = csv.writer(file)
  writer.writerows(data)