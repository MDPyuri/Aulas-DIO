# Automação de Processos e Análises
A automação de processos e análises é uma prática essencial para aumentar a eficiência e reduzir erros em tarefas repetitivas. No contexto de análise de dados, a automação permite que você execute fluxos de trabalho complexos com menos intervenção manual, economizando tempo e garantindo consistência nos resultados.

## Manipulação Automatizada de Arquivos
A manipulação automatizada de arquivos envolve a criação de scripts que podem ler, escrever e organizar arquivos de forma eficiente. Isso é particularmente útil quando você precisa lidar com grandes volumes de dados ou quando os dados são atualizados regularmente.
### Exemplo de Script para Manipulação de Arquivos
```python
import os

def listar_arquivos(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        print(arquivo)

def mover_arquivos(origem, destino):
    os.makedirs(destino, exist_ok=True)
    arquivos = os.listdir(origem)
    for arquivo in arquivos:
        caminho_origem = os.path.join(origem, arquivo)
        caminho_destino = os.path.join(destino, arquivo)
        if arquivo != os.path.basename(destino) and os.path.isfile(caminho_origem):
            os.rename(caminho_origem, caminho_destino)

diretorio_origem = './Testes/Origem'
diretorio_destino = './Testes/Destino'
listar_arquivos(diretorio_origem)
mover_arquivos(diretorio_origem, diretorio_destino)

```
Vide [001_manipulacao.py](./001_manipulacao.py)

## Integração com APIs
A integração com APIs permite que você automatize a coleta e o envio de dados entre diferentes sistemas. Isso é especialmente útil para obter dados de serviços externos, como redes sociais, plataformas de análise ou bancos de dados online.

### Exemplo de Script para Integração com API
```python
# Instalar as bibliotecas se ainda não estiver instalada
# pip install requests pandas matplotlib
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fazer a requisição
url = "https://api.frankfurter.app/latest?from=USD"
response = requests.get(url)

# Verificar se deu certo
if response.status_code == 200:
    data = response.json()
    
    # Extrair as taxas de câmbio
    rates = data["rates"]
    
    # Converter para DataFrame
    df = pd.DataFrame(list(rates.items()), columns=["Moeda", "Taxa"])
    
    # Mostrar as 10 primeiras moedas
    print(df.head(10))

    # Mostrar apenas as moedas BRL, EUR e GBP
    moedas_desejadas = ["BRL", "EUR", "GBP"]
    df_filtrado = df[df["Moeda"].isin(moedas_desejadas)]
    print(f"\nMoedas filtradas:\n{df_filtrado.to_string(index=False)}")

    # Plotar um gráfico de barras das moedas filtradas
    plt.figure(figsize=(10, 6))
    plt.bar(df_filtrado["Moeda"], df_filtrado["Taxa"], color='#6eaa5e')
    plt.xlabel('Moeda')
    plt.ylabel('Taxa de Câmbio')
    plt.title('Taxas de Câmbio - Moedas Filtradas')
    plt.show()
else:
    print("Erro na requisição:", response.status_code)

```
Vide [002_api.py](./002_api.py)

## Integração com Banco de Dados
A integração com bancos de dados permite que você automatize a leitura e escrita de dados em sistemas.

### Exemplo
```python
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
```
>Vide [003_banco.py](./003_banco.py)

## Agendamento de Tarefas
O agendamento de tarefas é fundamental para garantir que processos automatizados sejam executados de forma consistente e sem necessidade de intervenção manual. Ele permite que scripts, programas ou rotinas sejam disparados em horários específicos ou em resposta a eventos, assegurando maior eficiência e confiabilidade na execução de fluxos de trabalho.

### Imoprtância
- **Eficiência**: elimina a necessidade de rodar scripts manualmente.
- **Consistência**: garante que tarefas sejam executadas sempre nos mesmos horários.
- **Escalabilidade**: facilita a manutenção de processos repetitivos em ambientes corporativos.
- **Redução de erros**: diminui a chance de falhas humanas ao automatizar execuções críticas.

### Uso em Linux
No Linux, o agendamento de tarefas é feito principalmente com o **cron**, um serviço que executa comandos em intervalos definidos.
- Arquivo de configuração: `crontab -e`
- Sintaxe básica:
  ```bash
  * * * * * comando
  ```
  Onde cada `*` representa minuto, hora, dia do mês, mês e dia da semana.
- Exemplo: rodar um script Python todos os dias às 9h:
  ```bash
  0 9 * * * python3 /home/usuario/scripts/analise.py
  ```
### Uso em Windows
No Windows, o equivalente ao cron é o **Agendador de Tarefas (Task Scheduler)**.
  - Permite criar tarefas que rodam em horários específicos ou em resposta a eventos (como login ou inicialização do sistema).
  - Configuração pode ser feita pela interface gráfica ou via linha de comando com `schtasks`.
  - Exemplo via Prompt/PowerShell:
    ```powershell
    schtasks /create /sc daily /tn "AnaliseDiaria" /tr "python C:\scripts\analise.py" /st 09:00
    ```
    Esse comando agenda a execução do script às 9h.

