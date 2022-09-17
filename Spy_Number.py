n=int(input())
s=1
r=0
for i in str(n):
    d=int(i)
    s=s*d
    r=r+d
if s==r:
    print("Spy Number")
else:
    print("Not Spy Number")