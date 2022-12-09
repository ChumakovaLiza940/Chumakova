a = list(map(int, input().split()))

avrg = sum(a) / len(a)
print(avrg)
print(*a)
for i in range(len(a)):
    if a [i] > avrg:
        a[i] = 1
print(*a)