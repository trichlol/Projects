f = open("Aula\ma.txt", 'r')
s = f.read()
lista = s.split('\n')
print(s)


f = open("Aula\ma.txt", 'a')
f.write('novo texto1')
f.write('novo texto2')
f.close()


f = open("Aula\ma.txt", 'r')
s = f.read()
f.close()