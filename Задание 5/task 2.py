n = int(input())
d=2
while d <= n:
    if n % d != 0:
        d += 1
    else:
        print(d)
        break
