def fun(a,b):
    for i in a:
        if i in b:
            return(list(i))
a,b=map(int,input().split())
r=list(map(int,input().split()))
s=list(map(int,input().split()))
m=set(r)
k=set(s)
c=0
for i in m:
    if i in k:
        c+=1
print(c)