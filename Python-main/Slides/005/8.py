'''
Ler um número inteiro de 1 a 10 e mostrar a sua tabuada.
'''

print('\nDigite um número de 1 a 10 para descobrir a sua tabuada')
x = int(input('Número: '))
print('')

for i in range(10):
    print(x, ' * ', i+1, ' = ', x*(i+1))