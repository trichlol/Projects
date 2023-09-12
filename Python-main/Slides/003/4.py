'''
Desenhe um fluxograma e implemente um programa em Python que recebe um número inteiro e informe se é
par ou ímpar.
'''

x = int(input('Digite o número: '))

x = x % 2

if x == 0:
    print('O número é par')

else:
    print('O número é ímpar')