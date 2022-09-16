n=int(input())
d=list(map(int,input().split()))
m=sorted(d)
if d==m[::-1]:
    print("yes")
else:
    print("no")