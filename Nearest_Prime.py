def prime(n):
    if n==1 or n==0:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
s=int(input())
for i in range(s):
    p=int(input())
    b=1
    if prime(p):
        print(p)
    else:
        while True:
            if prime(p-b):
                print(p-b)
                break
            elif prime(p+b):
                print(p+b)
                break
            b+=1
    