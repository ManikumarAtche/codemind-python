def fun(a,b):
    if b==0:
        return abs(a)
    else:
        return fun(b,a%b)
m,n=map(int,input().split())
print(fun(m,n))