'''
Desenhe um fluxograma e implemente o programa em Python que recebe a largura e a altura de um
retângulo, calcula e mostra sua área e seu perímetro.
'''

print('')
print('ÁREA E PERÍMETRO')
print('')

H = float(input("Digite a altura: "))
B = float(input("Digite a largura: "))

A = H*B
P = H*2 + B*2

print('')
print('A área do quadrilátero é:', A)
print('O perímetro do quadrilátero é:', P)
print('')