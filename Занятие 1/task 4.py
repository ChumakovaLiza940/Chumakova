second = int(input("Введите количество секудн: "))
minutes = second // 60
hours = second //60 // 60
days = second //60 //60 //24
s = second - (minutes * 60 + hours * 60 * 60 + days * 24 * 60 * 60)
print(days, ":", hours, ":",minutes, ":", s)