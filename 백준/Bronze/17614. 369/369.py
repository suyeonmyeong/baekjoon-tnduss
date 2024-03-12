import sys

n= int(sys.stdin.readline().rstrip())
count=0
for i in range(1,n+1):
	s= str(i)
	for j in s:
		if j in ['3','6','9']:
			count+=1

print(count)