n = input().split()

n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])

if n1 < n2:
    if n1 < n3:
        print(n1)
        if n2 < n3:
            print(n2)
            print(n3)
        else:
            print(n3)
            print(n2)
    else:
        print(n3)
        if n1 < n2:
            print(n1)
            print(n2)
        else:
            print(n2)
            print(n1)
else:
    if n2 < n3:
        print(n2)
        if n1 < n3:
            print(n1)
            print(n3)
        else:
            print(n3)
            print(n1)
    else:
        print(n3)
        if n1 < n2:
            print(n1)
            print(n2)
        else:
            print(n2)
            print(n1)

print('')

print(n1)
print(n2)
print(n3)