import sys

lst=list(map(int,sys.stdin.readline().rstrip().split()))
res=0
for i in lst:
	res+=i*i
print(res%10)