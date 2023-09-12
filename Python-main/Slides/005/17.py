'''
Para exibir o menu a seguir e realizar as suas operações:
1 –Ler um novo número e o adicionar em uma somatória
2 –Exibir o valor atual da somatória
3 –Exibir a quantidade de números digitados até o momento
4 –Mostrar a média dos números digitados até o momento
5 -Sair
'''

menu = 0
soma = 0
cont = 0

while menu != 5:
    print('1 – Ler um novo número e o adicionar em uma somatória')
    print('2 – Exibir o valor atual da somatória')
    print('3 – Exibir a quantidade de números digitados até o momento')
    print('4 – Mostrar a média dos números digitados até o momento')
    print('5 – Sair\n')
    
    menu = int(input('Opção: '))
    print('')

    if menu == 1:
        print('Adicionar valor à somatória')
        valor = int(input('Valor: '))
        print('')

        cont += 1
        soma += valor

    elif menu == 2:
        print('SOMATÓRIA ATUAL DE:', soma)
        print('')
    
    elif menu == 3:
        print('Você já adicionou %i números ao total\n' % cont)

    elif menu == 4:
        print('A média total é de: ', soma/cont)
        print('')

    elif menu == 5:
        print('OPERAÇÃO FINALIZADA!')
        break