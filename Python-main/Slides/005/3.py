'''
Ler um número inteiro (N) maior que 1 e mostrar os números inteiros de 1 até N.
'''

print('\nDigite um valor maior que 1')
n = int(input('Valor: '))
print('')

if n < 1:
    print('Número menor que 1')
else:
    cont = 1
    while n >= cont:
        print(cont)
        cont += 1
    print('')