#Lê o arquivo CSV criado
import csv

with open("pokemons.csv", "r") as file:
  read = csv.reader(file)

  for line in read:
    print(line)