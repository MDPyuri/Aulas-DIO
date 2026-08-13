# Leitura da linha de identificadores de transações
entrada = input()

# TODO: Crie uma lista com as transações sem duplicatas, mantendo a ordem da primeira ocorrência

# Dica: Percorra cada transação e adicione à lista apenas se ainda não estiver presente

transacoes_unicas = []
for transacao in entrada.split():
    if transacao not in transacoes_unicas:
        transacoes_unicas.append(transacao)

print(' '.join(transacoes_unicas))  # Descomente após implementar a lógica