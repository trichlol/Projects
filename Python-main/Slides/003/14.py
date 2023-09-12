'''
Desenhe um fluxograma e implemente um programa em Python que recebe quatro notas de um aluno, calcule
sua média final, mostre sua média final junto com sua situação:

Média Final = (2.P1 + 2.P2 + 3.P3 + 3.P4) / 10

Situação:

Aprovado = se a nota for igual ou superior a 7.0
Reprovado = se a nota for menor que 5.0

Se a nota é igual ou superior a 5.0 e menor que 7.0, leia a nota de exame, calcule e mostre a média
com exame e sua situação:Média com Exame = (Média Final + Exame) / 2
'''

p1 = float(input('Digite a nota da P1: '))
p2 = float(input('Digite a nota da P2: '))
p3 = float(input('Digite a nota da P3: '))
p4 = float(input('Digite a nota da P4: '))
print('')

media = (2*p1 + 2*p2 + 3*p3 + 3*p4) / 10

if media >= 7:
    print('Nota %.1f — Aprovado' % media)

elif media >= 5:
    exame = float(input('Digite a nota do Exame: '))
    media = (exame + media) / 2
    
    if media >= 7:
        print('Nota %.1f — Aprovado' % media)
    else:
        print('Nota %.1f — Reprovado' % media)

else:
    print('Nota %.1f — Reprovado' % media)