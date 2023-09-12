'''
Desenhe um fluxograma e implemente o programa em Python que leia o total de um objeto em estoque, o
total vendido de objetos do mesmo tipo, calcule e mostre o percentual de objetos vendidos.

Total de um Objeto em Estoque (TE) -----------100 %
Total Vendido de Objetos (TV)------------X %

X = TV * 100 / TE
'''

print('')
print('VENDAS TV')
print('')

TOTAL = int(input('Digite o total inicial de TVs: '))
VENDIDO = int(input('Digite quantas TVs foram vendidas desse total: '))

X = VENDIDO * 100 / TOTAL

print('')
print('A sua porcentagem de vendas foi de %.2f' % (X), end='%')
print('')