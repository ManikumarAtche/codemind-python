def prime(n):
    if n<=1:
        return False
    for i in range(2,(int(n**0.5))+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
x=min(a,b)
y=max(a,b)
c=0
for i in range(x,y+1):
    if i==1 or i<1:
        continue
    if prime(i)==True:
        c+=1
print(c)
    
        
    