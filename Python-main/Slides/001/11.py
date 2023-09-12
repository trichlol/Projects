'''
Desenhe um fluxograma e implemente o programa em Python que leia dois números inteiros (X e Y),
calcule conforme a fórmula a seguir e mostre o resultado.

Fórmula = (-X) + [ (Y-X) +(-Y) . (X)] + 20
'''

print('')
print('FÓRMULA')
print('')
print('(-X) + [(Y-X) + (-Y) * (X)] +20')
print('')

X = int(input('Digite o valor de X: '))
Y = int(input('Digite o valor de Y: '))

Z = -X + (Y-X) + (-Y) * (X) +20

print('')
print('(-%d) + [(%d-%d) + (-%d) * (%d)] +20' % (X,Y,X,Y,X))
print('O resultado da equação é %d' % (Z))
print('')