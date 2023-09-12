piramide = ['.']*26

input = input().split()

quant = int(input[0])
tipo = input[1]

maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'

letra = 0

if tipo == 'maiusculas':
    for i in range(len(piramide)-1, -1, -1):
        piramide[i] = maiusculas[letra]
        print(piramide)
        letra += 1

        if i == quant:
            break

else:
    for i in range(len(piramide)-1, -1, -1):
        piramide[i] = maiusculas[letra]
        print(piramide)
        letra += 1

        if i == quant:
            break