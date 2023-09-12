'''
Para receber a idade de várias pessoas e informe se possui direito a desconto.
Regra para obter o desconto é necessário ter menos de 6 anos ou ser idoso (ter a partir de 60 anos).
Para finalizar a leitura, digite 9999.
'''

idade  = 0

while idade != 9999:
    idade = int(input('Informe a idade: '))

    if idade == 9999:
        print('FIM DA OPERAÇÃO')
    elif idade < 6 or idade >= 60:
        print('Possui direito!')
        print('')
    else:
        print('Não possui direito!')
        print('')