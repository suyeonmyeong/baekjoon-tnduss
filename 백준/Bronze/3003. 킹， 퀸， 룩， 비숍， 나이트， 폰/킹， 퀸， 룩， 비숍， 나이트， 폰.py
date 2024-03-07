import sys

org=[1,1,2,2,2,8]
res=[]
lst=list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(len(org)):
	res.append(org[i]-lst[i])

print(*res)