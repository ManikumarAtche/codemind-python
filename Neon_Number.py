n=int(input())
sq=(n*n)
c=0
for i in str(sq):
    d=int(i)
    c+=d
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")