n=int(input())
d=list(map(int,input().split()))
s=set(d)
r=list(s)
c=0
for i in r:
    if i%2==0:
        c+=1
print(c)