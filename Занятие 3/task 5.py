a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)