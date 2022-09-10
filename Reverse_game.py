n=int(input())
d=list(map(int,input().split()))
for i in d:
    s=str(i)
    m=s[::-1]
    print(int(m),end=' ')