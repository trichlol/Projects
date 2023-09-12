numeros = [0]*10

i = 0
while i < len(numeros):
    numeros[i]=int(input(f'digite o {i+1}º numero: '))
    i += 1

i = 0

while i < len(numeros):
    if numeros[i] % 2 == 1:
        i+=1
    else:
        print(f'o {i+1} numero é par')
        i+=1