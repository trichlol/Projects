def funA(lista):
    x = len(lista)
    for i in range(x//2):
        aux = lista[i]
        lista[i] = lista[x-1-i]
        lista[x-1-i] = aux
        print(lista[i])