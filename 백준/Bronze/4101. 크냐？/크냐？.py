import sys
a,b=map(int,sys.stdin.readline().rstrip().split())

while(a!=0 and b!=0):
	if a>b:
		print('Yes')
	else:
		print('No')
	a,b=map(int,sys.stdin.readline().rstrip().split())