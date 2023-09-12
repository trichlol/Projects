seg = int(input())

min = seg // 60
hor = min // 60
min = min % 60
seg = seg % 60

print('%d:%d:%d' % (hor, min, seg))