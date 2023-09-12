'''
Mostra o N-ésimotermo da Sequencia de Fibonacci.
'''

n = int(input('Digite um valor: '))

cont = 1
x = 0
y = 1

while cont <= n:
    res = x + y
    x = y
    y = res
    cont += 1
print(x)