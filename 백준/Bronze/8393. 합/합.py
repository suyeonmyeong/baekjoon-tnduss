import sys

n= int(sys.stdin.readline().rstrip())
res=0
for i in range(1,n+1,1):
	res+=i

print(res)