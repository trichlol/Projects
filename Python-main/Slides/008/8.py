'''
Gerar duas listas (listaAe listaB) de 100 posições cada uma com números inteiros gerados
aleatoriamente. Em seguida, gere uma nova lista (listaC) com a soma dos elementos da listaA
com lista a listaB(percorra cada índice das listas usando implementando uma estrutura de
repetição):
'''

import random

def main():
    ListaA = gerar()
    ListaB = gerar()
    
    print('LISTA A:')
    mostrar(ListaA)
    print('LISTA B:')
    mostrar(ListaB)
    
    ListaC = somar(ListaA, ListaB)
    
    print('SOMA DAS LISTAS:')
    mostrar(ListaC)
    print('MÉDIA DA SOMA:')
    media(ListaC)

def gerar():
    lista = [0]*100
    for i in range(len(lista)):
        lista[i] = random.randint(-9999,9999)
    return lista

def somar(a, b):
    c = [0]*100
    for i in range(len(c)):
        c[i] = a[i] + b[i]
    return c

def media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
        media = soma / len(lista)
    print("%d"%media)

def mostrar(lista):
    for i in range(len(lista)):
        print('O número %d está no índice %d' % (lista[i], i+1))
    
main()