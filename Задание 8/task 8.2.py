import math
def distance(a=[],b=[],*args):
    d=0
    v=[]
    for i in range(4):
        for j in range(3):
            d=d+math.sqrt(pow((a[i]-b[j]),2))
            v.append(d)
            iterl = iter(v)
    minimum = maximum = next(iterl)
    for item in iterl:
        if item < minimum:
            minimum = item
    print(minimum)
 
Identify=['X','Y','Z','T']
m1=0
m2=0
min=0
dist=0
arr=[]
print("Введите кординаты точек:")
for i in range(4):
    b=[]
    print("Кординаты точки:",Identify[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
min=-1
for i in range(4):
    j=i+1
    for j in range(3):
        distance(arr[i],arr[j],dist)
        if(min<0)or(dist<min):
            m1=i
            m2=j
            min=dist
print('Минимальная дистанция между точками ',Identify[m1],' и ',Identify[m2],'')
print("Размер дистанции= ",min)