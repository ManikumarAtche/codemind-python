def prime(n):
    k=int(n**0.5)
    if n==1 or n==0:
        return False
    for i in range(2,k+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n)==False:
     print("Not Mega Prime")
elif prime(n):
    
    while n:
        a=n%10
        n=n//10
        if prime(a):
            f=True
        else:
            f=False
            break

if f==True:
    print("Mega Prime")
else:
    print("Not Mega Prime")
    
        
            