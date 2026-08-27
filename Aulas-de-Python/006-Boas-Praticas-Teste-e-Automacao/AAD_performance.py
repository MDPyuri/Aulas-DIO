# Loop tradicional
soma = 0
for i in range(1_000_000):
    soma += i

# Mais rápido: função interna
soma = sum(range(1_000_000))