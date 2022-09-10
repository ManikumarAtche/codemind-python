def palindrome(n):
    m=str(n)
    rev=m[::-1]
    rev=int(rev)
    if n==rev:
        return True
    return False
n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    if palindrome(i):
            c+=1
print(c)
        