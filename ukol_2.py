import numpy as np
import matplotlib.pyplot
import sys

x = []
y = []

try:
    for line in sys.stdin:
        vstup = line.split()
        x.append(int(vstup[0]))
        y.append(int(vstup[1]))
except IndexError:
    pass

m = np.array([x], dtype=float)
m = m.T
A = m
b = m
n = np.array(y, dtype=float)

j = 0
while j < len(m) - 2:
    b = b * m
    A = np.hstack((A, b))
    j += 1

I = np.ones((len(m), 1), dtype=np.int32)
I = np.hstack((I, A))

reseni = np.linalg.solve(I, n)

for i in reseni:
    print(i)



