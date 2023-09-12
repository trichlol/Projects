'''
Para garantirmos a segurança na transmissão de dados, podemos codificá-los antes de transmitir.
Suponha um número inteiro positivo X qualquer de 3 dígitos na forma d1d2d3 (por exemplo 237 onde
d1 = 2, d2 = 3 e d3 = 7). Desenhe um fluxograma e implemente um programa em Python que transforma
o número inteiro X = d1d2d3 em um número Y = f1f2f3 que corresponde a X codificado usando a seguinte
regra:

fi = ((dj + 7) mod 10) para i = 1 e j = 3
fi = ((dj + 6) mod 9) para i = 2 e j = 1
fi = (9 mod (dj + 1)) parai = 3 e j = 2

Exemplificando, se X = 714 então Y = 141 pois:

d1 = 7 então f1 = ((4 + 7) mod 10) = 1
d2 = 1 então f2 = ((7 + 6) mod 9) = 4
d3 = 4 então f3 = (9 mod (1 + 1)) = 1
'''