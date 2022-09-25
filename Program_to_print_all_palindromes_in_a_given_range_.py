m=int(input())
n=int(input())
for i in range(m,n+1):
    s=str(i)
    r=s[::-1]
    if r==s:
        print(r,end=' ')