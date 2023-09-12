'''
Escreva um programa em Python e desenhe um fluxograma que converta para a base 10 um número natural
não nulo de três dígitos denominado X na forma X=x1x2x3 escrito na base B(B é um número inteiro
maior que 1 e menor que 10). Por exemplo, se X=314 e B=7 isto significa que o número é composto pelos
dígitos x1=3, x2=1 e x3=4, e que está escrito na base 7. Para converter esse número para a base 10
basta calcular: 3x72+1x71+4X70=158. Outro exemplo, se X=085 e B=9 isto significa que o número é
composto pelos dígitos x1=0, x2=8 e x3=5, e que está escrito na base 9. Para converter esse número
para a base 10 basta calcular: 0x92+8x91+5X90=77.
'''

print('')
print('DOIDURA DOS TRÊS DÍGITOS')
print('')
X = int(input('Digite um número com três dígitos: '))
B = int(input('Digite a base que será calculada entre um número de 1 à 9: '))
print('')

X1 = X//100
RX1 = X % 100
X2 = RX1 // 10
X3 = RX1 % 10

RESULTADO = X1*B**2 + X2*B + X3

print('O resultado será', RESULTADO)
print('')
