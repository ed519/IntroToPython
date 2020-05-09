import numpy as np


array1 = np.arange(-10,11)

zuyg = [x for x in array1 if x%2 ==0]
print(zuyg[:10])

array2 = np.array([4,5,6] * 7)
print(array2)

array3 = np.full((7,7) , 0, dtype=int )

for x in range(7):
    array3[0][x] = 1
    array3[x][0] = 1
    array3[-1][x] = 1
    array3[x][-1] = 1

print(array3)