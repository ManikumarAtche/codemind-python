n=int(input())
d=list(map(int,input().split()))
r=set(d)
s=list(r)
c=0
for i in s:
    if i%2==1:
        c+=1
print(c)