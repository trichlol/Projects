'''
Desenhe um fluxograma e implemente o programa em Python que recebe a largura de uma parede quadrada e
a largura de um azulejo quadrado, calcula e mostra quantos azulejos são necessários para preencher
completamente a parede.
'''

print('')
print('PAREDE QUADRADA')
print('')

P = float(input('Digite a largura da sua parede: '))
A = float(input('Digite a largura do azulejo que deseja utilizar: '))

P = P**2
A = A**2

X = P//A +1

print('')
print('Você irá precisar comprar %f azulejo(s) para a sua parede' % (X))
print('')

#======================================================================================

'''
Comentar sobre o exempo de 1m para 1m = 2 (???)
1.55/0.66
2/0.2
'''