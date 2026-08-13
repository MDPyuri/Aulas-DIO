import sqlite3
from tabulate import tabulate #

conexao = sqlite3.connect("dados.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()

linhas = [dict(linha) for linha in dados]

print(tabulate(linhas, headers="keys", tablefmt="grid"))