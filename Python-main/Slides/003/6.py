'''
Desenhe um fluxograma e implemente um programa em Python que recebe um número real e informe se é
igual a zero, número positivo ou negativo.
'''

x = float(input('Digite o número: '))

if x == 0:
    print(x, 'é igual a zero')

else:
    if x < 0:
        print(x, 'é negativo')
    
    else:
        print(x, 'é positivo')