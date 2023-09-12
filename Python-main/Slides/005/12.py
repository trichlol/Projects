'''
Calcular e mostrar o resultado da expressão
1/1 + 1/2 + 1/3 + ... + 1/N para os 50 primeiros termos
'''

fra = int(input('Digite até onde a expressão deve seguir: '))
soma = 0
cont = 1

if fra <=0:
    print('Pelo amor de Deus, né? Nem começa!')
else:
    while cont <= fra:
        if fra <= 50:
            calc = 1/cont
            soma += calc
        else:
            print('Número limite de 50 ultrapassado!')
            break
        cont += 1
        print(soma)