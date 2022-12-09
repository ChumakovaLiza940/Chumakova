from random  import *

n = int(input("Введите порядок матрицы: "))
m=int(input("Введите номер строки: "))

a = [([0] * n) for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = randing(-50,50)

for i in range(n):
    print(*a[i])

max_el = a[0][0]
num_str = 1
print()
for i in range(n):
    for j in range(n):
        if i == j:
            if a[i][j] > max_el:
                max_el = a[i][j]
                num_str = i
print(max_el, num_str, m - 1)
a[num_str], a[m - 1] = a[m -1], a[num_str]

for i in range(n):
    print(*a[i])