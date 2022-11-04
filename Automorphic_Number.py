n=int(input())
m=n*n
r=str(m)
if r.endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")