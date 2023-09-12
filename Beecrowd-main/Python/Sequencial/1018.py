valor = int(input())

_100 = valor // 100
resto = valor % 100

_50 = resto // 50
resto %= 50

_20 = resto // 20
resto %= 20

_10 = resto // 10
resto %= 10

_5 = resto // 5
resto %= 5

_2 = resto // 2
resto %= 2

_1 = resto // 1

print(valor)
print('%d nota(s) de R$ 100,00' % _100)
print('%d nota(s) de R$ 50,00' % _50)
print('%d nota(s) de R$ 20,00' % _20)
print('%d nota(s) de R$ 10,00' % _10)
print('%d nota(s) de R$ 5,00' % _5)
print('%d nota(s) de R$ 2,00' % _2)
print('%d nota(s) de R$ 1,00' % _1)