# Ineficiente: busca em lista
lista = [1, 2, 3, 4, 5]
print(100 in lista)  # O(n)

# Mais eficiente: busca em set
conjunto = {1, 2, 3, 4, 5}
print(100 in conjunto)  # O(1)