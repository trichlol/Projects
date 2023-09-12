'''
Desenhe um fluxograma e implemente o programa em Python que recebe a largura e a altura de uma parede
retangular, e a largura e altura de um azulejo retangular, calcula e mostra quantos azulejos são
necessários para preencher completamente a parede.
'''

print('')
print('PAREDE RETANGULAR')
print('')

PB = float(input('Digite a largura da sua parede: '))
PH = float(input('Digite a altura da sua parede: '))
print('')
AB = float(input('Digite a largura do azulejo escolhido: '))
AH = float(input('Digite a altura do azulejo esolhido: '))

P = PB*PH
A = AB*AH

X = P//A + 1

print('')
print('Você irá precisar comprar %d azulejo(s) para a sua parede' % (X))
print('')

#=====================================================================================
'''
3
2.44

0.1
0.55
'''