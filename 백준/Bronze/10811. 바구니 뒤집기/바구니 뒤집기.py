import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
lst= [i for i in range(0, n+1)]
for z in range(m):
	i,j=map(int,sys.stdin.readline().rstrip().split())
	tmp=lst[i:j+1]
	tmp.reverse()
	lst[i:j+1]=tmp[:]
print(*lst[1:])
