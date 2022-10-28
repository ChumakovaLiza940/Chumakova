n=int(input())
f=1
s=0
for i in range(1,n+1):
    s=s+f*i
    f=i
print(s)