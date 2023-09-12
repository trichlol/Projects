'''
Ler vários números enquanto o usuário não digitar um número negativo.
Calcule e mostre a somatória dos números positivos.
'''

soma = 0
n = int(input('Digite um valor: '))
soma = n

if n > 0:

    while n > 0:
        n = int(input('Digite um valor: '))
        if n > 0:
            soma += n
    print(soma)
else:
    print('Número negativo apenas utilizado para finalizar a operação')