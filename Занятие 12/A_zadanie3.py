def obratniy_porydok(x):
    if len(x) == 0:
        return x
    else:
        return obratniy_porydok(x[1:]) + x[0]

a = str(input('Введите число: '))
print(obratniy_porydok(a))