n = input().split()

n1 = float(n[0])
n2 = float(n[1])
n3 = float(n[2])
n4 = float(n[3])

media = (n1*2 + n2*3 + n3*4 + n4*1) / 10
print('Media: %.1f' % media)

if media >= 7.0:
    print('Aluno aprovado.')

elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')

    nota = float(input())
    print('Nota do exame: %.1f' % nota)

    final = (media + nota) / 2

    if final >= 5.0:
        print('Aluno aprovado.')
    
    else:
        print('Aluno reprovado.')
    
    print('Media final: %.1f' % final)

elif media < 5.0:
    print('Aluno reprovado.')