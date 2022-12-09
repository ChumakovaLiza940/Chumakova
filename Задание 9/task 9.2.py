n = int(input())
a = [[0] * n  for i in range (n)]
Ibeg = Ifin = Jbeg = Jfin = 0;
k = 1
i = j = 0;

while k <= n * n:
    a[i][j] = k
    if (i == Ibeg and j < n - Jfin - 1):
        j += 1
    elif (j == n - Jfin - 1 and i < n - Ifin - 1):
        i += 1
    elif (i == n - Jfin - 1 and j > Jbeg):
        j -= 1
    else:
        i -= 1

if ((i == Ibeg + 1) and (j == Jbeg) and (Jbeg != n - Jfin - 1)):
    Ibeg += 1
    Ifin += 1
    Jbeg += 1
    Jfin += 1
k += 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end = '')
    print()