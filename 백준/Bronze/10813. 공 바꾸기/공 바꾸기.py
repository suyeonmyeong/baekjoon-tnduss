import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
lst= [i for i in range(1, n+1)]
for z in range(m):
	i,j=map(int,sys.stdin.readline().rstrip().split())
	lst[i-1],lst[j-1]=lst[j-1],lst[i-1]
print(*lst)