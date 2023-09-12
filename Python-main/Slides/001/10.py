'''
Desenhe um fluxograma e implemente o programa em Python que leia três números reais, calcula a média
ponderada e mostre o resultado.

Média Aritmética = (n1 . 2 + n2 . 3 + n3 . 5) / 10
'''

print('')
print('MÉDIA PONDERADA')
print('')

N1 = float(input('Digite o primeiro valor: '))
N2 = float(input('Digite o segundo valor: '))
N3 = float(input('Digite o terceiro valor: '))

X = (N1*2 + N2*3 + N3*5)/10

print('')
print('O valor da média ponderada é %f' % (X))
print('')