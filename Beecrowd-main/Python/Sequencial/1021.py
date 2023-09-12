valor = input().split('.')

real = float(valor[0])
centavo = float(valor[1])

n100 = real // 100
resto = real % 100

n50 = resto // 50
resto %= 50

n20 = resto // 20
resto %= 20

n10 = resto // 10
resto %= 10

n5 = resto // 5
resto %= 5

n2 = resto // 2
resto %= 2

print('NOTAS:')
print('%d nota(s) de R$ 100.00' % n100)
print('%d nota(s) de R$ 50.00' % n50)
print('%d nota(s) de R$ 20.00' % n20)
print('%d nota(s) de R$ 10.00' % n10)
print('%d nota(s) de R$ 5.00' % n5)
print('%d nota(s) de R$ 2.00' % n2)

m100 = resto // 1
resto %= 1

m50 = centavo // 50
resto = centavo % 50

m25 = resto // 25
resto %= 25

m10 = resto // 10
resto %= 10

m5 = resto // 5
resto %= 5

m1 = resto // 1

print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % m100)
print('%d moeda(s) de R$ 0.50' % m50)
print('%d moeda(s) de R$ 0.25' % m25)
print('%d moeda(s) de R$ 0.10' % m10)
print('%d moeda(s) de R$ 0.05' % m5)
print('%d moeda(s) de R$ 0.01' % m1)