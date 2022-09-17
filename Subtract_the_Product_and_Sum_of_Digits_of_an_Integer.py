n=int(input())
s=1
r=0
for i in str(n):
    d=int(i)
    s=s*d
    r=r+d
print(s-r)