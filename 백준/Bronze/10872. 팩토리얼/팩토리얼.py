import sys
n= int(sys.stdin.readline().rstrip())
res=1
for i in range(2,n+1):
	res*=i

print(res)