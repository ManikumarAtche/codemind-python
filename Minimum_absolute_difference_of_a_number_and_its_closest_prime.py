def prime(n):
    if n<=1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
m=int(input())
b=1
if prime(m):
    print(0)
else:
    while True:
        if prime(m-b):
            print(b)
            break
        elif prime(m+b):
            print(b)
            break
        b+=1
    