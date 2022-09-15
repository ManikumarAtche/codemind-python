v=['a','e','i','o','u','A','E','I','O','U']
n=input()
c=0
for i in n:
    if i in v:
        c+=1
print(c)