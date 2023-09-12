cod = input('digite o codigo: ')
soma = 0
for i in range(len(cod)):
  a = int(cod[i])
  soma += a
if soma % 2 == 0:
  print('dumbinho')
else:
  print('8-bonito')
