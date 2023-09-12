'''
Calcular e mostrar o resultado da expressão:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 + ... + 1/16384
'''

fra = 2
soma = 0

while fra <= 16384:
    calc = 1/fra
    soma += calc
    fra *= 2
print(soma)