import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

lst=list(map(int,sys.stdin.readline().rstrip().split()))
re=0
for i in lst:
	for j in lst:
		for k in lst:
			if i != j and i!=k and j!=k and re < i+j+k<=m:
				re= i+j+k
print(re)