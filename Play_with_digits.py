def digit(n):
    summ=0
    while n:
        m=n%10
        summ=summ+m
        n//=10
    return summ
n=int(input())
d=list(map(int,input().split()))
k=[]
for i in d:
    k.append(digit(i))
print(sum(k))