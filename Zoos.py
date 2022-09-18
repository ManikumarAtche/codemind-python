n=input()
c=0
d=0
for i in range(len(n)):
    if (n[i]=='z'):
        c+=1
    elif (n[i]=='o'):
        d+=1
if d==(2*c):
    print("Yes")
else:
    print("No")