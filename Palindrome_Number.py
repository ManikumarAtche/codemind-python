n=int(input())
for i in range(n):
    m=input()
    k=m[::-1]
    if k==m:
        print(True)
    else:
        print(False)