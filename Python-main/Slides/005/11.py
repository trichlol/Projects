'''
Calcular e mostrar o resultado da expressão:
1/1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/200
'''

soma = 0
fra = 1

while fra <= 200:
    calc = 1/fra
    soma += calc
    fra += 1
print(soma)