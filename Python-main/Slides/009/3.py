'''
Implemente em Python um algoritmo que leia números reais em duas matrizes 3x2. Calcule o
resultado da subtração da primeira pela segunda matriz.
'''

def gerarMatriz():
    m = [0.0]*3

    for l in range(len(m)):
        m[l] = [0.0]*2
        for c in range(len(m[l])):
            m[l][c] = float(input(f'Digite um valor: '))
    
    return m

def subtrair(m1, m2):
     m = [0.0]*3

     for l in range(len(m)):
        m[l] = [0.0]*2
        for c in range(len(m[l])):
            m[l][c] = m1[l][c] - m2[l][c]

     return m

def main():
    m1 = gerarMatriz()
    print()
    m2 = gerarMatriz()
    
    sub = subtrair(m1, m2)
    print()
    print(sub)

main()