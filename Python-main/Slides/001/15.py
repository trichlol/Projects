'''
Dado um número inteiro positivo X=x1x2 escrito na base 4, os valores de x1ex2 podem variar de 0 a 3.
Se o número inteiro positivo X=x1x2 está escrito na base 8, os valores de x1ex2 podem variar de 0 a 7.
Considere que você deseja converter um número inteiro positivo escrito em qualquer base de 3 a 9 para
a base 2, para isso será necessário converter para a base decimal e depois para a base binária. A 
conversão para a base decimal, é realizada pelo cálculo: Xnovo = x1xb1+x2xb0, resultando em um valor
com dois dígitos (x1x2). Para converter um número escrito na base decimal para a base binária, devemos
realizar sucessivas divisões por 2. Como ainda não aprendemos a estrutura de repetição, esse cálculo
é inviável. A partir do conteúdo discutido até o momento, é possível converter qualquer valor escrito
na base 4 para a base 2. Para isso realize a sequência de comandos:

Divida x1 por dois e guarde o quociente em y1 e o resto em y2;
Divida x2 por dois e guarde o quociente em y3 e o resto em y4;
Escreva Y=1000 x y1 + 100 x y2 + 10 x y3 + y4

Desenhe um fluxograma e implemente um programa em Python que leia um número inteiro positivo escrito
na base 4, calcule e mostre o número correspondente na base binária.
'''

print('\nDigite um valor de dois digitos na base 4\n')
x = int(input('Valor: '))

if x >= 100:
    print('Número possui mais de dois dígitos')
else:
    if x / 10 <= 3.3 and x / 10 >= 0:
        x1 = x // 10
        x2 = x % 10
        
        binario=[6]
        while x != 0:
            for i in range(7):
                binario[i] = x % 2
                x //= 2
            for i in range(6):
                print(binario[i])
        print(x)
    elif x < 0:
        print('Não são aceitos números negativos')
    else:
        print('O número digitado não está na base 4')
#binario = 