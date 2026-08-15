import os

with open('./Testes/Origem/arquivo.txt', 'w') as arquivo:
    arquivo.write('Arquivo de teste')

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
