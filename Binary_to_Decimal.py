def fun(n):
    power=1
    decimal=0
    while n>0:
        rem=n%10
        n=n//10
        decimal+=rem*power
        power=power*2
    return decimal
n=int(input())
for i in range(n):
    a=int(input())
    print(fun(a))