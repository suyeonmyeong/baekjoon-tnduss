import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
d=dict()
for i in range(1,n+1):
	s= sys.stdin.readline().rstrip()
	d[s]=i
	
k=list(d.keys())
for i in range(m):
	s= sys.stdin.readline().rstrip()
	try:
		ints=int(s)

		print(k[ints-1])
	except:
		print(d[s])