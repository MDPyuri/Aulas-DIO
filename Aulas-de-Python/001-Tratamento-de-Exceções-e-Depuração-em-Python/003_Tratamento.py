def dividir(a, b):
    if b == 0:
        # Lança uma exceção personalizada
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

try:
    resultado = dividir(10, 0)
    print("Resultado:", resultado)
except ValueError as e:
    print("Erro capturado:", e)
