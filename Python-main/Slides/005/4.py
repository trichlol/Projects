'''
Ler um número inteiro (N) e, se N é maior que 1, mostrar os números inteiros de 1 até N.
Senão, mostre os números de N até 1.
'''

n = int(input('Digite um valor: '))

if n > 1:
    cont = 1
    while cont <= n:
        print(cont)
        cont += 1
else:
    while n <= 1:
        print(n)
        n += 1