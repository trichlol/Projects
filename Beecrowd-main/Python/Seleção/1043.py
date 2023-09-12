n = input().split()

a = float(n[0])
b = float(n[1])
c = float(n[2])

#DIVISÃO DE VALORES

if a > b:
    r1 = b
    if a > c:
        maior = a
        r2 = c
    else:
        maior = c
        r2 = a
else:
    r1 = a
    if b > c:
        maior = b
        r2 = c
    else:
        maior = c
        r2 = b

#TRIÂNGULO OU TRAPÉZIO

soma = r1 + r2

if maior - soma == 0:
    trap = (a+b)*c / 2
    print('Area = %.1f' % trap)
else:
    perimetro = maior + r1 + r2
    print('Perimetro = %.1f' % perimetro)