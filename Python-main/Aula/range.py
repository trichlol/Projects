lista = []

n = int(input('Digite um valor inteiro e zero para encerrar a leitura: '))

while n != 0:
    lista.append(n)
    n = int(input('Digite um valor inteiro e zero para encerrar a leitura: '))
    
print('Elementos dos índices ímpares')

for i in range(2, len(lista), 2):
    print('%d' % lista[i], end='\t')
    
print('\n\nSomatória dos números ímpares: ', end='\t')

soma = 0

for i in range(len(lista)):
    if lista[i] % 2 == 1:
        soma = soma + lista[i]

print(soma)