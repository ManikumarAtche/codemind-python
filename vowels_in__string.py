n=input()
v=['a','e','i','o','u','A','E','I','O','U']
c=[]
for i in range(len(n)):
    if n[i] in v and n[i] not in c:
        c.append(n[i])
print(*c)