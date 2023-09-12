'''
Para garantirmos a segurança na transmissão de dados, podemos codificá-los antes de transmitir.
Suponha um número inteiro positivo X qualquer de 4 dígitos na forma d1d2d3d4 (por exemplo 2371 onde
d1 = 2, d2 = 3, d3 = 7 e d4 = 1). Desenhe um fluxograma e implemente um programa em Python que
transforma o número inteiro X = d1d2d3d4 em um número Y = f1f2f3f4 que corresponde a X codificado
usando a seguinte regra

fi = ((di + 7) mod 10) para i = 1, 2, 3, 4

Exemplificando, se X = 7149 então Y = 4816 pois:

d1 = 7 então f1 = ((7 + 7) mod 10) = 4
d2 = 1 então f2 = ((1 + 7) mod 10) = 8
d3 = 4 então f3 = ((4 + 7) mod 10) = 1
d4 = 9 então f4 = ((9 + 7) mod 10) = 6
'''