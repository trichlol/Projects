'''
Desenhe um fluxograma e implemente um programa Python que recebe dois números inteiros e mostre o
resultado da divisão deles apenas se o segundo número for diferente de zero. Se o segundo número for
igual a zero, informe que é impossível devido a divisão por zero.
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n2 == 0:
    print('Não é possível dividir por zero')

else:
    x = n1 / n2
    print(x)