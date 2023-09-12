'''
Suponha que um simples vírus tenha infectado o sistema de banco de dados da Universidade e que, com
o único estrago, ele tenha alterado os RAs dos alunos. Após algum tempo, descobriu-se que dado o RA
gerado pelo vírus RAV = x1x2x3x4x5x6x7x8, o RA correto RAC = y1y2y3y4y5y6y7y8 poderia ser obtido
através das operações: y1=x1, y2=x2, y3=x8, y4=x7, y5=x5, y6=x6, y7=x3 e y8=x4. Exemplificando, se
RAV = 197845602 então RAC = 1940645782. Desenhe um fluxograma e implemente em Python um programa que
leia RAV e gere RAC com 8 dígitos.
'''