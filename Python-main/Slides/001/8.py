'''
Desenhe um fluxograma e implemente o programa em Python que recebe o raio de uma esfera, calcula e
mostra seu volume.
'''

print('')
print('VOLUME ESFERA')
print('')

R = float(input('Digite o raio da esfera: '))

V = (4 * 3.14 * R**3)/3

print('')
print('O volume da esfera é %.2f' % (V))
print('')