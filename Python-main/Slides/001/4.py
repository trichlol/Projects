'''
Desenhe um fluxograma e implemente o programa em Python que recebe o raio de uma circunferência,
calcula e mostra sua área e seu perímetro.
'''

print('')
print('CÍRCULO')
print('')

R = float(input('Digite o raio do círculo: '))

A = 2 * 3.14 * R
P = 3.14 * R**2

print('')
print('A área do círculo é: %.2f' % (A))
print('O perímetro do círculo é: %.2f' % (P))
print('')