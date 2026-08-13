try:
    # Código que pode gerar uma exceção
    numero = 100/0
    print(numero)
except Exception as e:
    # Código que trata a exceção
    print(f"Ocorreu um erro: {e}")