def fun(a,b):
    if b==0:
        return abs(a)
    else:
        return fun(b,a%b)
a,b=map(int,input().split())
print(fun(a,b))