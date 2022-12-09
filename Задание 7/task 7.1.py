from random import *
n = int(input("Введите кол-во чисел в массиве:"))

a = [randint(-100,100) for i in range(n)]
print(*a)
max_el = max(a)
min_el = min(a)
a[a.index(max_el)], a[a.index(min_el)] =
a[a.index(min_el)], a[a.index(max_el)] 
print(*a)