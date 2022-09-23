n=int(input())
m=str(n)
c=0
d=1
for i in m:
    r=int(i)
    c+=r
    d*=r
if c==d:
    print("Spy Number")
else:
    print("Not Spy Number")