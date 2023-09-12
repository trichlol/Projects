n = int(input('Digite um número inteiro: '))

if n < 0:
    print('Não é possível calcular o fatorial')
else:
    if n == 0 or n == 1:
        print('%d! = 1' % n)
    else:
        f = 1
        
        while n >= 2:
            f *= n
            n -= 1
            
        print('Fatorial = %d' % f)