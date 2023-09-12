num = input().split()

a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

if b>c and d>a and c+d > a+b and c>0 and d>0 and a%2==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')