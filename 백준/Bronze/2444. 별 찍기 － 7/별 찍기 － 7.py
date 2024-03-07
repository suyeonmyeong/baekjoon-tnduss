import sys

n= int(sys.stdin.readline().rstrip())
t=n-1
for i in range(1,2*n,2):
	print(' '*t,end='')
	print('*'*i)
	t-=1
t=1
for i in range(2*n-3,0,-2):
	print(' '*t,end='')
	print('*'*i)
	t+=1