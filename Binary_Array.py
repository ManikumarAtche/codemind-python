n=int(input())
d=list(map(int,input().split()))
r=[]
for i in d:
    if i==1 or i==0:
        r.append(i)
if len(r)==len(d):
    print(True)
else:
    print(False)