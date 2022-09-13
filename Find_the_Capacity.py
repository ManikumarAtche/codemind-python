a,b,c=map(int,input().split())
d=((a*b*c*512*2)//1024)
print(d,end='KB')