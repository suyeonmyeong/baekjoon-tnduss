import sys

n= int(sys.stdin.readline().rstrip())
lst=[]
for i in range(n):
	a,b=map(int,sys.stdin.readline().rstrip().split())
	lst.append((a,b))
	
	
lst.sort(key= lambda x: (x[1],x[0]) )
for i in lst:
	print(*i)