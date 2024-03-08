import sys

a,b=map(int,sys.stdin.readline().rstrip().split())

mul=1
div=1
for i in range(1,b+1):
	mul*=a
	a-=1
	div*=i
print(mul//div)