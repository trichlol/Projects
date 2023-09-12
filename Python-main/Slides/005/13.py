'''
Calcular e mostrar o resultado do fatorial de um número escolhido pelo usuário.
'''

x = int(input('Digite um número fatorial: '))

soma = 1
cont = 1

while cont <= x:
    soma *= cont
    cont += 1
print(soma)