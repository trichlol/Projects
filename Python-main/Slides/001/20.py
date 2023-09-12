'''
O preço dos produtos de uma empresa é armazenado de forma codificada e são lidos por uma máquina
semelhante (mas não igual a um código de barras. O código tem o formato C = c1c2c3c4c5 (c1, c2, c3, c4
e c5 são dígitos entre 0 e 9). Para determinarmos o preço P = p1p2p3p4 de um determinado produto cujo
código é C, a máquina deve ler C e calcular o preço fazendo as seguintes contas:

p3p4 = C div 1000
p2 = (c1*c2*c3*c4*c5) mod 10
p1 = (c2c3) div 10 (repare que esta operação não é c2*c3)

Exemplificando, se C = 47238 então P = 7447, pois as contas feitas foram: p3p4 = 47238 div 1000 = 47,
p2 = (4*7*2*3*8) mod 10 = 4, p1 = 72 div 10 = 7

Desenhe um fluxograma e implemente um programa em Python que leia C e imprima P com 4 casas.
'''