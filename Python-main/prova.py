m = [0]*3

for l in range(len(m)):
    m[l] = [0]*3
    for c in range(len(m[l])):
        m[l][c] = int(input('Nº: '))

for l in range(len(m)-1, -1, -1):
    print()
    for c in range(len(m[l])-1, -1, -1):
        print(m[l][c], end=' ')
print()