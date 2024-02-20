import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
a=[]
b=[]
for i in range(n):
	a.append(list(map(int,sys.stdin.readline().rstrip().split())))
for i in range(n):
	b.append(list(map(int,sys.stdin.readline().rstrip().split())))
re=[]
for i in range(n):
	for j in range(m):
		a[i][j]+=b[i][j]
		re.append(a[i][j])
	print(*re)
	re=[]