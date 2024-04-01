import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
d=dict()
for _ in range(n):
	s= sys.stdin.readline().rstrip()
	d[s]=0
lst=[]
for _ in range(m):
	s= sys.stdin.readline().rstrip()
	if s in d:
		lst.append(s)
lst.sort()
print(len(lst))
print(*lst,sep='\n')