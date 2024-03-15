import sys

n= int(sys.stdin.readline().rstrip())

lst=[]
for i in range(n):
	a,b=map(int,sys.stdin.readline().rstrip().split())
	lst.append((a,b))

slst=sorted(lst,key=lambda x: (x[0],x[1]))

for i in slst:
	print(*i)