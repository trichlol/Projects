'''
Implemente em Python um algoritmo que leia números reais em uma matriz quadrada de ordem 3.
Em seguida,calcule e mostre a somatória dos elementos de cada linha.
'''

def gerarMatriz():
    m = [0.0]*3

    for l in range(len(m)):
        m[l] = [0.0]*3
        for c in range(len(m[l])):
            m[l][c] = float(input('Valor: '))
    
    return m

def calcularSoma(m):
    for l in range(len(m)):
        s = 0
        for c in range(len(m[l])):
            s += m[l][c]
        print(f'Linha {l+1}: {s}')

def main():
    m = gerarMatriz()
    print()
    calcularSoma(m)

main()