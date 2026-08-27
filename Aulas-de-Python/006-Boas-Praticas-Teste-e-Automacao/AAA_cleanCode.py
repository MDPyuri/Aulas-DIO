def f(x):
    r = 0
    for i in x:
        r += i
    return r / len(x)
# Aqui não fica claro o que a função faz. O nome f não diz nada, e r é vago.

def calcular_media(lista_numeros):
    soma = sum(lista_numeros)
    quantidade = len(lista_numeros)
    return soma / quantidade
# Agora está explícito: a função calcula a média de uma lista de números.
# Os nomes (calcular_media, soma, quantidade) tornam o código autoexplicativo.