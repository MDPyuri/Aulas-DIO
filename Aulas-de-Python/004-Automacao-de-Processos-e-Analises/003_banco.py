import sqlite3

con = sqlite3.connect("dados.db")

cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
nome TEXT,
idade INTEGER
)
""")

con.commit()

print("Tabela criada com sucesso\n")

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Maria", 30))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Ana", 25))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Carlos", 40))
con.commit()

cursor.execute("SELECT * FROM usuarios")

rows = cursor.fetchall()

for row in rows:
  print(row)

con.close()