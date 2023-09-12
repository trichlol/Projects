'''
Desenhe um fluxograma e implemente o programa em Python que leia três números reais, calcula a média
aritmética e mostre o resultado.

Média Aritmética = (n1 + n2 + n3) / 3
'''

print('')
print('MÉDIA ARITMÉTICA')
print('')

N1 = float(input('Digite o primeiro valor: '))
N2 = float(input('Digite o segundo valor: '))
N3 = float(input('Digite o terceiro valor: '))

X = (N1 + N2 + N3)/3

print('')
print('O valor da média aritmética dos valores inseridos é %f' % (X))
print('')