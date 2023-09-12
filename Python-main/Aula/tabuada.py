notas = [0]*5
soma = 0
i = 0

while i < len(notas):
    notas[i] = int(input(f'botanota {i+1}: '))
    soma += notas[i]
    i+=1
media = soma / len(notas)

print('A média da turma é de ', media)