'''
Implemente em Python um algoritmo que leia strings para uma matriz quadrada de ordem 2. Em
seguida mostre os elementos da diagonal principal.
'''

def gerarMatriz():
    m = [0.0]*2

    for l in range(len(m)):
        m[l] = [0.0]*2
        for c in range(len(m[l])):
            m[l][c] = input('Digite: ')
    
    return m

def mostrarDiagonal(m):
    for l in range(len(m)):
        print()
        for c in range(len(m[l])):
            if l == c:
                print(m[l][c], end=' ')
            else:
                print(' ', end=' ')
    print()

def mostrarMatriz(m):
    for i in range(len(m)):
        print(m[i], end='\n')

def main():
    m = gerarMatriz()
    print()
    mostrarMatriz(m)
    
    mostrarDiagonal(m)

main()