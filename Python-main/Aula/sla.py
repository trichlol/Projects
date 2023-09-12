matriz = [0]*3

for l in range(len(matriz)):
    matriz[l] = [0]*3
    
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input())

print(matriz)