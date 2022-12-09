def f(x):
    n=int(input('Введите число: '))
    if n == 0:
        return x
    x.append(n)
    return f(x)

n=[]
n=f(n)
n.sort()
print('Второе максимальное число: ', n[-2])