s = 'aвария акция аннотация аллергия администрация'
lst = s.split()
i = 0
while i<len(lst):
    if lst[i].startswith('a') or lst[i].endswith('я'):
      print(lst[i])
    i += 1


