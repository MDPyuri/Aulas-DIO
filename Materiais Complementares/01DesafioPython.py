# Desafio
# Você faz parte da equipe de tecnologia de um grande banco e recebeu uma missão importante: ajudar o setor financeiro a organizar rapidamente os lançamentos diários de despesas e receitas. Cada lançamento é registrado como uma string contendo o tipo (D para despesa, R para receita) seguido do valor em reais, separados por espaço. Sua tarefa é criar uma função que, ao receber uma lista desses lançamentos em uma única linha, calcule o saldo final do dia. O saldo é a soma de todas as receitas menos a soma de todas as despesas. O resultado deve ser apresentado com duas casas decimais, mesmo que o valor seja inteiro. Não utilize bibliotecas externas.

# Implemente uma função que leia uma linha contendo lançamentos separados por vírgula, processe cada um conforme o tipo e valor, e imprima o saldo final do dia no formato especificado. Considere que todos os valores são números positivos e que pode haver tanto receitas quanto despesas, ou apenas um dos tipos.

# Entrada
# Uma única linha contendo lançamentos separados por vírgula. Cada lançamento é composto por uma letra (D ou R), seguida de um espaço e um valor decimal positivo.

# Saída
# Uma única linha contendo o saldo final do dia, com duas casas decimais.


#-----------------------------------------------------------------------------------------------------------------#

# Lê a linha de lançamentos do stdin
entrada = input().strip() 

# Inicialize o saldo do dia
saldo = 0.0

# Divide os lançamentos pela vírgula
lancamentos = entrada.split(',')

for lancamento in lancamentos:
    tipo, valor = lancamento.strip().split()
    valor = float(valor)
    # TODO: Atualize o saldo conforme o tipo de lançamento ('R' soma, 'D' subtrai)
    if tipo == 'R':
        saldo += valor
    elif tipo == 'D':
        saldo -= valor

# Imprima o saldo final com duas casas decimais
print(f"{saldo:.2f}")