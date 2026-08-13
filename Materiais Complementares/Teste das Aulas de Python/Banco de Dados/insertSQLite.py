import sqlite3

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute(
  "INSERT INTO usuarios (nome, idade) VALUES (?, ?)", 
  ("João", 25)
)
conexao.commit()