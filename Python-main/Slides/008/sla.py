import random

qntlinha = int(input('digite o numero de linhas: '))
qntcoluna =int(input('digite o numero de colunas: '))

def criarmatriz(qntlinha, qntcoluna):
    matriz = [0]*qntlinha

    for linha in range(qntlinha):
        matriz[linha] = [0]*qntcoluna
        for coluna in range(matriz[linha]):
            matriz[linha] [coluna] = random.randint(0, 999)
    return matriz

def main(matriz):
    print(matriz)
    
main()