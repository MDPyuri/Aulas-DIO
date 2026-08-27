# Noções de Boas Práticas, Teste e Automação em Python
> Por motivos de regras de modulação, nesta sessão de estudos estarei mudando minha regra de nomeclatura de arquivos para não iniciarem com números e sim com letras. Portanto segue o novo padrão utilizado "XXX_arquivo.py"

## Clean Code
Clean Code significa escrever código de forma **clara**, **simples** e **fácil** de entender.
A ideia é que qualquer pessoa (inclusive você no futuro) consiga ler e manter o código sem esforço.  
Os princípios básicos incluem:
- **Legibilidade**: nomes de variáveis e funções descritivos.
- **Simplicidade**: evitar complexidade desnecessária.
- **Organização**: funções pequenas e bem definidas.
- **Consistência**: seguir padrões e boas práticas.

### Exemplo sem clean code
```python
def f(x):
    r = 0
    for i in x:
        r += i
    return r / len(x)
# Aqui não fica claro o que a função faz. O nome f não diz nada, e r é vago.
```
> Vide [AAA_cleanCode.py](./AAA_cleanCode.py)

### Exemplo com clean code
```python
def calcular_media(lista_numeros):
    soma = sum(lista_numeros)
    quantidade = len(lista_numeros)
    return soma / quantidade
# Agora está explícito: a função calcula a média de uma lista de números.
# Os nomes (calcular_media, soma, quantidade) tornam o código autoexplicativo.
```
> Vide [AAA_cleanCode.py](./AAA_cleanCode.py)

## organização e Modularização
A organização de projetos em Python é essencial para manter o código **limpo**, **reutilizável** e **escalável**. Projetos desorganizados tendem a dificultar a manutenção e a colaboração entre desenvolvedores. A modularização é a prática de dividir o código em módulos e pacotes, cada um com responsabilidades específicas.  

### Benefícios da modularização
- **Reutilização**: módulos podem ser usados em diferentes partes do projeto ou em outros projetos.
- **Manutenção** facilitada: localizar e corrigir erros se torna mais simples.
- **Escalabilidade**: novos recursos podem ser adicionados sem comprometer a estrutura existente.
- **Colaboração**: equipes podem trabalhar em diferentes módulos sem conflitos.

### Boas práticas
- **Separar código de aplicação** (lógica de negócio) de código de configuração.
- **Criar pacotes** para funcionalidades relacionadas.
- Usar **nomes claros** e consistentes para arquivos e pastas.
- **Documentar** cada módulo com docstrings e comentários relevantes.
- Adotar **padrões** como PEP8 para estilo e PEP20 (Zen of Python) para filosofia.

### Exemplo de Disposição de Diretórios em um Projeto Python Genérico
```txt
📂 meu_projeto/  
├── 📄 README.md  
│   → Documentação inicial do projeto, instruções de uso e instalação.  
│  
├── 📄 requirements.txt  
│   → Lista de dependências necessárias para rodar o projeto.  
│  
├── 📄 setup.py  
│   → Script de configuração para empacotar e distribuir o projeto.  
│  
├── 📂 src/  
│   ├── 📂 meu_pacote/  
│   │   ├── 📄 __init__.py  
│   │   │   → Torna a pasta um pacote Python.  
│   │   ├── 📄 main.py  
│   │   │   → Ponto de entrada principal da aplicação.  
│   │   ├── 📄 utils.py  
│   │   │   → Funções auxiliares e utilitárias.  
│   │   ├── 📄 models.py  
│   │   │   → Definição de classes e estruturas de dados.  
│   │   └── 📄 config.py  
│   │       → Configurações e constantes do projeto.  
│   │  
│   └── 📂 submodulo/  
│       ├── 📄 __init__.py  
│       └── 📄 funcionalidades.py  
│           → Implementação de funcionalidades específicas.  
│  
├── 📂 tests/  
│   ├── 📄 test_main.py  
│   │   → Testes para o módulo principal.  
│   └── 📄 test_utils.py  
│       → Testes para funções auxiliares.  
│  
├── 📂 docs/  
│   └── 📄 manual.md  
│       → Documentação detalhada do projeto.  
│  
├── 📂 data/  
│   └── 📄 exemplo.csv  
│       → Arquivos de dados usados pelo projeto.  
│  
└── 📂 scripts/  
    └── 📄 run.sh  
        → Scripts auxiliares para execução ou automação.  
```
## Testagem
O processo de testagem em projetos Python tem como objetivo **verificar** se o software funciona corretamente, **evitar** regressões e **garantir** a **qualidade** do código. A prática consiste em criar testes automatizados que são executados sempre que novas funcionalidades são adicionadas ou modificadas.

### Principais tipos de teste
- **Teste Unitário**: verifica pequenas partes isoladas do sistema, como funções ou métodos. É o tipo mais rápido e mais utilizado.
- **Teste de Integração**: valida a comunicação entre diferentes componentes, como uma API e um banco de dados.
- **Teste Funcional** (ou End-to-End): simula o comportamento do usuário e avalia o sistema completo em funcionamento.
- **Teste de Regressão**: garante que alterações recentes não tenham quebrado funcionalidades que já funcionavam anteriormente.
  
### Ferramentas comuns no ecossistema Python
| Ferramenta |	Finalidade |
| -- | -- |
| unittest | Framework de testes incluído na biblioteca padrão do Python. |
| pytest |	Framework moderno e popular, com sintaxe simples e muitos recursos extras. |
| coverage.py |	Mede a cobertura de testes, indicando quais partes do código foram executadas pelos testes. |
| mock (unittest.mock) |	Permite simular dependências externas, como APIs e bancos de dados. |
| tox |	Executa testes em diferentes versões do Python e ambientes. |

### Fluxo típico
1. Desenvolver uma funcionalidade.
2. Criar testes para validar seu comportamento.
3. Executar os testes localmente.
4. Utilizar ferramentas de integração contínua (CI/CD), como GitHub Actions, para executar os testes automaticamente a cada alteração no código.
5. Corrigir falhas identificadas antes da publicação da aplicação.

> Uma boa estratégia de testes aumenta a confiabilidade do projeto, facilita a manutenção e reduz a ocorrência de erros em produção.

### Exemplo de uso do `pytest`
> É necessário instalar o Pytest `pip install pytest`

```python
def somar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b
```
>Vide [AAB_calculadora.py](./AAB_calculadora.py)

```python
import pytest
from AAB_calculadora import somar, dividir


def test_somar():
    assert somar(2, 3) == 5


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)


@pytest.mark.parametrize(
    "a,b,resultado",
    [
        (1, 1, 2),
        (2, 3, 5),
        (-1, 1, 0),
        (10, 5, 15),
    ]
)
def test_somar_varios_casos(a, b, resultado):
    assert somar(a, b) == resultado
```
>Vide [AAB_calculadora_test.py](./AAB_calculadora_test.py)

## Refatoração
Trata-se de melhorar o código existente sem alterar seu comportamento externo. O objetivo é torná-lo mais legível, eficiente e fácil de manter.

### Benefícios
- **Legibilidade**: código mais claro e fácil de entender por outros desenvolvedores.
- **Manutenibilidade**: facilita correções e evoluções futuras.
- **Redução de duplicação**: elimina trechos repetidos, aplicando princípios como DRY (Don't Repeat Yourself).
- **Performance**: em alguns casos, pode otimizar a execução.
- **Preparação para testes**: código mais modular e organizado facilita a criação de testes automatizados.

### Técnicas comuns
- **Extração de métodos**: transformar blocos de código em funções menores e reutilizáveis.
- **Renomeação de variáveis/métodos**: dar nomes mais claros e significativos.
- **Substituição de números mágicos**: usar constantes nomeadas em vez de valores soltos.
- **Divisão de classes**: separar responsabilidades para evitar classes muito grandes (God Classes).
- **Introdução de interfaces**: melhorar a flexibilidade e reduzir acoplamento.

Muitos desenvolvedores veem a refatoração como uma forma de "higiene do código": não muda o que o programa faz, mas muda como ele está escrito, tornando o futuro mais sustentável.

## Performance e Eficiência
Em Python, performance e eficiência são temas importantes porque a linguagem privilegia legibilidade e produtividade, mas nem sempre é a mais rápida em termos de execução. Ainda assim, há várias estratégias para otimizar código sem perder clareza.

### Estratégias para melhorar performance
- **Estruturas de dados adequadas**
  - Use `set` para buscas rápidas em vez de listas.
  - Prefira `dict` para mapeamentos em vez de listas de pares.
- **Bibliotecas otimizadas**
  - `numpy` e `pandas` são implementados em C e oferecem operações vetorizadas muito mais rápidas que loops puros em Python.
  - `multiprocessing` e `concurrent.futures` ajudam a paralelizar tarefas.
- **Evitar loops desnecessários**
  - Substituir loops por comprehensions ou funções internas (sum, max, any, all) que são otimizadas.
- **Uso de geradores**
  - Em vez de listas grandes, use `yield` ou expressões geradoras para economizar memória.
- **Profiling e medição**
  - Ferramentas como `cProfile` e `timeit` ajudam a identificar gargalos reais antes de otimizar.

### Exemplos Práticos
```Python
# Ineficiente: busca em lista
lista = [1, 2, 3, 4, 5]
print(100 in lista)  # O(n)

# Mais eficiente: busca em set
conjunto = {1, 2, 3, 4, 5}
print(100 in conjunto)  # O(1)

```
>Vide [AAC_performance](./AAC_performance.py)

```Python
# Loop tradicional
soma = 0
for i in range(1_000_000):
    soma += i

# Mais rápido: função interna
soma = sum(range(1_000_000))

```
> Vide [AAD_performance](./AAD_performance.py)

## Profiling
É o processo de analisar o desempenho do seu código para descobrir onde estão os gargalos — quais funções consomem mais tempo ou memória. Isso é crucial porque muitas vezes o problema não está onde imaginamos.

### Ferramentas principais
- `cProfile`
  - Integrado ao Python, mostra estatísticas detalhadas sobre chamadas de funções.
  - Exemplo:
  ```Python
    import cProfile

    def funcao_lenta():
      total = 0
      for i in range(10**6):
        total += i
      return total

    cProfile.run("funcao_lenta()")
  ```
  > Vide [AAE_profiling](./AAE_profiling.py) <br>
  > Saída: lista de funções chamadas, número de chamadas e tempo gasto em cada uma.
  
- `pstats`
  - Permite manipular os resultados do cProfile para ordenar e filtrar.
  - Exemplo:
  ```Python
  import pstats
  p = pstats.Stats("saida.prof")
  p.sort_stats("time").print_stats(10)  # Top 10 funções mais lentas
  ```
- `timeit`
  - Ideal para medir pequenos trechos de código.
  - Exemplo:
  ```Python
  import timeit
  print(timeit.timeit("sum(range(1000))", number=10000))
  ```
> Sempre combine profiling com refatoração: primeiro descubra o gargalo, depois otimize. Muitas vezes, trocar uma estrutura de dados ou usar uma biblioteca otimizada resolve mais do que mexer em microdetalhes.