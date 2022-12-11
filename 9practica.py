import random
n=int(input("Введите количество строк и столбцов матрицы:"))
h=("")
matrix=[[random.randrange(10) for i in range(n)] for j in range(n)]
for elem in matrix:
    print(elem)
for k in range(n):
    for l in range(1,n):
        if matrix[k][l]!=matrix[l][k]:
            h=('False')
            break
if h!=('False'):
    print('Матрица симметрична')
else:
    print('Матрица не симметрична')

from random import randint

a = [[randint(10, 99) for i in range(9)] for j in range(7)]
for row in a:
    print(*map('{:2d}'.format, row))
print()

max_elem = a[0][0]
ie = je = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] > max_elem:
            max_elem = a[i][j]
            ie = i
            je = j
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for row in a:
    print(*map('{:2d}'.format, row))