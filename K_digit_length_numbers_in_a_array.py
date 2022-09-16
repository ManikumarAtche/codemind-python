a,b=map(int,input().split())
d=list(map(int,input().split()))
r=0
c=0
for i in d:
    s=abs(i)
    r=str(s)
    if len(r)==b:
        c+=1
print(c)