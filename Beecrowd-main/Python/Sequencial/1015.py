p1 = input().split()

x1 = float(p1[0])
y1 = float(p1[1])

p2 = input().split()

x2 = float(p2[0])
y2 = float(p2[1])

raiz = (x2-x1)**2 + (y2-y1)**2

import math
total = math.sqrt(raiz)

print('%.4f' % total)