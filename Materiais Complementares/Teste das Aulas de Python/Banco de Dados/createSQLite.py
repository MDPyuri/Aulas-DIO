import sqlite3

# Conexão com o banco de dados (ou criação do banco se não existir)
connection = sqlite3.connect("dados.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Commit das alterações e fechamento da conexão
connection.commit()

