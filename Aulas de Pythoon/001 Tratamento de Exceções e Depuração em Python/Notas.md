# Tratamento de Exceções e Depuração em Python
> Em Python, os erros são chamados de exceções. 

Quando ocorre um erro, o Python gera uma **exceção** que interrompe a execução do programa, a menos que seja tratada adequadamente. O tratamento de exceções permite que você lide com erros de forma **controlada**, evitando que o programa falhe inesperadamente.

## Exemplos de Exceções
- `ZeroDivisionError`: Ocorre quando há uma divisão por zero.
- `TypeError`: Ocorre quando há um tipo de dado incompatível em uma operação.
- `ValueError`: Ocorre quando uma função recebe um argumento do tipo correto, mas com um valor inadequado.
- `FileNotFoundError`: Ocorre quando um arquivo não é encontrado.

## Tipagem de Exceções
> Em Python, as exceções são organizadas em uma hierarquia de classes. A classe base para todas as exceções é a `BaseException`, e a maioria das exceções derivam da classe `Exception`. Isso permite que você capture exceções **específicas** ou **genéricas**, dependendo da necessidade do seu programa.

| Tipo de Exceção | Quando ocorre |
| --- | --- |
| ``ZeroDivisionError`` | Divisão por zero → ``10 ``/ ``0`` |
| ``NameError`` | Variável não definida → ``print(x)`` sem declarar ``x`` |
| ``TypeError`` | Operação com tipos incompatíveis → ``"2" ``+ ``2`` |
| ``ValueError`` | Valor inválido para operação → ``int("abc")`` |
| ``IndexError`` | Índice fora da lista → ``[1,2,3][10]`` |
| ``KeyError`` | Chave inexistente em dicionário → ``{"a":1}["b"]`` |
| ``FileNotFoundError`` | Arquivo não encontrado → ``open("nao_existe.txt")`` |
| ``AttributeError`` | Objeto sem atributo chamado → ``"texto".metodo_inexistente()`` |
| ``RecursionError`` | Recursão infinita sem condição de parada |

## Tratamento de Exceções
### Bloco try-except
O tratamento de exceções em Python é feito utilizando os blocos `try` e `except`. O código que pode gerar uma exceção é colocado dentro do bloco `try`, e o código que trata a exceção é colocado dentro do bloco `except`.

Esse código permite que o programa continue a execução mesmo após a ocorrência de um erro, fornecendo uma mensagem de erro amigável ao usuário.

```python
try:
    # Código que pode gerar uma exceção
    numero = 100/0
    print(numero)
except Exception as e:
    # Código que trata a exceção
    print(f"Ocorreu um erro: {e}")
```
>Vide ``001_Tratamento.py``

### Bloco finally
O bloco `finally` é opcional e é executado **independentemente** de uma exceção ter ocorrido ou não. Ele é útil para liberar recursos, como arquivos ou conexões de banco de dados, garantindo que certas ações sejam realizadas mesmo que ocorra um erro.

```python
try:
    # Código que pode gerar uma exceção
    numero = 100/0
    print(numero)
except Exception as e:
    # Código que trata a exceção
    print(f"Ocorreu um erro: {e}")
finally:
    # Código que será executado independentemente de uma exceção ter ocorrido ou não
    print("Execução do bloco finally")
```
>vide ``002_Tratamento.py``

### Comando raise
O comando `raise` é usado para **lançar** uma exceção manualmente. Ele pode ser útil para sinalizar que ocorreu uma condição de erro específica em seu código, permitindo que você crie suas próprias exceções personalizadas.

```python
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
```
>Vide ``003_Tratamento.py``

## Depuração em Python
A depuração é o processo de identificar e corrigir erros em um programa. Python oferece várias ferramentas para depuração, incluindo o módulo `pdb`, que permite executar o código passo a passo, inspecionar variáveis e controlar o fluxo de execução.

### Print Debugging
Uma técnica simples de depuração é usar declarações `print()` para exibir o valor de variáveis em diferentes pontos do programa. Isso ajuda a entender o fluxo de execução e identificar onde os erros podem estar ocorrendo.

```python
numeros = 10
divisor = 0
print(f"Tentando dividir {numeros} por {divisor}")
resultado = numeros / divisor  # Isso causará um ZeroDivisionError
print(f"Resultado: {resultado}")
```
>Vide ``004_Debugging.py``

### Stack Trace
Quando uma exceção ocorre, o Python gera um **stack trace**, que é uma mensagem detalhada mostrando a sequência de chamadas de função que levaram ao erro. O stack trace inclui informações sobre o tipo de exceção, a linha de código onde ocorreu e o caminho do arquivo. Analisar o stack trace é uma habilidade importante para depuração eficaz.

```python
1.Traceback (most recent call last):
2.  File "c:\Users\Yuri\Documents\Aulas-DIO\Aulas de Pythoon\001 Tratamento de Exceções e Depuração em Python\004_Debugging.py", line 4, in <module>
3.    resultado = numeros / divisor  # Isso causará um ZeroDivisionError
4.                ~~~~~~~~^~~~~~~~~
5.ZeroDivisionError: division by zero
```
>Neste exemplo:  
>a linha 1 indica que é um stack trace,   
>a linha 2 mostra o arquivo e a linha onde ocorreu o erro,   
>a linha 3 mostra a operação que causou o erro,  
>e a linha 5 indica o tipo de exceção (`ZeroDivisionError`) e uma breve descrição do erro.  

### Depurando com o módulo `pdb`
O módulo `pdb` é o depurador interativo do Python. Ele permite que você execute o código passo a passo, inspecione variáveis e controle o fluxo de execução. Para usar o `pdb`, você pode inserir ``import pdb; pdb.set_trace()`` no seu código:

```python
#Para continuar a execução do código, você pode usar o comando (continue) no prompt do pdb
import pdb

def soma(a, b):
    pdb.set_trace()  # Pausa a execução aqui
    return a + b

resultado = soma(3, 5)
print("Resultado:", resultado)
```
>Vide ``005_Debugging.py``  

Alguns comandos úteis do `pdb` incluem:
- `n` (next): Executa a próxima linha de código.
- `c` (continue): Continua a execução até o próximo ponto de interrupção.

### Logs e Monitoramento
Além da depuração interativa, é uma boa prática adicionar **logs** ao seu código para registrar informações importantes sobre a execução do programa. O módulo `logging` do Python permite criar logs com diferentes níveis de severidade (DEBUG, INFO, WARNING, ERROR, CRITICAL). Isso ajuda a monitorar o comportamento do programa em produção e facilita a identificação de problemas.

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Este é um log de informação")
logging.warning("Este é um log de aviso")
logging.error("Este é um log de erro")
```
>Vide ``006_Debugging.py``

|Nível de Log|Uso|
|-------------|-----|
|DEBUG        | Informações detalhadas para depuração |
|INFO         | Informações gerais sobre a execução do programa |
|WARNING      | Avisos sobre situações que podem não ser problemas imediatos |
|ERROR        | Erros que ocorrem durante a execução do programa |
|CRITICAL     | Erros graves que podem causar falhas no programa |
>Os logs são vantagensos porque permitem que você registre informações importantes sobre a execução do programa sem interromper o fluxo normal de execução, ao contrário das mensagens de depuração que podem ser exibidas no console.

## Prevenção de Erros
Além de tratar exceções e depurar o código, é importante adotar práticas que ajudem a **prevenir erros** antes que eles ocorram. Algumas estratégias incluem:
- **Validação de Entrada**: Verifique se os dados fornecidos pelo usuário ou por outras fontes são válidos antes de processá-los.
  
    Um exemplo simples de validação de entrada é verificar se um número fornecido pelo usuário é positivo antes de realizar uma operação que requer números positivos:
  
    ```python
    numero = float(input("Digite um número positivo: "))
    if numero < 0:
        print("Erro: O número deve ser positivo.")
    else:
        print(f"A raiz quadrada de {numero} é {numero ** 0.5}")
    ```

- **Testes Automatizados**: Escreva testes unitários e de integração para garantir que seu código funcione conforme o esperado.
  
    Um exemplo de teste unitário usando o módulo `unittest` do Python:
  
    ```python
    import unittest

    def soma(a, b):
        return a + b

    class TestSoma(unittest.TestCase):
        def test_soma(self):
            self.assertEqual(soma(2, 3), 5)
            self.assertEqual(soma(-1, 1), 0)

    if __name__ == '__main__':
        unittest.main()
    ```
    >Vide ``007_Prevention.py``  

  
- **Boas Práticas de Codificação**: Siga convenções de codificação, escreva código limpo e documentado, e use ferramentas de análise estática para identificar problemas potenciais.
- **Revisão de Código**: Faça revisões de código com colegas para identificar possíveis erros e melhorar a qualidade do código.

