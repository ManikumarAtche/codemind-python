def ugly(n):
    if n==0:
        return True
    for i in [2,3,5]:
        while n%i==0:
            n/=i
    return n==1
n=int(input())
if ugly(n):
    print("Ugly Number")
else:
    print("Not Ugly Number")