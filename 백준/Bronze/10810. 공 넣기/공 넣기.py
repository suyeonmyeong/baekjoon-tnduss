import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
lst=[0]*n
for z in range(m):
	i,j,k=map(int,sys.stdin.readline().rstrip().split())
	for t in range(i-1,j,1):
		lst[t]=k
print(*lst)