import random

def somaLinha(m):
    lista = []
    for l in range(len(m)):
        soma = 0
        for c in range(len(m[l])):
            soma = soma + m[l][c] 
        lista.append(soma)
    return lista

def listaImpar(m):
    lista = []
    for l in range(len(m)):
        for c in range(len(m)):
            if m[l][c] % 2 == 1:
                lista.append(m[l][c])
    return lista

def somaColuna(m):
    lista = []
    for c in range(len(m)):
        soma = 0
        for l in range(len(m[c])):
            soma = soma + m[l][c]
        lista.append(soma)
    return lista

def mediaLinha(m):
    lista = []
    for l in range(len(m)):
        soma = 0
        for c in range(len(m[l])):
            soma = soma + m[l][c]
        media = soma / len(m[c])
        lista.append(media)
    return lista

def gerarMatriz(linha, coluna):
    matriz = [0.0] * linha
    
    for l in range(linha):
        matriz[l] = [0.0] * coluna
        
        for c in range(coluna):
            matriz[l][c] = random.randint(0,10)
            
    return matriz

def gerarMatriz(dim):
    impar = 1
    matriz = [0] * dim
    
    for l in range(dim):
        matriz[l] = [0] * dim
        
        for c in range(dim):
            matriz[l][c] = impar
            impar = impar + 2
    
    return matriz

def mostrarDiagonalPrincipal(m):
    for d in range(len(m)):
        print('%d' % m[d][d], end='\t')

def main():
    dim = int(input('Digite o tamanho da matriz: '))
    
    matriz = gerarMatriz()
    sl = somaLinha(matriz)
    sc = somaColuna(matriz)
    med = mediaLinha(matriz)
    i = listaImpar(matriz)
    most = mostrarDiagonalPrincipal(dim)
    
    print('matriz = ', matriz)
    print('soma = ', sl)
    print('soma coluna = ', sc)
    print('media = ', med)
    print('lista impar = ', i)
    
main()