valores = input().split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

x = (a + b + abs(a-b))/2
maior = (x + c + abs(x-c))/2

print('%d eh o maior' % maior)