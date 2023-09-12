'''
Desenhe um fluxograma e implemente um programa em Python que recebe dois números reais e informa se
são iguais. Caso sejam diferentes, informe qual é o maior e qual é o menor.
'''

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo valor: '))

if x == y:
    print('Os números são iguais')

else:
    if x > y:
        print(x, ' é maior')
        
    else:
        print(y , 'é maior')