a,b=map(int,input().split())
d=list(map(int,input().split()))
c=0
for i in d:
    if i%b!=0:
        c+=1
print(c)