def fun(n):#111
    power=1
    decimal=0
    while n>0:
        rem=n%10 #1
        n=n//10 #11
        decimal+=rem*power#1*1
        power=power*2#1*2
    return decimal#1
m=int(input())
for i in range(m):
    a=int(input())
    print(fun(a))