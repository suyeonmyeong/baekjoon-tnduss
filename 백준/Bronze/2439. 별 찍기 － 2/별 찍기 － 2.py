import sys

#a,b=map(int,sys.stdin.readline().rstrip().split())
#lst=list(sys.stdin.readline().rstrip().upper())

n= int(sys.stdin.readline().rstrip())
for i in range(n):
	for k in range(n-i-1):
		print(' ',end='')
	for j in range(i+1):
		print('*',end='')
	print()