'''
Crie uma lista que exiba os valores do input ao contrário
'''

lista = [0]*10
i = 0

while i < len(lista):
    lista[i] = int(input(f'digite {i+1} numero: '))
    i+=1
    
i = -1
while i >= -len(lista):
    print(lista[i])
    i-=1