'''
Para exibir o menu a seguir e realizar as suas operações:
1 –Somar dois números
2 –Subtrair dois números
3 –Multiplicar dois números
4 -Sair
'''

menu = 0

while menu != 4:
    print('\nCalculadora\n')
    print('1 – Somar dois números')
    print('2 – Subtrair dois números')
    print('3 – Multiplicar dois números')
    print('4 – Sair')

    menu = int(input('Opção: '))

    if menu == 1:
        a = int(input('\nInsira o primeiro valor: '))
        b = int(input('Insira o segundo valor: '))
        
        print('\nA soma dos valores são: ', a+b)
    
    elif menu == 2:
        a = int(input('\nInsira o primeiro valor: '))
        b = int(input('Insira o segundo valor: '))
        
        print('\nA sobtração dos valores são: ', a-b)
    
    elif menu == 3:
        a = int(input('\nInsira o primeiro valor: '))
        b = int(input('Insira o segundo valor: '))
        
        print('\nA multiplicação dos valores são: ', a*b)

    elif menu == 4:
        print('\nPROGRAMA ENCERRADO!')
        break