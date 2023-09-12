'''
Ler um número inteiro (N) e , se N é maior que 1, mostrar os números inteiros pares de 1 até N.
Senão, mostre os números inteiro ímpares de N até 1. 
'''

print('Digite um valor maior que 1')
n = int(input('Valor: '))

if n > 1:
    cont = 1
    while cont <= n:
        if cont % 2 == 0:
            print(cont)
        cont += 1
else:
    while n <= 1:
        if n % 2 ==1:
            print(n)
        n += 1